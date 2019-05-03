# -----------------------------------------------------------
# 将爬虫爬取的重复新闻去除
# -----------------------------------------------------------
import pandas as pd
# 读取新闻
news = pd.read_excel("nefu_news.xlsx")
news_df = pd.DataFrame(news)

news_id = news_df['id']
news_title = news_df['head']
news_scaned = []
news_add_id = []

# 过滤数据，将新闻id唯一性地储存
for i in range(0, len(news_title)):
    if news_title[i] not in news_scaned:
        # print("id = " + str(i) + " news add")
        news_add_id.append(i)
        news_scaned.append(news_title[i])

print("Removal complete, total news num is " + str(len(news_add_id)))

# 重排新闻id
news_df = news_df[news_df['id'].isin(news_add_id)]
new_id = []
for i in range(0, len(news_df['id'])):
    new_id.append(i)
news_df['id'] = new_id
print(news_df)

# 输出为xlsx文件
out_path = "nefu_news_removal.xlsx"
news_df.to_excel(out_path,index=False)