# -*- encoding:utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Spider
import scrapy
from scrapy.selector import Selector
import json
#js解密
import execjs
import re
import execjs


class Qixin(Spider):
    a = []
    name = 'qixin'
    allowed_domins = []
    start_urls = ['https://xin.baidu.com/']

    def parse(self, response):
        a = input('请输入您要查找的内容:')
        url = 'https://xin.baidu.com/s/l?q='+a+'&t=0&p=1&s=10'#p是分页的
        yield scrapy.Request(url=url,callback=self.parse_item)

    def parse_item(self,response):
        # datas = json.loads(response.text)
        # infos = datas['data']['html']
        js_raw = response.text
        data = execjs.eval(js_raw)
        # print(data)
        # bid = datas['data']['bdCode']
        # print(bid)
        title = re.findall('<span class="zx-ent-address-text" title="(.*?)">',str(data),re.S)
        href = re.findall('href="(.*?)" title',str(data),re.S)
        ids = set(href)
        for id in ids:
            url = 'https://xin.baidu.com' + id
            yield scrapy.Request(url=url,callback=self.parse_xiangxi,meta={'id':id})

    def parse_xiangxi(self,response):
        ids = response.meta['id']
        bid = re.findall('百度信用代码：</em><span id="baiducode">(.*?)</span></div>',response.text,re.S)[0]
        j = re.findall("getAttribute\('(.*?)'\);var baiducode = document.getElementById\('baiducode'\)",response.text,re.S)[0]
        tk = re.findall(str(j)+'="(.*?)">',response.text,re.S)[0]
        #https://xin.baidu.com/detail/basicAjax?pid=xlTM-TogKuTwkFGmJVDV*CNPO8GvCHGNVgmd&tot=xlTM-TogKuTwMqpyapzPTPrbdKdpp-IKqAmd
        funs = re.findall("</script><script>(.*?)\(function",response.text, re.S)[-1]
        # js = "'''"+ funs +"'''"
        ctx = execjs.compile(funs)
        tot = ctx.call('mix',tk,bid)

        pid = re.findall("pid=(.*)",ids,re.S)[0]
        # print(pid)
        url = 'https://xin.baidu.com/detail/basicAjax?pid=' + pid + '&' + 'tot=' + tot
        yield scrapy.Request(url=url,callback=self.parse_jiekou)

    def parse_jiekou(self,response):
        # s = response.url
        a = execjs.eval(response.text)
        print(a)

# (function(){var tk = document.getElementById('teYJHdo9').getAttribute('a8XP5');var baiducode = document.getElementById('baiducode').innerText;window.tk = mix(tk, baiducode);})()












'''
function mix(tk, bid)
        {
            var tkLen = tk.length;
            tk = tk.split('');
            var bdLen = bid.length;
            bid = bid.split('');
            for (var i = 0; i < bdLen; i++){
            bid[i] = parseInt(bid[i]) + parseInt(tkLen - bdLen);
            }
            var one = tk[bid[bdLen - 1]]; 
            for (var i = bdLen - 1; i >= 0; i -= 1) {
                tk[bid[i]] = tk[bid[i - 1]]; 
                if ((i - 2) < 0) 
            {
            tk[bid[i - 1]] = one;
                break;}}

        return tk.join("");}
        (
        function(){
            var tk = document.getElementById('t1sWfY').getAttribute('a743PKd');
            var baiducode = document.getElementById('baiducode').innerText;
            window.tk = mix(tk, baiducode)
'''





