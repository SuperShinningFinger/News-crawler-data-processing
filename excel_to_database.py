# -----------------------------------------------------------
# 将xlsx中的数据写入数据库
# -----------------------------------------------------------
import pandas as pd
import sqlite3
# 读取新闻
news = pd.read_excel("add_type_nefu_news.xlsx")
news_df = pd.DataFrame(news)

# Columns: [id, dept, head, text, time, type]
article_id = []
for i in news_df['id']:
    article_id.append(i)
# print(article_id)

author = []
for i in news_df['dept']:
    author.append(i)
# print(author)

title = []
for i in news_df['head']:
    title.append(i)
# print(title)

text = []
for i in news_df['text']:
    text.append(i)
# print(text)

date = []
for i in news_df['time']:
    date.append(i)
# print(date)

click = []
for i in news_df['id']:
    click.append(0)
# print(click)

type = []
for i in news_df['type']:
    type.append(i)
# print(type)

news_size = len(article_id)
# print(news_size)
# 链接数据库
conn = sqlite3.connect("news.sqlite")
c = conn.cursor()
for i in range(0, news_size):
    # print(i)
    c.execute("INSERT INTO Article_article VALUES (?,?,?,?,?,?,?)",
              (title[i], author[i], text[i], str(date[i]), type[i], click[i], article_id[i]))

conn.commit()
conn.close()
