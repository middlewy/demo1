# -* encoding:utf-8 *-
from scrapy.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from ..items import NewsItem
import datetime
import time

class Wangyi(CrawlSpider):
    name = 'wangyi'
    allowed_domins = []
    start_urls = ['http://tech.163.com/gd/',]
    datetime = str(datetime.datetime.now())
    # t = time.strptime(datetime,("%Y-%m-%d"))
    # st = time.strftime(('%y%m%d'),t)
    st = datetime[:10]
    dt = st.replace('-','/').rstrip('/')
    # print(dt)
    rules = (
        #http://tech.163.com/special/gd2016_02/
        Rule(LinkExtractor(allow='http://tech.163.com/special/gd2016_\d{2}/'),follow=True),
        #http://tech.163.com/18/1129/11/E1PCO71O00097U81.html
        #http://tech.163.com/18/1129/11/E1PCCEIA00097U7R.html
        #http://tech.163.com/18/1128/20/E1NPNS7N00097U7R.html
        Rule(LinkExtractor(allow='http://tech.163.com/\d{2}/\d{4}/\d{2}/\w{16}.html',restrict_css="div.left a"),callback="parse_item")
    )
    def parse_item(self, response):
        item = NewsItem()
        sel = Selector(response)
        try:
            title = sel.xpath("//h1/text()").extract()
            if title == []:
                raise Exception('title is none')
            else:
                item['title'] = title[0]
        except:
            print('title不能为空')

        # atime = sel.xpath("//div[@class='post_time_source']/text()").extract()[0].strip()[:-4]
        try:
            atime = sel.xpath("//div[@class='post_time_source']/text()").extract()
            if atime == []:
                raise Exception('time is none')
            else:
                item['atime'] = atime[0].strip()[:-4]
        except:
            print('time不能为空')

        contents = sel.xpath("//div[@id='endText']/p/text()").extract()
        content = ''
        for a in contents:
            content += a.strip()
        # print(content)
        source = sel.xpath("//span[@class='left']/text()").extract_first()
        author = sel.xpath("//span[@class='ep-editor']/text()").extract_first()
        tupian_url = sel.xpath("//p[@class='f_center']/img/@src").extract_first()
        keywords = sel.xpath("//meta[@name='keywords']/@content").extract_first()
        synopsis = sel.xpath("//meta[@name='description']/@content").extract_first()
        article_link = response.url
        item['source'] = source
        item['content'] = content
        item['synopsis'] = synopsis
        item['author'] = author
        item['tupian_url'] = tupian_url
        item['keywords'] = keywords
        item['article_link'] = article_link
        yield item





