from selenium import webdriver
from scrapy.http import HtmlResponse
import time
class GuandianDownloaderMiddleware(object):
    def process_request(self, request, spider):
        click_page_url = "http://www.sdnlab.com/"
        if request.url == click_page_url:
            driver = webdriver.PhantomJS(executable_path=r'D:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe')
            try:
                driver.get(request.url)
                driver.implicitly_wait(3)
                guandian = ".//div[@class='title-content']/a[3]"
                getmore = "//input[@id='btn-more']"
                driver.find_element_by_xpath(guandian).click()
                for i in range(1):
                    driver.find_element_by_xpath(getmore).click()
                    time.sleep(5)
                true_page = driver.page_source
                return HtmlResponse(request.url, body=true_page, encoding='utf-8', request=request,)
            except:
                print("get guandian failed")

        else:
            return None