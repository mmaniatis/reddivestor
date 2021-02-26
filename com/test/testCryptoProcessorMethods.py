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
    def test_populate_coin_hash(self, mock_api_requester, mongo_datastore):
        # crypto_processor = CryptoProcessor(mock_api_requester, mongo_datastore)
        # mock_api_requester.get = MagicMock(return_value=generateTestCoinJSONResponse())
        # crypto_processor.populate_coin_hash()
        # self.assertTrue(len(crypto_processor.coin_hash_table) > 1)
        pass

    @mock.patch('com.src.network.ApiRequester')
    def test_end_to_end(self, mock_api_requester):
        mongo_datastore = MongoDatastore()
        crypto_processor = CryptoProcessor(mock_api_requester, mongo_datastore)
        # mock_api_requester.get = MagicMock(return_value=generateTestCoinJSONResponse())
        soup = BeautifulSoup(generateSimpleTestHTML3Mentions(), 'lxml')
        crypto_processor.handle(soup)

    
    @mock.patch('com.src.network.ApiRequester')
    @mock.patch('com.src.persist.MongoDatastore')
    def test_populate_coin_hash_null(self, mock_api_requester, mongo_datastore):
        # crypto_processor = CryptoProcessor(mock_api_requester, mongo_datastore)
        # mock_api_requester.get = MagicMock(return_value=None)
        # crypto_processor.populate_coin_hash()
        # self.assertTrue(len(crypto_processor.coin_hash_table) == 0)
        pass

if __name__ == '__main__':
    unittest.main()