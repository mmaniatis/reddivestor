import unittest
from com.src.CryptoProcessor import CryptoProcessor
from com.src.Spider import Spider
from com.src.network.ApiRequester import ApiRequester
from unittest.mock import MagicMock
from com.test.testUtil import *

class TestSpiderMethods(unittest.TestCase):
    mock_api_requester = ApiRequester()

    def testProcessSoup(self):
        self.mock_api_requester.get = MagicMock(return_value=generateTestCoinJSONResponse())
        processor = CryptoProcessor(self.mock_api_requester)
        spider = Spider(5, "", processor)
        spider.pageSource = generateSimpleTestHTML3Mentions()
        spider.process_soup()

        self.assertEqual(len(spider.processor.processor_dict.keys()), 3)

    def testProcessSoupEmptySource(self):
        self.mock_api_requester.get = MagicMock(return_value=generateTestCoinJSONResponse())
        processor = CryptoProcessor(self.mock_api_requester)
        spider = Spider(5, "", processor)
        spider.pageSource = ""
        spider.process_soup()
        self.assertEqual(len(spider.processor.processor_dict.keys()), 0)

    def testProcessSoupNullSource(self):
        self.mock_api_requester.get = MagicMock(return_value=generateTestCoinJSONResponse())
        processor = CryptoProcessor(self.mock_api_requester)
        spider = Spider(5, "", processor)
        spider.pageSource = None
        spider.process_soup()
        self.assertEqual(len(spider.processor.processor_dict.keys()), 0)

#TODO: GenerateComplexTestHTML.. waiting on issue #16

if __name__ == '__main__':
    unittest.main()