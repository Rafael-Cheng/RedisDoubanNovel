# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy.DoubanNovelSpider.items import DoubanNovelItem

class DoubanNovelSpider(RedisSpider):
    name = "douban"
    redis_key = "douban:start_urls"

    def parse(self, response):
        lists = response.xpath('//li[@class="subject-item"]')
        
        for li in lists:
            item = DoubanNovelItem()
            item['name'] = ''.join(li.xpath('.//div[@class="info"]/h2/a/text()').extract_first().split())
            item['pub'] = ''.join(li.xpath('.//div[@class="pub"]/text()').extract_first().split())
            item['rating'] = ''.join(li.xpath('.//span[@class="rating_nums"]/text()').extract_first().split())
            item['people'] = ''.join(li.xpath('.//span[@class="pl"]/text()').extract_first().split())
            yield item
