from pymongo import MongoClient

from database import db_util

waferDb = db_util.getWaferDb()
mapCollection = waferDb.maps

result = mapCollection.insert_one({
    "pattern" : "pattern1",
    "body": "123123123"
})

print(result.inserted_id)


