class VnExpressSpider(scrapy.Spider):
    name = "vnexpress-net"
    start_urls = [
        '<https://vnexpress.net>',
    ]
    custom_settings = {
        'LOG_LEVEL': logging.WARNING,
        'ITEM_PIPELINES': {'pipeline.mysql_pipe.MysqlWriterPipeline': 1}, # Used for pipeline 1
    }
    def parse_content(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.body, 'html.parser')
        bodyElem = soup.select_one('article.fck_detail')
        item['content'] = ''
        if bodyElem is not None:
            item['content'] = bodyElem.get_text()
        item['domain'] = self.start_urls[0]
        return item
    def parse(self, response):
        for quote in response.css('h3.title-news > a'):
            detail_url = quote.css('a::attr("href")').extract_first()
            if detail_url is not None:
                item = {
                    'title': quote.css('a::text').extract_first(),
                    'url': detail_url,
                }
                request = scrapy.Request(response.urljoin(detail_url), callback=self.parse_content)
                request.meta['item'] = item
                yield request
