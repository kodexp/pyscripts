#!/bin/bash

# apt search gdal
# apt-get install libgdal-dev python-gdal/trusty

ogrinfo -ro WFS:"http://sentinel.ga.gov.au/geoserver/sentinel/ows" hotspot_current_4326 > hotspot_current_4326.wfs

echo "Hotspots counts:"
grep start_dt hotspot_current_4326.wfs | wc -l

echo "Latest Hotspots :"
grep start_dt hotspot_current_4326.wfs | tail
