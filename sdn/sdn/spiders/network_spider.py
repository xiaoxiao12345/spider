import scrapy
from sdn.items import NetItem

class NetworkSpider(scrapy.Spider):
    name = "network"
    start_urls=[
        "http://www.sdnlab.com/"
    ]
    def parse(self, response):
        for sel in response.xpath(".//div[@id='artcontent']"):
            item = NetItem()
            title = sel.xpath(".//div/div/div/a[@title]/text()").extract()
            for t in title[0]['title']:
                print t

            yield item


