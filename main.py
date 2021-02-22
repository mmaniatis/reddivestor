from com.src.Spider import Spider
from com.src.CryptoProcessor import CryptoProcessor
from com.src.network.ApiRequester import ApiRequester
from com.src.passwords import COINMARKETCAP_API_KEY
import threading
import time

#TODO: Need to fix init.. put this into a config for sure.

#TODO #2: need to get crypto processor coin list built as a dictionary with object: int
# the object will contain coin name/symbol.. that's how i will track the count 

#TODO #3: import above TODO's as issues on git hub.

def init_processor():
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
    }
    api_requester = ApiRequester(headers)
    return CryptoProcessor(api_requester)

processor = init_processor()

def engine_start():
    interval = 5

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
        print("Displaying contents of processor: ") 
        print(" ")
        time.sleep(20)
        processor.display()

if __name__ == "__main__":
    main()
