# -*- encoding:utf8 -*-

import scrapy
import time
import json
from scrapy.spiders import Spider
import re

class Yangshi(scrapy.Spider):
    name = 'toutiao'
    allowed_domins = []
    start_urls = []

    def start_requests(self):
        a = time.time()
        t = str(a)[:10]
        url = 'http://ib.snssdk.com/api/news/feed/v88/?ac=WIFI&device_id=40440128266&aid=13&os_version=12.1&app_name=news_article&channel=App%20Store&idfa=620FDC9C-4FBC-4C6E-BFA0-FEB36A453259&device_platform=iphone&tma_jssdk_version=1.5.0.0&vid=D9C3A6C6-6A0F-4717-87B9-297D6A9F8425&openudid=fdb49758a6f6edfb3f40fb5360dab3494dc46a67&device_type=iPhone%206S%20Plus&ab_feature=z1&idfv=D9C3A6C6-6A0F-4717-87B9-297D6A9F8425&ssmix=a&version_code=6.9.8&resolution=1242*2208&ab_client=a1,f2,f7,e1&update_version_code=69836&detail=1&last_refresh_sub_entrance_interval=1544614778&tt_from=load_more&count=20&list_count=21&LBS_status=authroize&loc_mode=1&cp=5eC9120cF337Bq1&max_behot_time=1544612782&image=1&strict=0&refer=1&language=zh-Hans-CN&concern_id=6286225228934679042&st_time=3035&as=a2252fa17a877c03805471&ts='+t
        yield scrapy.Request(url=url,callback=self.parse_item)

    def parse_item(self, response):
        datas = json.loads(response.text)
        data = datas['data']
        for infos in data:
            info = json.loads(infos['content'].encode('utf-8').decode('utf-8'))
            try:
                title = info['title']
                # print(title)
            except Exception as e:
                print(e)
            content = info['abstract']
            url = info['share_url']
            print(url)




















