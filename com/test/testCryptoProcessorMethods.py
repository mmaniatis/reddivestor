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
        mock_api_requester.get.return_value= {'data': [{'name': 'Litecoin', 'symbol':'LTC'}, {'name': 'Ethereum', 'symbol':'ETH'}, {'name': 'Chainlink', 'symbol':'LINK'}] }
        mock_mongo_datastore.insert.return_value= None
        crypto_processor = CryptoProcessor(mock_api_requester, mock_mongo_datastore)
        crypto_processor.populate_coin_hash()
        self.assertTrue(len(crypto_processor.coin_hash_table) > 1)
        
    @mock.patch('com.src.persist.MongoDatastore.MongoDatastore')
    @mock.patch('com.src.network.ApiRequester.ApiRequester')
    def test_handle(self, mock_api_requester, mock_mongo_datastore):
        mock_api_requester.get.return_value = {'data': [{'name': 'Litecoin', 'symbol':'LTC'}, {'name': 'Ethereum', 'symbol':'ETH'}, {'name': 'Chainlink', 'symbol':'LINK'}] }
        crypto_processor = CryptoProcessor(mock_api_requester, mock_mongo_datastore)
        crypto_processor.populate_coin_hash()
        soup = BeautifulSoup("<html> \
                <h3>Ethereum is fantastic.</h3> \
                    <div> \
                    <div><p> Insert dummy text here </p> </div> \
                     </div> \
                <h3>I Like LINK because i like defi</h3> \
                    <div> \
                    <div><p> Do you like it too? </p> </div> \
                     </div> \
                <h3>I like coins</h3> \
                    <div> \
                    <div><p> LTC is great!</p> </div> \
                     </div> \
            </html>", 'lxml')
        crypto_processor.handle(soup, "TestSubReddit.com")
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
    def test_currently_seen_coins(self, mock_api_requester,mock_mongo_datastore):
        crypto_processor = CryptoProcessor(mock_api_requester, mock_mongo_datastore)
        mock_mongo_datastore.get.return_value = []
        mock_api_requester.get.return_value = {'data': [{'name': 'Cardano', 'symbol':'ADA'}] }
        crypto_processor.populate_seen_post_titles()
        crypto_processor.populate_coin_hash()
        soup = BeautifulSoup("<html> \
                <h3>This Cardano coin is fantastic.</h3> \
                    <div> \
                    <div><p> Google searches for Cardano breaks new high records, following breaking all-time high price, as retail investors surge towards ADA. The number of Google for ADA hit the roof since the beginning of February. The search interest for ADA increased with predictions around the crypto assets, which projected the value to more than double by March 6th, 2021. ADA has Increased about 600% from beginning of the year till date.  </p> </div> \
                     </div> \
            </html>", 'lxml')
        crypto_processor.handle(soup, "TestSubReddit.com")
        self.assertTrue(mock_mongo_datastore.insert.call_count == 2)

    @mock.patch('com.src.persist.MongoDatastore.MongoDatastore')
    @mock.patch('com.src.network.ApiRequester.ApiRequester')
    def test_populate_seen_posts_2_new_posts(self, mock_api_requester,mock_mongo_datastore):
        crypto_processor = CryptoProcessor(mock_api_requester, mock_mongo_datastore)
        mock_mongo_datastore.get.return_value = [{'post':'Ethereum is fantastic.'}]
        mock_api_requester.get.return_value = {'data': [{'name': 'Litecoin', 'symbol':'LTC'}, {'name': 'Ethereum', 'symbol':'ETH'}, {'name': 'Chainlink', 'symbol':'LINK'}] }
        crypto_processor.populate_seen_post_titles()
        crypto_processor.populate_coin_hash()
        soup = BeautifulSoup("<html> \
                <h3>Ethereum is fantastic.</h3> \
                    <div> \
                    <div><p> Insert dummy text here </p> </div> \
                     </div> \
                <h3>I Like LINK because i like defi</h3> \
                    <div> \
                    <div><p> Do you like it too? </p> </div> \
                     </div> \
                <h3>I like coins</h3> \
                    <div> \
                    <div><p> LTC is great!</p> </div> \
                     </div> \
            </html>", 'lxml')
        crypto_processor.handle(soup, "TestSubReddit.com")
        self.assertTrue(mock_mongo_datastore.insert.call_count == 2)

    @mock.patch('com.src.persist.MongoDatastore.MongoDatastore')
    @mock.patch('com.src.network.ApiRequester.ApiRequester')
    def test_populate_seen_posts_0_new_posts(self, mock_api_requester,mock_mongo_datastore):
        crypto_processor = CryptoProcessor(mock_api_requester, mock_mongo_datastore)
        mock_mongo_datastore.get.return_value = [{'post':'Ethereum is fantastic.'}, {'post': 'I Like LINK because i like defi'}, {'post': ' LTC is great!'}]
        
        mock_api_requester.get.return_value = {'data': [{'name': 'Litecoin', 'symbol':'LTC'}, {'name': 'Ethereum', 'symbol':'ETH'}, {'name': 'Chainlink', 'symbol':'LINK'}] }
        crypto_processor.populate_seen_post_titles()
        crypto_processor.populate_coin_hash()
        soup = BeautifulSoup("<html> \
                <h3>Ethereum is fantastic.</h3> \
                    <div> \
                    <div><p> Insert dummy text here </p> </div> \
                     </div> \
                <h3>I Like LINK because i like defi</h3> \
                    <div> \
                    <div><p> Do you like it too? </p> </div> \
                     </div> \
                <h3>I like coins</h3> \
                    <div> \
                    <div><p> LTC is great!</p> </div> \
                     </div> \
            </html>", 'lxml')
        crypto_processor.handle(soup, "TestSubReddit.com")
        self.assertTrue(mock_mongo_datastore.insert.call_count == 0)

    @mock.patch('com.src.persist.MongoDatastore.MongoDatastore')
    @mock.patch('com.src.network.ApiRequester.ApiRequester')
    def test_populate_seen_posts_NULL_new_posts(self, mock_api_requester,mock_mongo_datastore):
        crypto_processor = CryptoProcessor(mock_api_requester, mock_mongo_datastore)
        mock_mongo_datastore.get.return_value = None
        mock_api_requester.get.return_value = {'data': [{'name': 'Litecoin', 'symbol':'LTC'}, {'name': 'Ethereum', 'symbol':'ETH'}, {'name': 'Chainlink', 'symbol':'LINK'}] }
        crypto_processor.populate_seen_post_titles()
        crypto_processor.populate_coin_hash()
        soup = BeautifulSoup("<html> \
                <h3>Ethereum is fantastic.</h3> \
                    <div> \
                    <div><p> Insert dummy text here </p> </div> \
                     </div> \
                <h3>I Like LINK because i like defi</h3> \
                    <div> \
                    <div><p> Do you like it too? </p> </div> \
                     </div> \
                <h3>I like coins</h3> \
                    <div> \
                    <div><p> LTC is great!</p> </div> \
                     </div> \
            </html>", 'lxml')
        crypto_processor.handle(soup, "TestSubReddit.com")
        self.assertTrue(mock_mongo_datastore.insert.call_count == 3)

    @mock.patch('com.src.persist.MongoDatastore.MongoDatastore')
    @mock.patch('com.src.network.ApiRequester.ApiRequester')
    def testNanoMention(self, mock_api_requester,mock_mongo_datastore):
        crypto_processor = CryptoProcessor(mock_api_requester, mock_mongo_datastore)
        mock_mongo_datastore.get.return_value = None
        mock_api_requester.get.return_value = {'data': [{'name': 'Nano', 'symbol':'NANO'}, {'name': 'Ethereum', 'symbol':'ETH'}, {'name': 'Chainlink', 'symbol':'LINK'}] }
        crypto_processor.populate_seen_post_titles()
        crypto_processor.populate_coin_hash()
        soup = BeautifulSoup("<html> \
                <h3>I am using the Ledger Nano S these days!</h3> \
                    <div> \
                    <div><p> NANO is great!</p> </div> \
                     </div> \
            </html>", 'lxml')
        crypto_processor.handle(soup, "TestSubReddit.com")
        self.assertEquals(mock_mongo_datastore.insert.call_count,  1)
if __name__ == '__main__':
    unittest.main()