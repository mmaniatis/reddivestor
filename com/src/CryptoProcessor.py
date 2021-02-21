from .Processor import Processor
from bs4 import BeautifulSoup
from com.src.network.ApiRequester import ApiRequester


class CryptoProcessor(Processor):
    
    def __init__(self, ApiRequester):
        super(CryptoProcessor, self).__init__()
        self.test_coin_list = ["btc", "bitcoin", "eth", "ethereum", "bch", "bitcoin cash", "bitcoincash", "satoshi", "xrp", "cardano", "ada", "binancecoin", "binance coin", "bnb", "litecoin", "ltc", "chainlink", "link"]
        self.seen_post_titles = []

    def handle(self, message: BeautifulSoup):
        for message_item in message.findAll(['p','h3']):
            post = message_item.text.lower()
            if(post not in self.seen_post_titles):
                for word in post.split(" "):
                    if (word in self.test_coin_list):
                        if(word not in self.processor_dict.keys()):
                            self.processor_dict[word] = 1
                        else:
                            self.processor_dict[word] = self.processor_dict[word] + 1
                        break
            self.seen_post_titles.append(post)
    

#         Key: bitcoin | Count: 13
# Key: btc | Count: 3
# Key: ethereum | Count: 3
# Key: satoshi | Count: 2
# Key: link | Count: 1
# Key: eth | Count: 3
# Key: ada | Count: 1
# Key: cardano | Count: 1
# Engine is up and running...
# Displaying contents of proces