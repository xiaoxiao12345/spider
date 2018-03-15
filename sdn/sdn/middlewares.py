from selenium import webdriver
from scrapy.http import HtmlResponse

class GuandianDownloaderMiddleware(object):
    def process_request(self, request, spider):
        click_page_url = "http://www.sdnlab.com/"
        if request.url == click_page_url:
            driver = webdriver.PhantomJS(executable_path=r'D:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe')
            try:
                driver.get(request.url)
                driver.implicitly_wait(3)

                guandian = ".//div[@class='title-content']/a[3]"
                driver.find_element_by_xpath(guandian).click()
                true_page = driver.page_source
                return HtmlResponse(request.url, body=true_page, encoding='utf-8', request=request,)
            except:
                print("get guandian failed")

        else:
            return None