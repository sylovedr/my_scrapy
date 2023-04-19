# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 电影名
    movieInfo = scrapy.Field()  # 电影简介
    star = scrapy.Field()  # 评分
    number = scrapy.Field()  # 评价人数
    quote = scrapy.Field()  # 简评

