# -*- coding: utf-8 -*-
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FeijiPipeline(object):
    def __init__(self):
        myconn = pymongo.MongoClient('127.0.0.1',27017)
        mydb = myconn['newsss']
        self.mycol = mydb['newsbaidu']
    def process_item(self, item, spider):
        self.mycol.insert(dict(item))
        return item
