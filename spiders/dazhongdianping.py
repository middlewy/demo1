# -*- encoding:utf-8 -*-
from scrapy.spiders import Spider
import scrapy
from scrapy.selector import Selector
import io,sys
import re

class Dazhongdianping(Spider):
    name = 'dazhongdianping'
    allowed_domins = []
    start_urls = ['http://www.dianping.com/']

    def parse(self, response):
        a = input('请输入您要查找的内容:')
        # print(response.url)
        url = 'https://www.dianping.com/search/keyword/2/0_' + a
        yield scrapy.Request(url=url,callback=self.parse_item)

    def parse_item(self,response):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
        sel = Selector(response)
        all_li = sel.xpath("//div[@id='shop-all-list']/ul/li")
        for li in all_li:
            try:
                link = li.xpath("./div[@class='txt']/div[@class='tit']/a/h4/text()").extract()
                if link == []:
                    raise Exception('title is null')
                else:
                    link = link[0]
                # print(link)
            except:
                print('名字不能为空')
        all_ids = sel.xpath("//ul/li//div[@class='tit']/a/@data-shopid").extract()
        all_id = set(all_ids)
        for id in all_id:
            url = 'http://www.dianping.com/shop/' + str(id)
            yield scrapy.Request(url=url,callback=self.parse_xiangxi)

    def parse_xiangxi(self,response):
        pass





















