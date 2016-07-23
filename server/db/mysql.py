#! /usr/bin/python

import os 
import math
from ConfigParser import ConfigParser

try:
    import MySQLdb
except ImportError as exc:
    print("Error: failed to import settings module ({})".format(exc))

#parse config
config=ConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../config', 'config.cfg'))

def connect(app_name="local"):
    '''
    |  Open database connection to *app_name*
    |  Return *conn* object to perform database operations for succesful connection
    |  Return 0 for unsucessful connection
    '''
    host=config.get(app_name,"host")
    user=config.get(app_name,"user")
    passwd=config.get(app_name,"passwd")
    db=config.get(app_name,"db")
    charset=config.get(app_name,"charset")
    use_unicode=config.get(app_name,"use_unicode")
    try:
        conn=MySQLdb.connect(host,user,passwd,db,charset=charset,use_unicode=use_unicode)
        return conn, conn.cursor()
    except MySQLdb.Error, e:
        print "ERROR %d IN CONNECTION: %s" % (e.args[0], e.args[1])
        return 0, 0

def write(sql,cursor,conn):
    '''
    |  Perform insert and update operations on the database.
    |  Need to pass the cursor object as a parameter
    '''
    try:
        cursor.execute(sql)
        conn.commit()
    except MySQLdb.ProgrammingError, e:
        print "ERROR %d IN WRITE OPERATION: %s" % (e.args[0], e.args[1])
        print "LAST QUERY WAS: %s" %sql

def read(sql,cursor):
    '''
    |  Perform read operations on the database.
    |  Need to pass the cursor object as a parameter
    '''
    try:
        cursor.execute(sql)
        result=cursor.fetchall()
        return result
    except MySQLdb.ProgrammingError, e:
        print "ERROR %d IN READ OPERATION: %s" % (e.args[0], e.args[1])
        print "LAST QUERY WAS: %s" %sql
