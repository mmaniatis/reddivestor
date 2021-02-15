import unittest
from com.src.CryptoProcessor import CryptoProcessor
from com.src.Spider import Spider
from unittest.mock import MagicMock

class TestSpiderMethods(unittest.TestCase):

    def testProcessSoup(self):
        processor = CryptoProcessor()
        spider = Spider(5, "", processor)
        spider.setUpDriver = MagicMock(return_value = True)

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()