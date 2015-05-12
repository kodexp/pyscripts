# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:14:01 2015

@author: fzhang

Ref: http://www.pythonforbeginners.com/python-on-the-web/how-to-use-urllib2-in-python/

"""

import sys
from urllib2 import Request, urlopen, URLError

someurl='http://www.tle.info/data/resource.txt'

if __name__ == "__main__":
    
    if len(sys.argv)>1:
        someurl=sys.argv[1]
    else:
        print "USAGE eg: %s %s"%(sys.argv[0], 'http://www.tle.info/data/resource.txt' )
        sys.exit()
    
    req = Request(someurl)
    
    try:
        response = urlopen(req)
    
    except URLError, e:
    
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
    
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
    else:
        # everything is fine
        print response.read()