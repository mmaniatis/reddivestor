from com.src.passwords import MONGO_PASSWORD
from com.src.persist.Datastore import Datastore
from com.src.model import CryptoEntry
import pymongo

class MongoDatastore(Datastore):
    client = None
    main_db = None
    crypto_col = None

    def __init__(self):
        super()
        self.client = pymongo.MongoClient("mongodb+srv://reddivestor_admin:" + MONGO_PASSWORD + "@cluster0.fco56.mongodb.net/main?retryWrites=true&w=majority")
        self.main_db = self.client.main;
        self.crypto_col = self.main_db["crypto_counts"]


    def insert(self, crypto_entry: CryptoEntry):
        # self.crypto_col.insert({
        #     'post_hash': crypto_entry.post_hash, 
        #     'name': crypto_entry.coin, 
        #     'sub_reddit': crypto_entry.sub_reddit,
        #     'timestamp': crypto_entry.timestamp })
        print("Mock Inserting!")
    
    def display_crypto_col(self):
        print("Displaying currently tracked crypto records: ")
        for crypto in self.crypto_col.find():
            print(crypto)