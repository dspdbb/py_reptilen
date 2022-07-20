import urllib.request
import urllib.parse
base_url='https://www.baidu.com/s'
data={
    'wd':'周杰伦',
    # 'sex':'男',
    # 'location':'中国台湾'
}
new_data=urllib.parse.urlencode(data)

#请求资源路径
url=base_url+new_data
# 反爬伪装
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
# 请求对象定制
request=urllib.request.Request(url=url,headers=headers)
# 模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)
# 获取网页源码的数据
content=response.read().decode("utf-8")
print(content)