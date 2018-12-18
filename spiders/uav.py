#-* coding:utf-8 -*--

from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from ..items import NewsItem
import datetime
import logging
import os
import re

class Uav(CrawlSpider):
    name = 'uav'
    allowed_domins = []
    start_urls = [
    # 'http://www.81uav.cn/uav-news/45.html',
                  'http://www.81uav.cn/uav-news/4.html',
                  ]
    #http://www.81uav.cn/uav-news/201811/23/45656.html
    rules = (
        Rule(LinkExtractor(allow="http://www.81uav.cn/uav-news/\d{6}/\d{2}/\d+.html",restrict_css = "div.news_left a"),callback="parse_item"),
    )
    def parse_item(self, response):
        item = NewsItem()
        # print(response.url)
        article_link = response.url
        sel = Selector(response)
        t = datetime.datetime.now()
        try:
            title = sel.xpath("//h1/text()").extract()
            if len(title) == 0:
                raise Exception('title is none')
            else:
                title = title[0]
                item['title'] = title
        except Exception as e:
            logging.exception(e)


        infos = sel.xpath("//div[@class='view']/div[@class='info']/text()").extract()[3].replace(u'\xa0',u'').strip()
        atime = re.findall("发布日期：(.*?)来源",infos,re.S)[0]
        author = re.findall("作者：(.*)",infos,re.S)
        if author == []:
            author = '作者无'
        else:
            author = author[0]

        source = re.findall("来源：(.*)",infos,re.S)[0]
        if '作者' in source:
            a = source.find('作者')
            source = source[0:a]
        # print(source)
        tupian_href = sel.xpath("//div[@id='article']/p/img/@src").extract()
        if len(tupian_href) == 0:
            tupian_url = '无图片'
            # print(response.url)
        else:
            tupian_url = ','.join(tupian_href)
        keywords = sel.xpath("//meta[@name='keywords']/@content").extract()[0]
        synopsis = sel.xpath("//meta[@name='description']/@content").extract()[0]
        contents = sel.xpath("//p/text()").extract()
        content = ','.join(contents)
        print(content.replace(u'\u2003',u'').replace(u'\xa0',u''))
        item['atime'] = atime
        item['content'] = content
        item['synopsis'] = synopsis
        item['author'] = author
        item['tupian_url'] = tupian_url
        item['keywords'] = keywords
        item['article_link'] = article_link
        yield item




