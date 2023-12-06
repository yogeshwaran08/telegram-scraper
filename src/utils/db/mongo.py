import pymongo
from datetime import datetime

mongo_url = 'mongodb://localhost:27017/'
database_name = 'AIXploreTech'
client = pymongo.MongoClient(mongo_url)

db = client[database_name]
collection = db['Telegram-historical-20231206']

"""
data structure
~~~~~~~~~~~~~~
date
time
group_id
group_name
sender_firstname
sender_lastname
sender_id
message_content
"""

def upload_data(data : dict):
    # data["date"] = date
    # data["time"] = time
    collection.insert_one(data)
    # print(f"Inserted document ID: {inserted_document.inserted_id}")