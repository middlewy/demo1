#  -*- encoding:utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from ..items import NewsItem
from newspaper import Article
from readability import Document
from jieba import analyse
import urllib
from urllib import request
import scrapy
import time
import os

class Baidu(Spider):
    name = 'baiduzixun'
    allowed_domins = []
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        a = input('请输入您要查找的内容:')

        url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word='+a
        yield scrapy.Request(url=url,callback=self.parse_item)



    def parse_item(self,response):
        sel = Selector(response)
        item = NewsItem()
        all_divs = response.xpath("//div[@id='content_left']/div[3]/div")
        for div in all_divs:
            try:
                title = div.xpath("./h3[@class='c-title']/a/text()").extract()
                if title == []:
                    raise Exception('title is none')
                else:
                    item['title'] = title[0].strip()
                    print(item['title'])
            except:
                print('title不能为空')
            all_time = div.xpath("./div[@class='c-summary c-row ']/p[@class='c-author']/text()").extract()
            atime = ','.join(all_time).replace(u'\xa0',u'')
            # print(atime)
            num = atime.find('20')
            btime = atime[num:].strip()
            # print(btime)
            # t = time.strptime(btime,"%Y年%m月%d日 %H:%M")
            # nowtime = time.strftime("%Y-%m-%d %H:%M:%S",t)
            # item['atime'] = nowtime


        all_info = sel.xpath("//h3[@class='c-title']/a/@href").extract()
        for link in all_info:
            url = link
            # print(url)
            yield scrapy.Request(url=url,callback=self.parse_xiangxi)
        pagea = response.xpath("//strong/span[@class='pc']/text()").extract()[0]
        print(type(pagea))
        if pagea == '1':
            next_page = response.xpath("//a[@class='n'][1]/@href").extract()
            if next_page:
                aurl = 'https://www.baidu.com' + next_page
                yield scrapy.Request(url=aurl, callback=self.parse_item)
            else:
                print('进入第一个else')
        else:
            if pagea == '5':
                return
            next_page = response.xpath("//a[@class='n'][2]/@href").extract()[0]
            if next_page:
                burl = 'https://www.baidu.com' + next_page
                yield scrapy.Request(url=burl, callback=self.parse_item)
            else:
                print('2')


    def parse_xiangxi(self,response):
        sel = Selector(response)
        # print(response.url)
        item = NewsItem()
        if not os.path.exists('图片'):
            os.mkdir('图片')
        try:
            title = sel.xpath("//div[@class='article-title']/h2/text()").extract()
            if len(title) == 0:
                raise Exception('title is none')
            else:
                item['title'] = title[0]
                # print(title)
        except:
            print('title 不能为空')
        try:
            atime = sel.xpath("string(//div[@class='article-desc clearfix']/div/div[@class='article-source'])").extract()
            if len(atime) == 0:
                raise Exception('time is none')
            else:
                item['atime'] = atime[0][3:]
                # print(item['atime'])
        except:
            print('时间不能为空')


        source = sel.xpath("string(//div[@class='article-desc clearfix']/div/div[@class='article-source'])").extract()
        if source == []:
            source = '无'
        else:
            source = sel.xpath("string(//div[@class='article-desc clearfix']/div/div[@class='article-source'])").extract()[0][:4]
        item['source'] = source
        html = urllib.request.urlopen(response.url).read()
        article = Document(html).summary()
        sec = Selector(text=article)
        art = ','.join(sec.css("div.article-content p::text").extract())
        # 第一种关键词的算法
        tfidf = analyse.extract_tags
        keywords = tfidf(art)
        # print(keywords)
        #第二种关键词的算法
        # tfidf = analyse.default_textrank
        # keywords = tfidf(art)
        # for keyword in keywords:
        #     print(keyword)
        # content = sel.xpath("//div[@class='article-content']/p/text()").extract()
        # if content == []:
        #     content = ','.join(sel.xpath("string(//div[@class='article-content']/p)").extract())
        # else:
        #     content = ','.join(content)
        # item['content'] = content
        tupian_urls = sel.xpath("//div[@class='img-container']/img[@class='large']/@src").extract()
        if tupian_urls == []:
            tupian_url = '无'
        else:
            # for tupian_url in tupian_urls:
                # tupian_url = tupian_urls[0]
            tupian_url = ','.join(tupian_urls)
        item['tupian_url'] = tupian_url

        item['tupian_bendi'] = '图片/'+tupian_url[-6:]




















