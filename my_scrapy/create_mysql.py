def sql_table(hity):
    sql = f"""CREATE TABLE 安居客_{hity}_租房 (
         具体链接  varchar(200) ,
         房屋描述  varchar(200),
         房屋大小  varchar(200),
         租金  varchar(200))
         """
    db.create_table(sql)



import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='mysql', charset='utf8',db='scrapy')

cursor = db.cursor()

cursor.execute('CREATE DATABASE DOUBANDB')

sql = '''create table doubandb.Movie(
            id int not null primary key auto_increment comment '自增id',
            name varchar(1024) not null comment '电影名',
            movieInfo varchar(1024) default null comment '电影简介',
            star varchar(20) not null comment '评分',
            number varchar(1024) not null comment '评价人数',
            quote varchar(1024) not null comment '简评',
            createtime datetime default current_timestamp comment '添加时间'
)'''

cursor.execute(sql)

db.close()
