#!/usr/bin/env python2.7

from __future__ import print_function
from distutils.core import setup
import os

version = '0.5'

# Append TeamCity build number if it gives us one.
if 'TC_BUILD_NUMBER' in os.environ and version.endswith('b'):
    version += '-' + os.environ['TC_BUILD_NUMBER']

setup(
    name='hotpies',
    url='http://github.con',
    maintainer='Fei Zhang',
    maintainer_email='fei.zhang@ga.gov.au',
    version=version,
    description='Python code samples ',
    packages=[
        'hello',
        'hello/test',
    ],
    scripts=[
        'script/scripta',
    ],
    requires=[
        'pika',
        'requests',
        'suds',
        'mock'
    ]
)
