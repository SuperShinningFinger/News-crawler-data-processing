# -----------------------------------------------------------
# 初始化数据库，清零自增表，清除用户使用记录，清除新闻信息
# -----------------------------------------------------------
import sqlite3

# 链接数据库
conn = sqlite3.connect("news.sqlite")
c = conn.cursor()

# 清空新闻表，将评分表自增列清零，将用户浏览记录、评分记录、推荐新闻清零
c.execute('delete from Article_article')
c.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'Article_score';")
c.execute("UPDATE Article_user set viewed = ''")
c.execute("UPDATE Article_user set recommend = ''")
c.execute("UPDATE Article_user set scored = ''")
# print(c.fetchall())
conn.commit()
conn.close()


