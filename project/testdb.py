from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/testInv")

db=client.get_database("testInv")

collection =db.get_collection("items")

document={'img': 'static/P00X000-2019092701422/P00X000-2019092701422.jpg',
 'obj': [{'name': 'bottle', 'xmax': 274, 'xmin': 117, 'ymax': 517, 'ymin': 237},
         {'name': 'gun', 'xmax': 444, 'xmin': 249, 'ymax': 368, 'ymin': 215},
         {'name': 'razor_blade',
          'xmax': 360,
          'xmin': 319,
          'ymax': 229,
          'ymin': 184},
         {'name': 'lighter',
          'xmax': 315,
          'xmin': 247,
          'ymax': 217,
          'ymin': 158}],
 'proc_img': 'static/P00X000-2019092701422/output.jpg',
 'timemmddyy': 'Sat Mar 27 08:25:10 2021',
 'timstamp': 1616813710}

response=collection.insert_one(document)
last_inserted_id=response.inserted_id
print("last inserted id : {}".format(last_inserted_id))

