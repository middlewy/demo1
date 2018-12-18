from scrapy.spiders import Spider
import scrapy
import json
import io,sys

class Lol(Spider):
    name = 'lol'
    allowed_domins = []
    start_urls = ['http://gpcd.gtimg.cn/mobile/mlol/lol_expression/30s/expressionpackage_list.js']

    def parse(self, response):
        datas = json.loads(response.text)
        infos = datas['expressionpackage_list']
        for info in infos:
            title = info['name']
            atime = info['upload_time']
            synopsis = info['description']
            tupian_url = info['logo_url']
            # print(title,atime,synopsis,tupian_url)
        url = 'http://lol.qq.com/m/act/a20150319lolapp/exp_3.htm?iVideoId=18488&e_code=lolapp.videolist.18488'
        yield scrapy.Request(url=url,callback=self.parse_xiangxi)

    def parse_xiangxi(self,response):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
        print(response.text)
