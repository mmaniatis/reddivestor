from .Processor import Processor
from bs4 import BeautifulSoup
from com.src.network.ApiRequester import ApiRequester
from com.src.persist.Datastore import Datastore
from com.src.model.CryptoEntry import CryptoEntry
from com.src.coin_hash_constant import COIN_DICT
import datetime
from datetime import timedelta
import re

class CryptoProcessor(Processor):
    coin_hash_table = None
    seen_post_titles = None
    api_requester = None
    datastore = None
    # filter_list = ["A", "THE", "VIA", "AMA", "TOKEN"]
    filter_list=[]
    def __init__(self, api_requester: ApiRequester, datastore: Datastore):
        super(CryptoProcessor, self).__init__()
        self.seen_post_titles = []
        self.coin_hash_table = {}
        self.api_requester = api_requester
        self.datastore = datastore

    def handle(self, message: BeautifulSoup, url: str):
        for message_item in message.findAll(['p','h3']):
            post = message_item.text
            currently_seen_coins = []
            if(post not in self.seen_post_titles):
                for word in post.split(" "):
                    cleaned_word = re.sub('[^A-Za-z0-9]+', '', word).strip()
                    if ( (cleaned_word not in self.filter_list) and (cleaned_word in self.coin_hash_table) and (self.coin_hash_table[cleaned_word] not in currently_seen_coins) ):
                        current_coin = self.coin_hash_table[cleaned_word]
                        crypto_entry = CryptoEntry(post, current_coin, url, datetime.datetime.now())
                        self.datastore.insert(crypto_entry)         
                        currently_seen_coins.append(current_coin)
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
                'limit':'350',
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