from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from .Processor import Processor
import time

class Spider:
    processor = None
    crawl_interval = None
    driver = None
    
    def __init__(self, crawl_interval: int, processor: Processor):
        self.processor = processor
        self.crawl_interval = crawl_interval

    def setUpDriver(self):
        try:
            options = Options()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--incognito')
            options.add_argument('--headless')
            options.add_argument("--no-sandbox");
            options.add_argument("--disable-dev-shm-usage");
            self.driver = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver')
            print("Driver set up correctly.")
        except Exception as e:
            print("Error in driver set-up. StackTrace(): ")
            print(e)
            return False
        return True

    def getUrl(self, url):
        self.driver.get(url)

    def crawlAndRefresh(self):
        while True:
            pageSource = self.driver.page_source
            self.process_soup(pageSource, "")
            print("!!! process_soup() complete, hibernating for.. " + str(self.crawl_interval))
            time.sleep(self.crawl_interval)
            self.driver.refresh()
            print("Refreshing page and re-crawling..")
        self.driver.quit()
    
    def process_soup(self, pageSource, url):
        if(pageSource != None and pageSource != ""):
            soup = BeautifulSoup(pageSource, 'lxml')
            self.processor.handle(soup, url)