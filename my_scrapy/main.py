#  execute 可以调用scrapy的执行脚本
from scrapy.cmdline import execute

import sys
import os
# os.path.abspath(__file__) 获取当前文件所在的路径
# os.path.dirname(os.path.abspath(__file__)) 获取当前文件所在的父目录

# 设置执行路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 设置执行命令
execute(["scrapy", "crawl", "top250"])
