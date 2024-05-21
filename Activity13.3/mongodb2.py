# pip install pymongo
import pymongo
from pymongo import MongoClient
from datetime import datetime

# make a connection
client = MongoClient('mongodb://localhost:27017/dockerdemo')

# get database
db = client.pluto

# get collection
posts = db.posts


# delete posts collection data
db.posts.drop() 