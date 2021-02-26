import unittest
from com.src.Processor import Processor
from com.src.persist.MongoDatastore import MongoDatastore

class TestMongoDatastoreMethods(unittest.TestCase):

    def testMongoDatastore(self):
        mongo_datastore = MongoDatastore()



if __name__ == '__main__':
    unittest.main()