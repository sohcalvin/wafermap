from pymongo import MongoClient

def getWaferDb():
    client = MongoClient() # Defaults localhost interface on port 27017.
    # client = MongoClient("mongodb://mongodb0.example.net:27019")
    db = client.waferdb # or client["wafermap"]
    return db;
    