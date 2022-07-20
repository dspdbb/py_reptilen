import urllib.request
import urllib.parse
#请求网址
# E5%91%A8%E6%9D%B0%E4%BC%A6
url='https://www.baidu.com/s?wd='
#将周杰伦编程unicode编码
# 依赖于urllib.parse
name=urllib.parse.quote('周杰伦')
url=url+name
# 反爬第一伪装
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
# 请求对象定制
request=urllib.request.Request(url=url,headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取响应内容
content=response.read().decode("utf-8")
print(content)