# -*- coding: utf-8 -*-
import io
import scrapy
from scrapy_redis.spiders import RedisSpider
from doubannovel.items import DoubannovelItem

class DoubanNovelSpider(RedisSpider):
    name = "douban_backup"
    redis_key = "douban:start_urls"

    def parse(self, response):
        lists = response.xpath('//li[@class="subject-item"]')
        
        items = DoubannovelItem()
        f = io.open('test.json', 'a+', encoding='utf8')
        for li in lists:
                items['name'] = ''.join(li.xpath('.//div[@class="info"]/h2/a/text()').extract_first().split())
                items['pub'] = ''.join(li.xpath('.//div[@class="pub"]/text()').extract_first().split())
                items['rating'] = ''.join(li.xpath('.//span[@class="rating_nums"]/text()').extract_first().split())
                items['people'] = ''.join(li.xpath('.//span[@class="pl"]/text()').extract_first().split())
        f.write(items['name'])
        f.close()
