import urllib.request

# url='https://blog.csdn.net/qq_41684621/article/details/113851644'
url='https://www.goudan.com/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
try:
    request=urllib.request.Request(url=url,headers=headers)
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    print(content)
except urllib.error.HTTPError:
    print('系统正在升级')
except urllib.error.URLError:
    print('系统正在维护')