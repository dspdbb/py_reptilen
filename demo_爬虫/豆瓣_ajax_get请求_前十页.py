import urllib.request
import urllib.parse
import json


# 请求对象定制
def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data = {
        'start': (page - 1) * 20,
        'limit': 20,
    }
    data = urllib.parse.urlencode(data)
    url = base_url + str(data)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie': 'bid=hfoJNfIsroU; __gads=ID=9c81b1945f74a4fd-22a8cd8fc5d0002f:T=1646106440:RT=1646106440:S=ALNI_MYbbn4yRuGKz1SpL8GMGr6H1sYWyA; ll="108304"; _vwo_uuid_v2=DEE5C62ECEA9326D9944BBA1FCB900820|25149f570ad4cb9051da3d390df681ca; __utma=30149280.1293293853.1646106443.1657779472.1657844739.4; __utmc=30149280; __utmz=30149280.1657844739.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1657844739; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1657844741%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.557817394.1657762880.1657779475.1657844741.3; __utmb=223695111.0.10.1657844741; __utmc=223695111; __utmz=223695111.1657844741.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; _pk_id.100001.4cf6=92d5efc8ea543026.1657762880.3.1657844746.1657779605.'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(page, content):
    with open('douban_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


# 程序入口
if __name__ == '__main__':
    start_page = int(input("输入起始页"))
    end_page = int(input('输入结束页'))

    for page in range(start_page, end_page + 1):
        # 每一页都有自己的请求对象定制
        request = create_request(page)
        # 获取响应数据
        get_content(request)
        content = get_content(request)
        # 下载
        down_load(page, content)


# import urllib.request
# import urllib.parse
#
#
# # 下载前10页数据
# # 下载的步骤：1.请求对象的定制  2.获取响应的数据 3.下载
#
# # 每执行一次返回一个request对象
# def create_request(page):
#     base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
#         'Cookie': 'bid=hfoJNfIsroU; __gads=ID=9c81b1945f74a4fd-22a8cd8fc5d0002f:T=1646106440:RT=1646106440:S=ALNI_MYbbn4yRuGKz1SpL8GMGr6H1sYWyA; ll="108304"; _vwo_uuid_v2=DEE5C62ECEA9326D9944BBA1FCB900820|25149f570ad4cb9051da3d390df681ca; __utma=30149280.1293293853.1646106443.1657779472.1657844739.4; __utmc=30149280; __utmz=30149280.1657844739.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1657844739; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1657844741%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.557817394.1657762880.1657779475.1657844741.3; __utmb=223695111.0.10.1657844741; __utmc=223695111; __utmz=223695111.1657844741.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; _pk_id.100001.4cf6=92d5efc8ea543026.1657762880.3.1657844746.1657779605.'
#     }
#     data = {
#         #  1 2  3  4
#         #  0 20 40 60
#         'start': (page - 1) * 20,
#         'limit': 20
#     }
#     # data编码
#     data = urllib.parse.urlencode(data)
#     url = base_url + str(data)
#     request = urllib.request.Request(url=url, headers=headers)
#     return request
#
#
# # 获取网页源码
# def get_content(request):
#     response = urllib.request.urlopen(request)
#     content = response.read().decode('utf‐8')
#     return content
#
#
# def down_load(page, content):
#     #    with open（文件的名字，模式，编码）as fp:
#     #        fp.write(内容)
#     with open('douban_' + str(page) + '.json', 'w', encoding='utf‐8') as fp:
#         fp.write(content)
#
#
# if __name__ == '__main__':
#     start_page = int(input('请输入起始页码'))
#     end_page = int(input('请输入结束页码'))
#     for page in range(start_page, end_page + 1):
#         request = create_request(page)
#         content = get_content(request)
#         down_load(page, content)
