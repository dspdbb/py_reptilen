import urllib.request
import urllib.parse
# 请求对象定制
def create_request():
    base_url ='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data={
        'cname': '北京',
        'pid':'',
        'pageIndex': page,
       'pageSize': '10',
    }
    data=urllib.parse.urlencode(data).encode('utf-8')
    headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=base_url,data=data,headers=headers)
    return  request
def get_content(request):
    response=urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content
def down_load(page,content):
    with open('KFC'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)
if __name__ == '__main__':
    start_page=int(input('起始页码'))
    end_page=int(input('结束页码'))
    for page in range(start_page, end_page+1):
        # 请求对象定制
        request = create_request()
        # 获取网页源码
        content =get_content(request)
        # 下载
        down_load(page,content)
