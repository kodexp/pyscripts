#!/bin/bash

# suppose proxy has been setup


wget -r -nH -N --cut-dirs=2 ftp://ftp.ga.gov.au/outgoing-emergency-imagery/sentinel/hotspots/ 

#wget -r -nH -N --cut-dirs=1 ftp://ftp.ga.gov.au/outgoing-emergency-imagery/sentinel/MODIS
#mv sentinel/MODIS/* ../MODIS/hotspot/
#mv sentinel/VIIRS/* ../VIIRS/hotspot/
#mv sentinel/AVHRR/* ../AVHRR/hotspot/
#
# the current hotspots will be loaded by the next cronjob rn

cd /home/ec2-user/github/pyscripts/
source zprivate/envars.sh
python datadogapi/hotpup.py

# get WFS
# ogrinfo -ro WFS:"http://sentinel.ga.gov.au/geoserver/sentinel/ows" hotspot_current_4326 > hotspot_current_4326.wfs
wget -O sentinel_current_hotspot.kml "http://sentinel.ga.gov.au/geoserver/sentinel/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=sentinel:hotspot_current&outputFormat=application%2Fvnd.google-earth.kml%2Bxml"


