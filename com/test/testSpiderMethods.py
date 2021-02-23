import unittest
from com.src.CryptoProcessor import CryptoProcessor
from com.src.Spider import Spider
from com.src.network.ApiRequester import ApiRequester
from unittest.mock import MagicMock
from com.test.testUtil import *
from unittest import mock


class TestSpiderMethods(unittest.TestCase):

    @mock.patch('com.src.network.ApiRequester')
    def testProcessSoup(self, mock_api_requester):
        mock_api_requester.get = MagicMock(return_value=generateTestCoinJSONResponse())
        processor = CryptoProcessor(mock_api_requester)
        spider = Spider(5, "", processor)
        spider.pageSource = generateSimpleTestHTML3Mentions()
        spider.process_soup()

        self.assertEqual(len(spider.processor.processor_dict.keys()), 3)
    
    @mock.patch('com.src.network.ApiRequester')
    def testProcessSoupEmptySource(self, mock_api_requester):
        mock_api_requester.get = MagicMock(return_value=generateTestCoinJSONResponse())
        processor = CryptoProcessor(mock_api_requester)
        spider = Spider(5, "", processor)
        spider.pageSource = ""
        spider.process_soup()
        self.assertEqual(len(spider.processor.processor_dict.keys()), 0)

    @mock.patch('com.src.network.ApiRequester')
    def testProcessSoupNullSource(self, mock_api_requester):
        mock_api_requester.get = MagicMock(return_value=generateTestCoinJSONResponse())
        processor = CryptoProcessor(mock_api_requester)
        spider = Spider(5, "", processor)
        spider.pageSource = None
        spider.process_soup()
        self.assertEqual(len(spider.processor.processor_dict.keys()), 0)

#TODO: GenerateComplexTestHTML.. waiting on issue #16

if __name__ == '__main__':
    unittest.main()