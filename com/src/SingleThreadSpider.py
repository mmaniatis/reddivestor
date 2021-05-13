from com.src.Spider import Spider
from com.src.Processor import Processor
import time

class SingleThreadSpider(Spider):
    urls = None

    def __init__(self, crawl_interval: int,  processor: Processor):
        super(SingleThreadSpider, self).__init__(crawl_interval, processor)


    def setUrlList(self, urls: list):
        self.urls = urls

    def crawlAndRefresh(self):
        while True:
            for url in self.urls:
                self.getUrl(url)
                pageSource = self.driver.page_source
                self.process_soup(pageSource, url)
                print("Current URL: " + url)
                print("!!! process_soup() complete, hibernating for.. " + str(self.crawl_interval))
                print("Refreshing page and re-crawling..")
            time.sleep(self.crawl_interval)
        self.driver.quit()