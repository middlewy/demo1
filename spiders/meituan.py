from scrapy.spiders import Spider
import scrapy
import json
import io,sys

class Meituan(Spider):
    name = 'meituan'
    allowed_domins = []
    start_urls = ['']
