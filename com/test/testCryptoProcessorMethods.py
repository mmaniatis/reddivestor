import unittest
from unittest.mock import MagicMock
from unittest import mock
from com.src.Processor import Processor
from com.src.CryptoProcessor import CryptoProcessor
from com.src.network.ApiRequester import ApiRequester
from com.test.testUtil import *

class TestCryptoProcessorMethods(unittest.TestCase):

    @mock.patch('com.src.network.ApiRequester')
    def test_populate_coin_hash(self, mock_api_requester):
        crypto_processor = CryptoProcessor(mock_api_requester)
        mock_api_requester.get = MagicMock(return_value=generateTestCoinJSONResponse())
        crypto_processor.populate_coin_hash()
        self.assertTrue(len(crypto_processor.coin_hash_table) > 1)
    
    @mock.patch('com.src.network.ApiRequester')
    def test_populate_coin_hash_null(self, mock_api_requester):
        crypto_processor = CryptoProcessor(mock_api_requester)
        mock_api_requester.get = MagicMock(return_value=None)
        crypto_processor.populate_coin_hash()
        self.assertTrue(len(crypto_processor.coin_hash_table) == 0)

if __name__ == '__main__':
    unittest.main()