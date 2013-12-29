#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'fzhang'

import requests
# requests is urllib3  better than urllib2

r = requests.get('http://live.osgeo.org/en/overview/overview.html', auth=('user', 'pass'))

print r.status_code
print r.headers['content-type']
print r.text

# ------
# 200
# 'application/json'