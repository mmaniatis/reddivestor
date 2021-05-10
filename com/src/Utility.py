import re

class Utility:

    @staticmethod
    def cleanWord(word):
        return  re.sub('[^A-Za-z0-9$]+', '', word).strip().lower()