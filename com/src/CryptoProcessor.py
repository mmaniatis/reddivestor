from .Processor import Processor
from bs4 import BeautifulSoup
from com.src.network.ApiRequester import ApiRequester

class CryptoProcessor(Processor):
    coin_hash_table = None
    seen_post_titles = None
    api_requester = None

    def __init__(self, api_requester: ApiRequester):
        super(CryptoProcessor, self).__init__()
        self.seen_post_titles = []
        self.coin_hash_table = {}
        self.api_requester = api_requester
        self.populate_coin_list()

    def handle(self, message: BeautifulSoup):
        for message_item in message.findAll(['p','h3']):
            post = message_item.text
            currently_seen_coins = []
            if(post not in self.seen_post_titles):
                for word in post.split(" "):
                    # keeping word case sensitive for now until i find solution to issue of common words being used as coin symbols (the thecoin)
                    # as i iterate over the sentence i don't want to revisit previously seen coins.
                    if (word not in currently_seen_coins and word in self.coin_hash_table):
                        current_coin = self.coin_hash_table[word]
                        #if word is seen then either add to dict, or increment by one 
                        #do a break at end so we can get to next post without double counting.
                        if(current_coin not in self.processor_dict.keys()):
                            self.processor_dict[current_coin] = 1
                            currently_seen_coins.append(current_coin)
                        else:
                            self.processor_dict[current_coin] = self.processor_dict[current_coin] + 1
                            currently_seen_coins.append(current_coin)
            self.seen_post_titles.append(post)
        

    #Purpose of method is to call api_requester, which will need to be refactored to take url as param.. but anyways,
    #i am storing all coins as a hash table as the look ups are instant, and i want to hash 
    #symbols to name 
    def populate_coin_list(self):
        json = self.api_requester.get(
            'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest',
            {'start':'1',
            'limit':'5000',
            'convert':'USD'})
        data = json['data']
        for coin in data:
            self.coin_hash_table[coin['name']] = coin['name']
            self.coin_hash_table[coin['symbol']] = coin['name']
            