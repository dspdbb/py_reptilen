# 1）获取网页源码
# 2）解析    解析服务器响应文件   etree。HTML
# 3）打印出来
import urllib.request
from lxml import etree
url = 'https://www.baidu.com/'
headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器访问服务器
response = urllib.request.urlopen(request)

# 获取网页源码
content = response.read().decode('utf-8')

# 解析网页源码，获取想要数据


# 解析服务器响应文件
tree = etree.HTML(content)
# 获取想要数据
result = tree.xpath('//input[@id="su"]/@value')
print(result)
