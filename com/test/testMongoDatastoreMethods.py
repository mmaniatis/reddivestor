import unittest
from com.src.Processor import Processor
from com.src.persist.MongoDatastore import MongoDatastore
from com.src.model.CryptoEntry import CryptoEntry
import datetime

class TestMongoDatastoreMethods(unittest.TestCase):

    def testMongoDatastore(self):
        mongo_datastore = MongoDatastore()
        crypto_entry = CryptoEntry("0xPost_Hash", "Bitcoin", "CryptoMarket", str(datetime.datetime.now()))
        mongo_datastore.insert(crypto_entry)
        mongo_datastore.display_crypto_col()

if __name__ == '__main__':
    unittest.main()