
import urllib.request
import random
proxies_pool=[
    {'htttp': '47.56.69.11:8000'},
    { 'htttp':'202.55.5.209:8090'}
]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
proxies =random.choice(proxies_pool)
url ='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=ip'
request = urllib.request.Request(url=url,headers=headers)
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')
with open('dailic.html','w',encoding='utf-8') as fp:
    fp.write(content)