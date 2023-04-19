import json

import scrapy
import time
from scrapy import Request,Selector
from my_scrapy.items import MyScrapyItem

class Top250Spider(scrapy.Spider):
    name = "top250"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["http://movie.douban.com/"]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    url = 'https://movie.douban.com/top250'


    def start_requests(self):
        yield Request(self.url,headers=self.headers,callback=self.parse)


    def parse(self, response):
        item = MyScrapyItem()
        selector = Selector(response)
        movies = selector.xpath('//div[@class="info"]')
        for movie in movies:
            name = movie.xpath('div[@class="hd"]/a/span/text()').extract()
            message = movie.xpath('div[@class="bd"]/p/text()').extract()
            star = movie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            number = movie.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()

            quote = movie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            if quote:
                quote = quote[0]
            else:
                quote = ''

            item['name'] = ''.join(name)
            item['movieInfo'] = ';'.join(message).replace(' ', '').replace('\n', '')
            item['star'] = star[0]
            item['number'] = number[1].split('人')[0]
            item['quote'] = quote
            yield item

        # 下一页的url
        nextpage = selector.xpath('//span[@class="next"]/link/@href').extract()
        time.sleep(3)  # 休眠3秒，防止被检测到机器操作
        if nextpage:
            nextpage = nextpage[0]
            yield Request(self.url + str(nextpage), headers=self.headers, callback=self.parse)
