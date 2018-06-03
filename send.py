import os 
from pymongo import MongoClient
import time

MONGODB_URI = "mongodb://vighnesh:ganga@ds237700.mlab.com:37700/ganga"
client = MongoClient(MONGODB_URI, connectTimeoutMS=30000)
db = client.get_default_database()
user_records = db.user_records

# Return CPU temperature as a character string                                      
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))


def pushRECORD(record):
    user_records.insert_one(record)
id = int(1)
while True:

    x = getCPUtemperature();
    #print(x)
    #mlab part

    record = {
        "user_id": id+=1,
        "t": x,
        "ph":x/4.9
    }

    pushRECORD(record)
    time.sleep(5)