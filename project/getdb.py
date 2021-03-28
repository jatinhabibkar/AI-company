from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/testInv")

db=client.get_database("testInv")

collection =db.get_collection("items")

document=collection.find_one()

cursor=collection.find()

for each_documnet in cursor:

    print(each_documnet["timstamp"])

