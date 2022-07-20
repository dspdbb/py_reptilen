import urllib.request
import urllib.parse
import json

# get请求，获取豆瓣电影第一页数据，并保存
url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=0&limit=20'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

# 请求对象的定制
request=urllib.request.Request(url=url,headers=headers)

# 获取响应数据
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')

# 下载数据到本地
# open()方法默认情况下使用的是gbk的编码，如果我们需要保存汉字，则指定编码格式为utf-8
# encoding='utf-8'
fp=open('douban.json','w',encoding='utf-8',)
fp.write(content)
