# -*- encoding:utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
import scrapy
import json
import io,sys
from ..items import NewsItem
from newspaper import Article
import urllib.request
from readability.readability import Document

class Kerrrrr(Spider):
    name = 'kerrrrr'
    allowed_domins = []
    start_urls = [
        'https://36kr.com/'
    ]

    def parse(self, response):
        a = input('请输入您想要查找的内容：')
        url = 'https://36kr.com/api//search/entity-search?page=1&per_page=40&keyword='+a+'&entity_type=post&sort=date'
        yield scrapy.Request(url=url,callback=self.parse_item)

    def parse_item(self,response):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
        # sel = Selector(response)
        datas = json.loads(response.text)
        all_title = datas['data']['items']
        for titles in all_title:
            item = NewsItem()
            id = titles['id']
            item['title'] = titles['title']
            item['tupian_url'] = titles['cover']
            item['author'] = titles['user_name']
            item['atime'] = titles['published_at']
            # content1 = ','.join(titles['highlight']['content'])
            # content2 = ','.join(titles['highlight']['content_light'])
            # content = content1+content2
            # item['content'] = content.strip('<em>').strip('</em>')
            # print(item['content'])
            url = 'https://36kr.com/p/'+str(id)+'.html'
            yield scrapy.Request(url=url,callback=self.parse_xiangxi,meta={'item':item})

    def parse_xiangxi(self,response):
        item = response.meta['item']
        sel = Selector(response)
        # print(response.url)
        article_link = response.url
        # news = Article(url=response.url,language = 'zh')
        # news.download()
        # news.parse()
        # content = news.text
        html = urllib.request.urlopen(response.url).read()
        content = Document(html).summary()
        keywords = sel.xpath("//meta[@name='keywords']/@content").extract()[0]
        synopsis = sel.xpath("//meta[@name='description']/@content").extract()[0]
        source = sel.xpath("//section[@class='article-footer-label']/div[1]/div/div[1]/text()").extract_first()
        print(content)











