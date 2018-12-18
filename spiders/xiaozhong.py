# -*- encoding:utf-8 -*-
from newspaper import Article
from readability import Document
import scrapy
from scrapy import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule
import urllib.request
import re
import io,sys

class Xiaozhong(CrawlSpider):
    name = 'xiaozhong'
    allowed_domins = []
    start_urls = ['http://www.36k.cn/article/news/100-1.html']
    rules = {
        Rule(LinkExtractor(allow='http://www.36k.cn/article/news/100-\d+.html'),follow=True),
        Rule(LinkExtractor(allow='http://www.36k.cn/artinfo/\d{3}.html', restrict_css='ul.artlist a'),
             callback='parse_item'),
    }

    def parse_item(self,response):
        # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
        url = response.url
        # news = Article(url=url,language = 'zh')
        # news.download()
        # news.parse()
        # title = news.title
        html = urllib.request.urlopen(url).read()
        title = Document(html).short_title()
        sel = Selector(response)
        # authors = sel.xpath("")
        source = sel.xpath("//div[@class='aattr']/a/text()").extract_first()
        date = sel.xpath("//div[@class='aattr']/text()").extract()[1]
        atime = re.findall('时间：(.*)',date,re.S)[0]
        print(atime)











