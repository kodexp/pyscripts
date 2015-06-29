"""
hotspots monitor hotpup.py
__author__ = 'fzhang'
"""
# Configure the module according to your needs
import os, sys
import time
import logging

from datadog import initialize
from datadog import api  # Use Datadog REST API client


options = {}
options['api_key']=os.environ['DD_API_KEY']
options['app_key']=os.environ['DD_APP_KEY']
initialize(**options)


MAX_HOUR_HOTSPOT=6
THRESHOLD=MAX_HOUR_HOTSPOT*60*60

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    handlers=[logging.FileHandler("tmp.log"),  logging.StreamHandler()])
                    #filename='/temp/myapp.log',
                    #filemode='w')

def get_latest_hotspots_acquistion_time(satname_prefix='Aqua', filesuffix='hotspots.txt'):
    """
    get the latest file in a dir/list and return its acq time in epochseconds
    Aqua20150626T034511 20150626T035601
    :param satname_prefix:
    :return:epochseconds
    """
    HOTSPOT_FILES_DIR='/data/sentinel/wget_ftp/hotspots'
    hotfiles=os.listdir(HOTSPOT_FILES_DIR)

    hotspots_time_list=[]
    for afile in hotfiles:
        if afile.startswith(satname_prefix) and afile.endswith(filesuffix):
            acquisition_times= afile[len(satname_prefix):-len(filesuffix)]
            (startt,endt)= acquisition_times.split("Z")[:2]
            hotspots_time_list.append(startt)
            logging.debug("hotspot start and stop %s %s",startt, endt)

        else:
            pass

    #   sort get largest datetime, then converto epochsec.
    # 20150627T060548 20150627T061528
    # 20150624T163117 20150624T164352
    sorted_hotspotdt=sorted(hotspots_time_list)
    latest_hotspot=sorted_hotspotdt[-1]
    logging.debug("first hotspot: %s", sorted_hotspotdt[0])
    logging.debug("last hotspot  %s", latest_hotspot)

    epocsec= convert2epoch(latest_hotspot)

    return epocsec  #epoch seconds

def convert2epoch(dateTtime):
    """
    http://stackoverflow.com/questions/8777753/converting-datetime-date-to-utc-timestamp-in-python
    :param dateTtime:  20150627T170204
    :return:
    """
    epochs = time.time() #-THRESHOLD

    year=dateTtime[:4]
    mm=dateTtime[4:6]
    dd=dateTtime[6:8]
    hh=dateTtime[9:11]
    mm=dateTtime[11:13]
    ss=dateTtime[13:15]

    logging.debug("the date time %s %s %s %s %s %s ",year, mm, dd, hh, mm,ss)

    from datetime import datetime, timedelta

    epochs=(time.mktime(time.strptime(dateTtime, '%Y%m%dT%H%M%S'))) - time.timezone
    # epoch1970 = datetime(1970, 1, 1, 0, 0, 0)
    # epochs = (datetime(int(year),int(mm),int(dd),int(hh),int(mm),int(ss)) - epoch1970).total_seconds()

    return epochs

def dog_event(satname,diffhours):


    hostname = os.uname()[1]
    runuser = os.environ['USER']
    prog_name= sys.argv[0]

    title = satname +': The latest hotspots were acquired %s hours ago'% ( str(diffhours)[:5] )
    tags = ['version:1', 'PythonApp:hotpup.py']

    text =  "It was older than %s hours  "%( MAX_HOUR_HOTSPOT)
    text = text + 'This event was created on %s by %s using program %s ' % (hostname, runuser, prog_name)

    api.Event.create(title=title, text=text, tags=tags)

def dog_counter(difftime):
# Use Statsd, a Python client for DogStatsd
    from datadog import statsd

    statsd.increment('LatestFileMtime')
    statsd.gauge('timeGap', difftime)

# Or ThreadStats, an alternative tool to collect and flush metrics, using Datadog REST API
#from datadog import ThreadStats
# See https://github.com/DataDog/datadogpy

def dog_metric(satname, difftime):
    CurrentPosixTime = time.time()
    CurrentPosixTime10 = time.time() + 10


    # Submit a single point with a timestamp of `now`
    api.Metric.send(metric=satname+'.Latesthotspot.Minutes.Ago', points=difftime)

    # Submit a point with a timestamp (must be ~current)
    #api.Metric.send(metric='my.pair', points=(CurrentPosixTime, 100))

    # Submit multiple points.
    #api.Metric.send(metric='my.series', points=[(CurrentPosixTime, 15), (CurrentPosixTime10, 16)])

    # Submit a point with a host and tags.
    #api.Metric.send(metric='my.series', points=100, host="myhost.example.com", tags=["version:1"])

    # Submit multiple metrics
    #api.Metric.send([{'metric':'my.series', 'points':15}, {'metric':'my1.series', 'points':16}])


if __name__=="__main__":

    SAT_NAMES=['Aqua', 'Terra','Npp', 'Noaa19']

    for sat in SAT_NAMES:
        latest_hotspots_time= get_latest_hotspots_acquistion_time(satname_prefix=sat)

        #time.sleep(1)

        now=time.time()

        logging.debug("current epoch seconds %s", now)

        difftime= now - latest_hotspots_time

        print sat , difftime/3600.0  # hours old

        dog_metric(sat,difftime/3600.0) #submit metric data hours

        #event generator
        if difftime>THRESHOLD:
            dog_event(sat, difftime/3600.0)
            #dog_metric(difftime/60.0)
            pass
