# -*- econding:utf-8 -*-
from scrapy.linkextractors import LinkExtractor
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
import io,sys
import time

class Jingdong(CrawlSpider):
    name = 'jingdong'
    allowed_domins = []
    start_urls = ['https://search.jd.com/Search?keyword=shoubiao&enc=utf-8&wq=shoubiao&pvid=42e2feeb2c7245a9a172811f9ff0d8ff',]
    # rules = (
    #     Rule(LinkExtractor(allow='https://item.jd.com/\d+.html'),callback='parse_item'),
    # )
    # a = []
    def parse(self,response):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
        sel = Selector(response = response)
        all_divs = sel.xpath("//div[@class='gl-i-wrap']")
        for div in all_divs:
            price = div.xpath("./div[@class='p-price']/strong/i/text()").extract_first()
            title = div.xpath("string(./div[@class='p-name p-name-type-2']/a/em)").extract_first()
            # print(title,price)

        t = time.time()
        tt = '%5f' % t
        surl = 'https://search.jd.com/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=2&s=28&scrolling=y&log_id='+str(tt)
        yield scrapy.Request(url=surl,callback=self.parse_item)

    def parse_item(self,response):
        # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
        # sel = Selector(response=response)
        all_divs = response.xpath("//div[@class='gl-i-wrap']")
        for div in all_divs:
            price = div.xpath("./div[@class='p-price']/strong/i/text()").extract_first()
            title = div.xpath("string(./div[@class='p-name p-name-type-2']/a/em)").extract_first()
            print(title, price)
        # print(response.text)








