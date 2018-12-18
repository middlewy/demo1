#  -*- encoding:utf-8 -*-

import scrapy
from scrapy.spiders import Spider
import json
import re

class Xiecheng(scrapy.Spider):
    name = 'xiecheng'
    allowed_domins = []
    cookies = {
         'DUID': 'u=F2FEDC52D95C7570C49DCB17824690BFF71F3B9C37186641CF0E12A395AFFBFA&v=0', ' IsNonUser': 'F',
         ' _gat': '1', ' _RSG': '6Dagqe3_Io5auOfX1.BfVA', ' appFloatCnt': '2',
         ' ticket_ctrip': 'uoeOwviAJ6VQEgTNwLuTqSV9j/bS+aOP3Riia1P+kyQbgkQZsD2giZwDQz/2a8dt37GfCPF9RTX/sD+JPK5szT1CZ0It/CkNGbqgD4HIRsKf+o2hzn0OHG5oapH3/PBXijzm21ORTUhlTzl5w4niUK9xNGtzi4TQhWiYgpmeQPva4fabKQeJJ9hX/BHVk5IotW7S/XUDuJd3DVovAZ1ftEVc3FS1ApGRKR0uiFLdVeQQzgmfGS1TD8H7Yn/SsDLtST99CUxG4TXZeQrQM8ZmlsFNNd2BJTaSLG1hAtSVePBQ+QbFW2mTzG2EptqTUqIe',
         ' __zpspc': '9.3.1544702014.1544702039.3%232%7Cwww.baidu.com%7C%7C%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23',
         ' _abtest_userid': '52c6c146-fd9a-4428-9cac-602c07998652', ' manualclose': '1',
         ' Union': 'OUID=pinP&AllianceID=4897&SID=155950&SourceID=&Expires=1545306814918', ' _RF1': '125.33.192.69',
         ' _bfa': '1.1544699024736.3eceq7.1.1544699024736.1544699024736.1.13',
         ' _RDG': '2833d249efc06f29633795cf5778424003',
         ' ASP.NET_SessionSvc': 'MTAuMTUuMTI4LjMwfDkwOTB8b3V5YW5nfGRlZmF1bHR8MTU0MzgzNDAxMDc3Nw',
         'searchlist': 'searchlisttop=400', ' _gid': 'GA1.2.1389059067.1544699027',
         ' Session': 'SmartLinkCode=U155950&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh',
         ' AHeadUserInfo': 'VipGrade=10&UserName=&NoReadMessageCount=0&U=02603999AECE1D8A33E3644E0490AF87',
         ' _bfs': '1.13', ' cticket': '34A492A8B1A8B0377A56ED64D1585746F8FB06F67D3D2A36E08886CE436D2DA2',
         ' gad_city': '96617ee7af8aedd02bbece8583e0066e', ' _RGUID': '5c92fc3a-34aa-4346-a7e9-2fe061a58e24',
         ' _bfi': 'p1%3D108002%26p2%3D108001%26v1%3D12%26v2%3D11', ' MKT_Pagesource': 'PC',
         ' MKT_OrderClick': 'ASID=4897155950&CT=1544702039091&CURL=http%3A%2F%2Ftrains.ctrip.com%2FTrainBooking%2FSearch.aspx%3Ffrom%3Dbeijing%26to%3Dshanghai%26day%3D2018-12-15%26number%3D%26fromCn%3D%25u5317%25u4EAC%26toCn%3D%25u4E0A%25u6D77&VAL={"pc_vid":"1544699024736.3eceq7"}',
         ' _ga': 'GA1.2.1096021755.1544699027',
         ' Mkt_UnionRecord': '%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1544702039093%7D%5D',
         ' _jzqco': '%7C%7C%7C%7C1544699034607%7C1.1524848674.1544699027490.1544699637798.1544702014936.1544699637798.1544702014936.0.0.0.4.4'
    }

    formdata = {
        'value':{'DepartureCityName': '北京', 'ArrivalDate': '', 'IsDongChe': False, 'IsBus': False, 'Filter': '0', 'HubCity': '', 'CatalogName': '', 'DepartureDateReturn': '2018-12-17', 'Catalog': '', 'DepartureCity': 'beijing', 'ArrivalCityName': '上海', 'DepartureDate': '2018-12-15', 'ArrivalCity': 'shanghai', 'IsGaoTie': False, 'TrainNumber': ''}
    }
    start_urls = []

    def start_requests(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.10 Safari/537.36"
        }
        url = 'http://hotels.ctrip.com/hotel/shanghai2'
        # yield scrapy.FormRequest(url=url,callback=self.parse_item,formdata=self.formdata,headers=headers)
        yield scrapy.Request(url=url,callback=self.parse_item,cookies=self.cookies,headers=headers)
    def parse_item(self, response):
        # a = response.text
        # print(a.encode('gbk').decode('utf-8'))
        # all_div = response.xpath("//div[@id='hotel_list']/div")
        # for div in all_div:
        #     hotel_name = div.xpath("./ul[@class='hotel_item']/li[@class='hotel_item_name']/h2[@class='hotel_name']/a/text()").extract()
        #     print(hotel_name)
        # datas = json.loads(response.text)
        # infos = datas['advertisingqualityhotels']
        # for info in infos:
        #     hotel = info['hotelname']
        #     hotel_id = info['hotelid']
        #     print(hotel_id)
        #     url = 'view-source:http://hotels.ctrip.com/hotel/'+hotel_id+'.html?isFull=F'

        # all = re.findall(r'hotelPositionJSON:  (.*?)\]', response.text, re.S)[0] + ']'
        datas = re.findall("htllist: \'\[(.*?)\]\'",response.text,re.S)
        data = str(datas)[1:-1]
        info = re.findall('"hotelid":"(.*?)",',data,re.S)
        for id in info:
            url = 'http://hotels.ctrip.com/hotel/'+id+'.html'
            yield scrapy.Request(url=url,callback=self.parse_xiangxi)

    def parse_xiangxi(self, response):
        title = response.xpath("//h2[@class='cn_n']/text()").extract()
        pingfen = response.xpath("//p[@class='s_row']/span[@class='score']/text()").extract()
        print(pingfen)

















