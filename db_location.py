from typing import Collection
import pymongo
import uuid

client = pymongo.MongoClient("mongodb+srv://KeanuWinardi:keanuwinardi@cluster0.dricbtm.mongodb.net/?retryWrites=true&w=majority")
db = client.Lokasi
collection = db.Location

def locatioon(kecepatan,latitude,longitude,timestamp):
    data = {
        "ID transaksi": str(uuid.uuid4()),
        "kecepatan": kecepatan,
        "latitude": latitude,
        "longitude": longitude,
        "timestamp": timestamp
    }
    records = collection.insert_one(data)
    print("data tersimpan",records)