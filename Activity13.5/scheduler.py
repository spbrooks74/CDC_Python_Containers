from threading import Timer
import time
import mysqldb
import mongodb
# Uncomment code below for Activity 13.4
import redisdb
# Uncomment code below for Activity 13.5
import cassandradb
import sys

# delete data in all dbs
def clearout():
    mysqldb.delete()
    mongodb.delete()
    redisdb.delete()
    cassandradb.delete()
    print('Deleted data in all dbs!')

# read input argument
argument = len(sys.argv)
if (argument > 1):    
    argument = sys.argv[1]     

# if -clear input argument, delete data
if(argument == '-clear'):
    clearout()
    sys.exit()

# -------------
# time loop
# -------------

def status(stamps,db):
    print(f'Data in {db}:')
    for stamp in stamps:
        print(stamp)
    time.sleep(2)

def mysql():
    mysqldb.write()

def mongo():
    stamps = mysqldb.read()
    status(stamps,'mysql')
    mongodb.write(stamps)

# create function redis() for Activity 13.4:

def redis():
    stamps = mysqldb.read()
    redisdb.write(stamps)

# create function cassandra() for Activity 13.5:

def cassandra():
    stamps = mysqldb.read()
    cassandradb.write(stamps)


def verify():
    stamps = mongodb.read()
    status(stamps,'mongo')
    # call redisdb.read() for Activity 13.4 print results
    lastInsertDate = redisdb.read()
    print(f'Data in Redis: LastInsertDate = {lastInsertDate.decode("utf-8")}')
    # call cassandradb.read() for Activity 13.5 print results
    lastUpdateDate = cassandradb.read()
    print(f'Data in Cassandra: LastUpdateDate = {lastUpdateDate}')

def timeloop():    
    print(f'--- LOOP: ' + time.ctime() + ' ---')
    mysql()
    mongo()
    # call function redis() for Activity 13.4
    redis()
    # call function cassandra() for Activity 13.5
    cassandra()
    verify()
    Timer(5, timeloop).start()

timeloop()