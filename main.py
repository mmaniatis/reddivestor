from com.src.Spider import Spider
from com.src.CryptoProcessor import CryptoProcessor
from com.src.network.ApiRequester import ApiRequester
from com.src.persist.MongoDatastore import MongoDatastore
from com.src.passwords import COINMARKETCAP_API_KEY
import threading
import time

#TODO: Need to fix init.. put this into a config for sure.

def init_processor():
    api_requester = ApiRequester()
    mongo_datastore = MongoDatastore()
    return CryptoProcessor(api_requester, mongo_datastore)

processor = init_processor()
processor.populate_coin_hash()
processor.populate_seen_post_titles()

def engine_start():
    interval = 2000 #milliseconds

    print("!!!! Spider Engine starting, initializing processors and spiders !!!!")
    spider_cryptoCurrency = Spider(interval, 'https://www.reddit.com/r/CryptoCurrencies/new/', processor)
    spider_cryptoCurrency.setUpDriver()
    spider_cryptoCurrencyTrading = Spider(interval, 'https://www.reddit.com/r/CryptoCurrencyTrading/new/', processor)
    spider_cryptoCurrencyTrading.setUpDriver()
    spider_cryptoCryptoMarkets = Spider(interval, 'https://www.reddit.com/r/CryptoMarkets/new/', processor)
    spider_cryptoCryptoMarkets.setUpDriver()

    thread = threading.Thread(target=spider_cryptoCurrency.crawlAndRefresh, args=())
    thread.daemon = True    

    thread2 = threading.Thread(target=spider_cryptoCurrencyTrading.crawlAndRefresh, args=())
    thread2.daemon = True

    thread3 = threading.Thread(target=spider_cryptoCryptoMarkets.crawlAndRefresh, args=())
    thread3.daemon = True


    thread.start()
    thread2.start()
    thread3.start()
       

    

def main():
    engine_start()
    while(True):
        print("Engine is up and running...")
        time.sleep(500)

if __name__ == "__main__":
    main()
