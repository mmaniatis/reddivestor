import unittest
from com.src.Processor import Processor

class TestProcessorMethods(unittest.TestCase):
    # mock_api_requester = ApiRequester()
    # mock_api_requester.get = MagicMock(return_value=generateTestCoinJSONResponse())

    def testDisplayMethod(self):
        processor = Processor()
        self.assertEqual(processor.display(), True)


if __name__ == '__main__':
    unittest.main()