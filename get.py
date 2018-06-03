import os
import time

from pymongo import MongoClient
MONGODB_URI = "mongodb://vighnesh:ganga@ds237700.mlab.com:37700/ganga"
client = MongoClient(MONGODB_URI, connectTimeoutMS=30000)
db = client.get_default_database()
user_records = db.user_records

def getRECORD(user_id):
    records = user_records.find_one({"user_id":user_id})
    return records

i=int(2)
j=int(4)
while True:
	record = getRECORD(i)
    rec = list(record.values())
    #print(rec[2])
    s = str(rec[2])+','+str(rec[3])
    
    f=open("data.txt", "a+")
    f.write(s)
    f.write("\n")
    f.close()
    time.sleep(5)