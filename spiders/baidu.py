from newspaper import Article
3from scrapy.spiders import Spider
from scrapy.selector import Selector
import scrapy
from ..items import NewsItem
from dateparser import parser

class Baidu(scrapy.Spider):
    q = 0
    name = 'baidu'
    allowed_domins = []
    start_urls = ['https://www.baidu.com/']
    headers = {
        "Referer": "https://www.baidu.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.10 Safari/537.36"
    }
    def parse(self, response):
        # print(response.url)
        w = 0
        a = input('请输入您想要查找的内容:')
        for w in range(0,100,10):
            url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word='+a+'&pn='+str(w)
            yield scrapy.Request(url=url, callback=self.parse_item)


    def parse_item(self,response):

        all_links = response.xpath("//div/h3/a/@href").extract()
        for link in all_links:
            item = NewsItem()
            # print(link)
            url = link
            item['article_link'] = link
            news = Article(url, language='zh')
            news.download()
            news.parse()
            title = news.title
            content = news.text
            tupian_url = news.images
            item['title'] = title
            item['content'] = content
            # item['tupian_url'] = tupian_url
            for a in tupian_url:
                item['tupian_url'] = a
            # print(title)
            yield scrapy.Request(url=url,callback=self.parse_xiangxi,meta={'item':item},headers=self.headers)

    def parse_xiangxi(self,response):
        item = response.meta['item']
        sel = Selector(response)
        keywords = sel.xpath('//meta[@name="keywords"]/@content').extract_first()
        synopsis = sel.xpath("//meta[@name='description']/@content").extract_first()
        author = sel.xpath("//span[@class='editor']/text()").extract_first()
        if author == None:
            author = sel.xpath("//div[@id='article']//p[@class='author-name']/text()").extract_first()
        source = sel.xpath("//div[@id='article']//span[@class='source']/text()").extract_first()
        if source == None:
            source = sel.xpath("//span[@id='source_baidu']/a/text()").extract_first()
        atime = sel.xpath("//span[@id='pubtime_baidu']/text()").extract_first()
        if atime == None:
            atime = sel.xpath("string(//div[@id='article']//div[@class='article-source'])").extract_first()[3:]
        item['author'] = author
        item['keywords'] = keywords
        item['synopsis'] = synopsis
        item['source'] = source
        item['atime'] = atime
        yield item



#https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=%E6%B1%BD%E8%BD%A6&x_bfe_rqs=03E80&x_bfe_tjscore=0.147536&tngroupname=organic_news&pn=20




