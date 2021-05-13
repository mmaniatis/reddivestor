import re

class Utility:

    @staticmethod
    def cleanWord(word):
        return  re.sub('[^A-Za-z0-9]+', '', word).strip()
    
    @staticmethod
    def checkWord(word, coinHashTable):
        if (word in coinHashTable):
            return True

    @staticmethod
    def buildAndCheckWord(list, coinHashTable, index, afterIndex):
        if (afterIndex > (len(list) - 1)):
            return None

        currentWord = Utility.cleanWord(list[index] + list[afterIndex])
        if(Utility.checkWord(currentWord, coinHashTable)):
            return currentWord


        currentWord = Utility.cleanWord(list[index])
        if(Utility.checkWord(currentWord, coinHashTable)):
            return currentWord