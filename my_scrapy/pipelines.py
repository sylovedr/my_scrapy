# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyScrapyPipeline:
    def __init__(self):
        # 链接数据库，端口号默认为3306
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='mysql', db='doubandb',charset='utf8')
        # 建立游标对象
        self.cursor = self.conn.cursor()
        self.cursor.execute('truncate table movie')
        self.conn.commit()


    def process_item(self, item, spider):
        try:
            self.cursor.execute("insert into movie(name,movieInfo,star,number,quote) \
                        values (%s,%s,%s,%s,%s)", (item['name'], item['movieInfo'], item['star'],
                                                   item['number'], item['quote']))
            self.conn.commit()
        except pymysql.Error:
            print("Error：%s,%s,%s,%s,%s" % (item['name'], item['movieInfo'], item['star'],item['number'], item['quote']))
        return item


