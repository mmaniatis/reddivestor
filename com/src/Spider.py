from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from .Processor import Processor
import time

class Spider:
    processor = None
    crawl_interval = None
    pageSource = None
    driver = None
    url = None
    
    def __init__(self, crawl_interval: int, url: str, processor: Processor):
        self.processor = processor
        self.crawl_interval = crawl_interval
        self.pageSource = ""
        self.url = url

    def setUpDriver(self):
        try:
            options = Options()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--incognito')
            options.add_argument('--headless')
            options.add_argument("--no-sandbox");
            options.add_argument("--disable-dev-shm-usage");
            self.driver = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver')
            self.driver.get(self.url)
            print("Driver set up correctly.")
        except Exception as e:
            print("Error in driver set-up. StackTrace(): ")
            print(e)
            return False
        return True

    def crawlAndRefresh(self):
        print("Starting the crawl of: " + str(self.url))
        while True:
            self.pageSource = self.driver.page_source
            self.process_soup()
            print("!!! process_soup() complete, hibernating for.. " + str(self.crawl_interval))
            time.sleep(self.crawl_interval)
            self.driver.refresh()
            print("Refreshing page and re-crawling..")
        self.driver.quit()
    
    def process_soup(self):
        if(self.pageSource != None and self.pageSource != ""):
            soup = BeautifulSoup(self.pageSource, 'lxml')
            self.processor.handle(soup)