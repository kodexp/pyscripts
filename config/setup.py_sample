#!/usr/bin/env python2.7

from __future__ import print_function
from distutils.core import setup
import os

version = '0.5'

# Append TeamCity build number if it gives us one.
if 'TC_BUILD_NUMBER' in os.environ and version.endswith('b'):
    version += '-' + os.environ['TC_BUILD_NUMBER']

config={
    'name':'hotpies',
    'url':'http://github.con',
    'maintainer':'Fei Zhang',
    'maintainer_email':'feizhang@gmail.com',
    'version':version,
    'description':'Python samples ',
    'packages':[
        'topy/hello',
        'topy/logging',
        'topy/subproc',
        'topy/fabric_admin',
        'tests', ],
    'scripts':[ 'bin/scripta', ],
    'requires':[ 'pika', 'requests', 'suds', 'mock' ]
}


setup(**config)
