import unittest
from com.src.Processor import Processor
from com.src.CryptoProcessor import CryptoProcessor

class TestProcessorMethods(unittest.TestCase):
    mock_api_requester = ApiRequester()
    mock_api_requester.get = MagicMock(return_value=generateTestCoinJSONResponse())

    def testPopulate_coin_list():
        #Write some dang gum test cases!

if __name__ == '__main__':
    unittest.main()