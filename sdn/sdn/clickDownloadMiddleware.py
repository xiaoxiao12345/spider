"""from selenium import webdriver
from scrapy.http import HtmlResponse

class GuandianDownloadMiddleWare(object):
    def process_request(self, request, spider):
        click_page_url = "http://www.sdnlab.com/"
        if request.url == click_page_url:
            driver = webdriver.PhantomJS()
            try:
                driver.get(request.url)
                driver.implicitly_wait(3)

                guandian = "//@class title-content-c"
                """