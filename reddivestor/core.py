from Spider import *
import threading
import time

processor_dict = {}
def show_process_dict():
    while(True):
        print("Showing contents of processor_dict...")
        current_processor_dict_len = len(processor_dict.keys())
        for key in processor_dict.keys():
            print("Coin: " + key + " | Count: " + str(processor_dict[key]))
        time.sleep(5)    

def engine_start():
    print("######## Spider Engine starting")

    spider_cryptoCurrency = Spider(processor_dict, 'https://www.reddit.com/r/CryptoCurrencies/new/')
    spider_cryptoCurrencyTrading = Spider(processor_dict, 'https://www.reddit.com/r/CryptoCurrencyTrading/new/')
    spider_cryptoCryptoMarkets = Spider(processor_dict, 'https://www.reddit.com/r/CryptoMarkets/new/')

    thread = threading.Thread(target=spider_cryptoCurrency.crawlAndRefresh, args=())
    thread.daemon = True    

    thread2 = threading.Thread(target=spider_cryptoCurrencyTrading.crawlAndRefresh, args=())
    thread2.daemon = True

    thread3 = threading.Thread(target=spider_cryptoCryptoMarkets.crawlAndRefresh, args=())
    thread3.daemon = True


    thread.start()
    thread2.start()
    thread3.start()

    time.sleep(10) #let threads start...
    show_process_dict()
       

    

def main():
    engine_start()
    while(True):
        print("Engine is up and running...")
        time.sleep(5000)

if __name__ == "__main__":
    main()
