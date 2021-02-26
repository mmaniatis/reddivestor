from com.src.passwords import MONGO_PASSWORD
from com.src.persist.IDatastore import IDatastore
import pymongo

class MongoDatastore(IDatastore):
    def __init__(self):
        client = pymongo.MongoClient("mongodb+srv://reddivestor_admin:" + MONGO_PASSWORD + "@cluster0.fco56.mongodb.net/main?retryWrites=true&w=majority")
        main_db = client.main;

        crypto_col = main_db["crypto_counts"]

        for crypto in crypto_col.find():
            print(crypto)

    # def update(self, params):
        