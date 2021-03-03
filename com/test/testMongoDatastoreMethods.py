import unittest
from com.src.Processor import Processor
from com.src.persist.MongoDatastore import MongoDatastore
from datetime import timedelta
from com.src.model.CryptoEntry import CryptoEntry
import datetime

class TestMongoDatastoreMethods(unittest.TestCase):

    def testMongoDatastore(self):
        # mongo_datastore = MongoDatastore()
        # results = mongo_datastore.get(datetime.datetime.now() - timedelta(hours=24))
        
        # for x in results:
        #     print(x)
        # mongo_datastore.display_crypto_col()
        pass

if __name__ == '__main__':
    unittest.main()