# News-crawler-data-processing

项目需要处理爬虫爬取的新闻网站数据，于是有了本项目。

## 文件说明

`nefu_news.xlsx`: 新闻爬取结果，手动在首列添加了id列名

`cluster_id.txt`: 聚类结果，每个数组代表一个聚类

`nefu_news_removal.xlsx`: 去重后的新闻数据，未添加`type`列

`add_type_nefu_news.xlsx`: 添加`type`列后的新闻数据

`requirements.txt`: 环境配置文件，有许多多余的包，只要有pandas和xlrd就能运行了（大概）



## 代码功能

`duplicate_removal.py`: 去重新闻数据（由于新闻网站迷之代码，每页都有隐藏的上页的新闻）

`add_type_column.py`: 将聚类结果添加至`type`列

`clear_database.py`: 清除Django框架中的sqlite数据，以备更新数据用

`excel_to_database.py`:  将`add_type_nefu_news.xlsx`中的数据添加至数据表中



## 运行顺序

`duplicate_removal.py`  => `add_type_column.py` => `clear_database.py` => `excel_to_database.py`