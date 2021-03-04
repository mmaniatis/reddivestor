import unittest
from unittest.mock import MagicMock
from unittest import mock
from unittest.mock import patch
from com.src.Processor import Processor
from com.src.CryptoProcessor import CryptoProcessor
from com.src.network.ApiRequester import ApiRequester
from com.test.testUtil import *
from com.src.persist.MongoDatastore import MongoDatastore
from bs4 import BeautifulSoup

class TestCryptoProcessorMethods(unittest.TestCase):

    @mock.patch('com.src.network.ApiRequester.ApiRequester')
    @mock.patch('com.src.persist.MongoDatastore.MongoDatastore')
    def test_populate_coin_hash(self, mock_api_requester, mock_mongo_datastore):
        mock_api_requester.get.return_value=generateTestCoinJSONResponse()
        mock_mongo_datastore.insert.return_value= None
        crypto_processor = CryptoProcessor(mock_api_requester, mock_mongo_datastore)
        crypto_processor.populate_coin_hash()
        self.assertTrue(len(crypto_processor.coin_hash_table) > 1)
        
    @mock.patch('com.src.persist.MongoDatastore.MongoDatastore')
    @mock.patch('com.src.network.ApiRequester.ApiRequester')
    def test_handle(self, mock_api_requester, mock_mongo_datastore):
        mock_api_requester.get.return_value = generateTestCoinJSONResponse()
        crypto_processor = CryptoProcessor(mock_api_requester, mock_mongo_datastore)
        crypto_processor.populate_coin_hash()
        soup = BeautifulSoup(generateSimpleTestHTML3Mentions(), 'lxml')
        crypto_processor.handle(soup)
        self.assertTrue(mock_mongo_datastore.insert.call_count, 3)

    @mock.patch('com.src.persist.MongoDatastore.MongoDatastore')
    @mock.patch('com.src.network.ApiRequester.ApiRequester')
    def test_populate_coin_hash_null(self, mock_api_requester, mock_mongo_datastore):
        mock_api_requester.get.return_value = None
        crypto_processor = CryptoProcessor(mock_api_requester, mock_mongo_datastore)
        crypto_processor.populate_coin_hash()
        self.assertTrue(len(crypto_processor.coin_hash_table) == 0)

    @mock.patch('com.src.persist.MongoDatastore.MongoDatastore')
    @mock.patch('com.src.network.ApiRequester.ApiRequester')
    def test_populate_seen_posts(self, mock_api_requester,mock_mongo_datastore):
        mock_mongo_datastore.get.return_value = [{'post':'Test!'}]
        crypto_processor = CryptoProcessor(mock_api_requester, mock_mongo_datastore)
        crypto_processor.populate_seen_post_titles()
        self.assertTrue(len(crypto_processor.seen_post_titles) == 1)


    @mock.patch('com.src.persist.MongoDatastore.MongoDatastore')
    @mock.patch('com.src.network.ApiRequester.ApiRequester')
    def test_populate_seen_posts_2_new_posts(self, mock_api_requester,mock_mongo_datastore):
        crypto_processor = CryptoProcessor(mock_api_requester, mock_mongo_datastore)
        mock_mongo_datastore.get.return_value = [{'post':'Ethereum is fantastic.'}]
        mock_api_requester.get.return_value = generateTestCoinJSONResponse()
        crypto_processor.populate_seen_post_titles()
        crypto_processor.populate_coin_hash()
        soup = BeautifulSoup(generateSimpleTestHTML3Mentions(), 'lxml')
        crypto_processor.handle(soup)
        self.assertTrue(mock_mongo_datastore.insert.call_count, 2)

    @mock.patch('com.src.persist.MongoDatastore.MongoDatastore')
    @mock.patch('com.src.network.ApiRequester.ApiRequester')
    def test_populate_seen_posts_0_new_posts(self, mock_api_requester,mock_mongo_datastore):
        crypto_processor = CryptoProcessor(mock_api_requester, mock_mongo_datastore)
        mock_mongo_datastore.get.return_value = [{'post':'Ethereum is fantastic.'}, {'post': 'I Like LINK because i like defi'}, {'post': ' LTC is great!'}]
        
        mock_api_requester.get.return_value = generateTestCoinJSONResponse()
        crypto_processor.populate_seen_post_titles()
        crypto_processor.populate_coin_hash()
        soup = BeautifulSoup(generateSimpleTestHTML3Mentions(), 'lxml')
        crypto_processor.handle(soup)
        self.assertTrue(mock_mongo_datastore.insert.call_count == 0)

    @mock.patch('com.src.persist.MongoDatastore.MongoDatastore')
    @mock.patch('com.src.network.ApiRequester.ApiRequester')
    def test_populate_seen_posts_NULL_new_posts(self, mock_api_requester,mock_mongo_datastore):
        crypto_processor = CryptoProcessor(mock_api_requester, mock_mongo_datastore)
        mock_mongo_datastore.get.return_value = None
        mock_api_requester.get.return_value = generateTestCoinJSONResponse()
        crypto_processor.populate_seen_post_titles()
        crypto_processor.populate_coin_hash()
        soup = BeautifulSoup(generateSimpleTestHTML3Mentions(), 'lxml')
        crypto_processor.handle(soup)
        self.assertTrue(mock_mongo_datastore.insert.call_count == 3)
# TODO: De couple generateTestCoinJSONResponse and these tests. Changing that util class method will break a lot of tests.

if __name__ == '__main__':
    unittest.main()