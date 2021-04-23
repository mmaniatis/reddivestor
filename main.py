from com.src.SingleThreadSpider import SingleThreadSpider
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
    interval = 600 #seconds

    print("!!!! Spider Engine starting, initializing processors and spiders !!!!")
    spider = SingleThreadSpider(interval, processor)
    spider.setUpDriver()
    spider.setUrlList([
        'https://www.reddit.com/r/CryptoCurrencies/new/', 
        'https://www.reddit.com/r/CryptoCurrencyTrading/new/', 
        'https://www.reddit.com/r/CryptoMarkets/new/',
        'https://www.reddit.com/r/CryptoMoonShots/new/',
        'https://www.reddit.com/r/altcoin/new/',
        'https://www.reddit.com/r/Crypto_General/new/',
        'https://www.reddit.com/r/ico/new/',
        'https://www.reddit.com/r/CoinBase/new/',
        'https://www.reddit.com/r/ledgerwallet/new/'])
    spider.crawlAndRefresh()


    # MULTI-THREADED IMPLEMENTATION... NOT NEEDED YET AND DON'T WANT TO PAY FOR EXTRA CPU CORES ON AWS:
    
    # spider_cryptoCurrency = Spider(interval, 'https://www.reddit.com/r/CryptoCurrencies/new/', processor)
    # spider_cryptoCurrency.setUpDriver()
    # spider_cryptoCurrency.getUrl('https://www.reddit.com/r/CryptoCurrencies/new/')
    # spider_cryptoCurrencyTrading = Spider(interval, 'https://www.reddit.com/r/CryptoCurrencyTrading/new/', processor)
    # spider_cryptoCurrencyTrading.setUpDriver()
    # spider_cryptoCryptoMarkets = Spider(interval, 'https://www.reddit.com/r/CryptoMarkets/new/', processor)
    # spider_cryptoCryptoMarkets.setUpDriver()
    # thread = threading.Thread(target=spider_cryptoCurrency.crawlAndRefresh, args=())
    # thread.daemon = True    
    # thread2 = threading.Thread(target=spider_cryptoCurrencyTrading.crawlAndRefresh, args=())
    # thread2.daemon = True
    # thread3 = threading.Thread(target=spider_cryptoCryptoMarkets.crawlAndRefresh, args=())
    # thread3.daemon = True
    # thread.start()
    # thread2.start()
    # thread3.start()
       

    

def main():
    engine_start()
    while(True):
        print("Engine is up and running...")
        time.sleep(500)

if __name__ == "__main__":
    main()
