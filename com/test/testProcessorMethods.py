import unittest
from com.src.Processor import Processor

class TestProcessorMethods(unittest.TestCase):

    def testDisplayMethod(self):
        processor = Processor()
        self.assertEqual(processor.display(), True)


if __name__ == '__main__':
    unittest.main()