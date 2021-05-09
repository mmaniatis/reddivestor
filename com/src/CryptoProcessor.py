from .Processor import Processor
from .WordFilter import WordFilter
from .Utility import Utility
from bs4 import BeautifulSoup
from com.src.network.ApiRequester import ApiRequester
from com.src.persist.Datastore import Datastore
from com.src.model.CryptoEntry import CryptoEntry
from com.src.coin_hash_constant import COIN_DICT, FILTER_LIST
import datetime
from datetime import timedelta

class CryptoProcessor(Processor):
    coin_hash_table = None
    seen_post_titles = None
    api_requester = None
    datastore = None
    wordFilter = None

    def __init__(self, api_requester: ApiRequester, datastore: Datastore):
        super(CryptoProcessor, self).__init__()
        self.seen_post_titles = []
        self.coin_hash_table = {}
        self.api_requester = api_requester
        self.datastore = datastore
        self.wordFilter = WordFilter()
 
    def handle(self, soup: BeautifulSoup, url: str):
        for htmlElement in soup.findAll(['p','h3']):
            post = htmlElement.text
            currently_seen_coins = []
            
            if(post not in self.seen_post_titles):
                index = 0;
                postList = post.split(' ')
                while(index < len(postList) - 1):
                    word = Utility.cleanWord(postList[index])
                    
                    if ((not WordFilter.handle(word, postList, index)) 
                        and (word in self.coin_hash_table) 
                        and (self.coin_hash_table[word] not in currently_seen_coins)):
                        currently_seen_coins.append(self.process_coin(word, post, url))

                    index = index + 1
            self.seen_post_titles.append(post)
        
    #Purpose of method is to call api_requester, which will need to be refactored to take url as param.. but anyways,
    #i am storing all coins as a hash table as the look ups are instant, and i want to hash 
    #symbols to name 
    def populate_coin_hash(self):
        try:
            self.api_requester.open()
            json = self.api_requester.get(
                'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest',
                {'start':'1',
                'limit':'2000',
                'convert':'USD'})
        except:
            print("Error in JSON request.")
        finally:
            self.api_requester.close()
            if json != None:
                data = json['data']
                for coin in data:
                    self.coin_hash_table[coin['name']] = coin['name']
                    self.coin_hash_table[coin['symbol']] = coin['name']
    
    def populate_seen_post_titles(self):
        # Append posts from past 3 days to ensure absolutely no duplicates.
        crypto_entries = self.datastore.get(datetime.datetime.now() - timedelta(hours=72))
        if(crypto_entries != None):
            for entry in crypto_entries:
                self.seen_post_titles.append(entry['post'])

    def populate_coin_list_offline(self):
        self.coin_hash_table = COIN_DICT

    def process_coin(self, cleaned_word, post, url):
        current_coin = self.coin_hash_table[cleaned_word]
        crypto_entry = CryptoEntry(post, current_coin, url, datetime.datetime.now())
        try:
            self.datastore.insert(crypto_entry)
        except(e):
            print(e)
        return current_coin