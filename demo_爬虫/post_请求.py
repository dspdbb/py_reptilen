import urllib.request
import urllib.parse
import json
url='https://fanyi.baidu.com/sug'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
data={
   'kw':'早上'
}
# post请求必须要进行编码
data=urllib.parse.urlencode(data).encode('utf-8')
# post请求参数是不会拼接在url后面的  而是放在请求对象定制的参数中
# post请求必须要进行编码
request=urllib.request.Request(url=url,data=data,headers=headers)
# 模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)
# 获取响应数据
content=response.read().decode("utf-8")
print(content)
# post请求必须要进行编码 data=urllib.parse.urlencode(data)
# 编码之后 必须调用encode方法 data=urllib.parse.urlencode(data).encode('utf-8')
# 参数是放在请求对象定制的方法中 request=urllib.request.Request(url=url,data=data,headers=headers)
# 字符串--》json对象

obj = json.loads(content)
print(obj)