import urllib.request

url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器访问
# response=urllib.request.urlopen(request)
proxies = {
    'htttp': '127.0.0.1:10809'
}
# handler  build_opener open
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

# 获取响应数据

content = response.read().decode('utf-8')

# 保存数据
with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
