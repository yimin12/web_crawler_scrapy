import redis
import json
import pymongo
redis_client = redis.Redis(host='localhost', port=6379, db=0)
mongo_client = pymongo.MongoClient()
collection = mongo_client.room.lianjia2
while True:
    key, data = redis_client.blpop(['lianjia2:items'])
    # print(key)
    d = json.loads(data)
    collection.insert_one(d)