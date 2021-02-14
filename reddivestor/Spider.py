from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
class Spider:
    #Test coin list
    test_coin_list = ["btc", "bitcoin", "eth", "ethereum", "bch", "bitcoin cash", "bitcoincash", "satoshi", "xrp", "cardano", "ada", "binancecoin", "binance coin", "bnb", "litecoin", "ltc", "chainlink", "link"]
    
    def __init__(self, processor_dict, url):
        self.processor_dict = processor_dict
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver')
        # self.driver.set_window_size(1080,800)

        self.driver.get(url)
        self.driver.refresh()
        self.pageSource = ""
        self.seen_post_titles = []

    def crawlAndScrollReddit(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.pageSource += self.driver.page_source
            soup = BeautifulSoup(self.pageSource, 'lxml')
            self.populateElemList(soup)
            self.show()
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                self.driver.quit()
                break

            last_height = new_height

        self.driver.quit()

    def crawlAndRefresh(self):
        while True:
            soup = BeautifulSoup(self.driver.page_source, 'lxml')
            self.process_soup(soup)

            time.sleep(5)
            print("Refreshing page and re-crawling..")
            self.driver.refresh()
            
        self.driver.quit()
    
        
    def process_soup(self,soup):
        for element in soup.findAll('h3'):
            post_title = element.text.lower()
            if((post_title not in self.seen_post_titles)):
                for word in post_title.split(" "):
                    if (word in self.test_coin_list):
                        if(word not in self.processor_dict.keys()):
                            self.processor_dict[word] = 1
                        else:
                            self.processor_dict[word] = self.processor_dict[word] + 1
            self.seen_post_titles.append(post_title)


    def show(self):
        for elem in self.seen_post_titles:
            print(elem)