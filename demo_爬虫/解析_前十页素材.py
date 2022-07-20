# 1.请求对象定制
# 2.获取网页源码
# 3.下载

# 需求  下载前十页图片
import urllib.request

# 解析导包
from lxml import etree

url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'


def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_' + str(page) + '.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    tree = etree.HTML(content)
    # 创建列表存储图片地址和图片名称
    name_list = tree.xpath("//div[@id='container']//a/img/@alt")
    src_list = tree.xpath("//div[@id='container']//a/img/@src")
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src
        urllib.request.urlretrieve(url=url, filename='./love/' + name + '.jpg')


if __name__ == '__main__':
    start_page = int(input('起始页码'))
    end_page = int(input('结束页码'))
    for page in range(start_page, end_page + 1):
        # 请求对象定制
        request = create_request(page)
        # 获取网页源码
        content = get_content(request)
        # 下载
        down_load(content)
