#-*- coding:utf-8 -*--
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from ..items import NewsItem
import re

class Dayinhu(CrawlSpider):
    name = 'dayinhu'
    allowed_domins = []
    start_urls = ['http://www.dayinhu.com/news/category/%E7%A7%91%E6%8A%80%E5%89%8D%E6%B2%BF',]
    rules = (
        Rule(LinkExtractor(allow='http://www.dayinhu.com/news/category/%E7%A7%91%E6%8A%80%E5%89%8D%E6%B2%BF/page/\d+'),follow=True),
        Rule(LinkExtractor(allow='http://www.dayinhu.com/news/\d{6}.html',restrict_css="section#primary a"),callback='parse_item'),
    )
    def parse_item(self, response):
        item = NewsItem()
        sel = Selector(text=response.text)
        try:
            title = sel.xpath("//h1[@class='entry-title']/text()").extract()
            if title == []:
                raise Exception('title is none')
            else:
                item['title'] = title[0]
        except:
            print('title不能为空')
        try:
            atime = sel.xpath("//a/time[@class='entry-date']/text()").extract()
            if atime == []:
                raise Exception('atime is none')
            else:
                item['atime'] = atime[0]
        except:
            print('时间不能为空')
        contents = sel.xpath("//div[@class='entry-content']/p/text()").extract()
        content = ','.join(contents)
        infos = sel.xpath("//div[@class='entry-content']/p/text()").extract()[-1]
        if '作者' in infos:
            author = re.findall('作者：(.*)',infos,re.S)[0]
            # source = '空'
            item['author'] = author
        else:
            source = infos
            # author = '空'
            print(source)
        tupian = sel.xpath("//div[@class='entry-content']/p/img/@src").extract()
        tupian_url = ','.join(tupian)
        article_link = response.url
        keywords = sel.xpath("//meta[@name='keywords']/@content").extract()[0]
        synopsis = sel.xpath("//meta[@name='description']/@content").extract()[0]
        # item['atime'] = atime
        item['content'] = content
        item['synopsis'] = synopsis

        item['tupian_url'] = tupian_url
        item['keywords'] = keywords
        item['article_link'] = article_link
        yield item



