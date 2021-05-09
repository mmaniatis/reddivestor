from com.src.coin_hash_constant import FILTER_LIST
from .Utility import Utility

class WordFilter:

    @staticmethod
    def handle(word, postList, index):
        if(word.lower() in FILTER_LIST):
            before = -1 if index <= 0 else Utility.cleanWord(postList[index-1]).lower()
            after = -1 if index >= len(postList) else Utility.cleanWord(postList[index+1]).lower()
            return WordFilter.filter(before, word.lower(), after)
        return False

    @classmethod
    def filter(self, before, commonWord, after): 
        if ((after == 'coin' or after == 'token' or after == 'swap' or after == 'protocol' or after == 'fi')):
            return False
        elif (commonWord == 'nano' and (before != 'ledger' and after != 's' and after != 'x')):
            return False
        else:
            return True