from .Processor import Processor
from bs4 import BeautifulSoup
from com.src.network.ApiRequester import ApiRequester
from com.src.persist.Datastore import Datastore
from com.src.model.CryptoEntry import CryptoEntry
import datetime

class CryptoProcessor(Processor):
    coin_hash_table = None
    seen_post_titles = None
    api_requester = None
    datastore = None
    def __init__(self, api_requester: ApiRequester, datastore: Datastore):
        super(CryptoProcessor, self).__init__()
        self.seen_post_titles = []
        self.coin_hash_table = {}
        self.api_requester = api_requester
        self.datastore = datastore
        #Have one processor for entire engine so this will only be called once in init().

        self.populate_coin_list_offline()
        # self.populate_coin_hash()

    def handle(self, message: BeautifulSoup):
        for message_item in message.findAll(['p','h3']):
            post = message_item.text
            currently_seen_coins = []
            if(post not in self.seen_post_titles):
                for word in post.split(" "):
                    if (word not in currently_seen_coins and word in self.coin_hash_table):
                        current_coin = self.coin_hash_table[word]
                        crypto_entry = CryptoEntry(post, current_coin, "", datetime.datetime.now())
                        crypto_entry.display()
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
                'limit':'5000',
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
    
    def populate_coin_list_offline(self):
        self.coin_hash_table = {"BTC": "Bitcoin", "Bitcoin":"Bitcoin", "ETH": "Ethereum", "Ethereum":"Ethereum", "BCH": "Bitcoin Cash", "Bitcoin Cash": "BCH", "Litecoin":"Litecoin", "LTC": "Litecoin", "Chainlink": "Chainlink", "LINK": "Chainlink"}

