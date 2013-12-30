#!/usr/bin/python
# -*- coding: utf-8 -*-

# set the postgres password as postgres
# change the pg_hba.conf from peer to md5
# local   all             postgres                                md5
# restart the server

__author__ = 'fzhang'

import psycopg2
import sys

if __name__ == "__main__":

    con = None

    try:
        con = psycopg2.connect(database='postgres', user='postgres', password='postgres')
        cur = con.cursor()
        cur.execute('SELECT version()')
        ver = cur.fetchone()
        print ver


    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
        sys.exit(1)


    finally:

        if con:
            con.close()
