from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from Processor import Processor
import time

class Spider:
    def __init__(self, crawl_interval: int, url: str, processor: Processor):
        #Class variables:
        self.processor = processor
        self.crawl_interval = crawl_interval
        self.pageSource = ""
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver')
        self.driver.get(url)
        # self.driver.refresh() Might need this.. TODO: Test and find out.

    def crawlAndRefresh(self):
        while True:
            soup = BeautifulSoup(self.driver.page_source, 'lxml')
            self.processor.handle(soup)
            time.sleep(self.crawl_interval)
            print("Refreshing page and re-crawling..")
            self.driver.refresh()
            
        self.driver.quit()