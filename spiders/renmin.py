# -*- encoding:utf-8 -*-
from newspaper import Article
from readability import Document
import scrapy
from scrapy import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule
import io,sys
import urllib

class Renmin(CrawlSpider):
    name = 'renmin'
    allowed_domins = []
    # a = input('请输入您想要得到的内容：')
    start_urls = ['http://search.people.com.cn/cnpeople/news/getNewsResult.jsp']
    # rules = (
    #     Rule(LinkExtractor(allow='http://search.people.com.cn/cnpeople/search.do?pageNum=\d{1}&keyword='+a+'&siteName=news&facetFlag=true&nodeType=belongsId&nodeId=0'),follow=True),
    #     Rule(LinkExtractor(allow='http://\w+.people.com.cn/n1/2018/\d+/\.*.html',restrict_css="div.fr a"),callback='parse_item')
    # )
    def parse(self, response):
        # sel = Selector(response)
        a = input('请输入您想要查找的内容：')
        b = a.encode('utf-8')
        for i in range(1,4):
            url = 'http://search.people.com.cn/cnpeople/search.do?pageNum='+str(i)+'&keyword='+b+'&siteName=news&facetFlag=null&nodeType=belongsId&nodeId='
            yield scrapy.Request(url=url,callback=self.parse_item)

    def parse_item(self,response):
        sel = Selector(response)
        infos = sel.xpath("//div[@class='fr w800']/ul")
        for info in infos:
            href = info.xpath("./li/a/text()").extract_first()
            yield scrapy.Request(url=href,callback=self.parse_xiangxi)

    def parse_xiangxi(self,response):
        # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
        sel = Selector(response)
        # title = sel.xpath("//h1/text()").extract_first().replace(u'\xa0',u'')
        try:
            title = sel.xpath("//h1/text()").extract_first().replace(u'\xa0',u'')
            if len(title) == 0:
                raise Exception ('title is none')
            else:
                print(title)
        except:
            print('title不能为空')
        source = sel.xpath("//div[@class='box01']/div[@class='fl']/a/text()").extract()
        if len(source) == 0:
            source = '无'
        else:
            source = sel.xpath("//div[@class='box01']/div[@class='fl']/a/text()").extract_first()
        print(source)
        keywords = sel.xpath("//meta[@name='keywords']/@content").extract()
        if len(keywords) == 0:
            keywords = '无'
        else:
            keywords = keywords = sel.xpath("//meta[@name='keywords']/@content").extract_first()
        synopsis = sel.xpath("//meta[@name='description']/@content").extract()
        if len(synopsis) == 0:
            synopsis ='无'
        else:
            synopsis = sel.xpath("//meta[@name='description']/@content").extract()[0].replace(u'\xa0',u'')







