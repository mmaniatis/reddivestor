import unittest
from unittest.mock import MagicMock
from unittest import mock
from com.src.Processor import Processor
from com.src.CryptoProcessor import CryptoProcessor
from com.src.network.ApiRequester import ApiRequester
from com.test.testUtil import *
from com.src.persist.MongoDatastore import MongoDatastore
from bs4 import BeautifulSoup

class TestCryptoProcessorMethods(unittest.TestCase):

    @mock.patch('com.src.network.ApiRequester')
    @mock.patch('com.src.persist.MongoDatastore')
    def test_populate_coin_hash(self, mock_api_requester, mock_mongo_datastore):
        crypto_processor = CryptoProcessor(mock_api_requester, mock_mongo_datastore)
        mock_api_requester.get = MagicMock(return_value=generateTestCoinJSONResponse())
        crypto_processor.populate_coin_hash()
        self.assertTrue(len(crypto_processor.coin_hash_table) > 1)
        

    @mock.patch('com.src.network.ApiRequester')
    @mock.patch('com.src.persist.MongoDatastore')
    def test_handle(self, mock_api_requester, mock_mongo_datastore):
        mongo_datastore = MongoDatastore()
        mock_api_requester.get = MagicMock(return_value=generateTestCoinJSONResponse())
        crypto_processor = CryptoProcessor(mock_api_requester, mock_mongo_datastore)
        mock_mongo_datastore.insert = MagicMock(return_value= None)
        soup = BeautifulSoup(generateSimpleTestHTML3Mentions(), 'lxml')
        crypto_processor.handle(soup)
        self.assertTrue(mock_mongo_datastore.insert.call_count, 3)

    
    @mock.patch('com.src.network.ApiRequester')
    @mock.patch('com.src.persist.MongoDatastore')
    def test_populate_coin_hash_null(self, mock_api_requester, mock_mongo_datastore):
        crypto_processor = CryptoProcessor(mock_api_requester, mock_mongo_datastore)
        mock_api_requester.get = MagicMock(return_value=None)
        print(len(crypto_processor.coin_hash_table))
        self.assertTrue(len(crypto_processor.coin_hash_table) == 0)

if __name__ == '__main__':
    unittest.main()