from threading import Timer
import time
import mysqldb
import mongodb
import sys

def clearout():
    mysqldb.delete()
    mongodb.delete()
    # call "redisdb.delete()" for Activity 13.4
    # call "cassandradb.delete()" for Activity 13.5
    print('Deleted data in all dbs!')

clearout()
sys.exit()