import scrapy
import logging
from scrapy.crawler import CrawlerProcess
import json
import csv
import time
from bs4 import BeautifulSoup
from datetime import datetime
from gensim.models import CoherenceModel
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
from crawler.crawl import GenkSpider, VnExpressSpider, Kenh14Spider, DantriSpider, DevToApi
# process.crawl(VnExpressSpider)
# process.crawl(GenkSpider)
# process.crawl(Kenh14Spider)
# process.crawl(DantriSpider)
process.crawl(DevToApi)
process.start()
