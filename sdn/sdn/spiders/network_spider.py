import scrapy

class NetworkSpider(scrapy.Spider):
    name = "network"
    start_urls=[
        "http://www.sdnlab.com/"
    ]
    def parse(self, response):
        filename = 'jiagou.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

