import urllib.request
import jsonpath
import json

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1658212745805_128&jsoncallback=jsonp129&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    # ':authority': ' dianying.taobao.com',
    # ':method': ' GET',
    # ':path': ' /cityAction.json?activityId&_ksTS=1658213415511_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme': ' https',
    'accept': ' text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': ' gzip, deflate, br',
    'accept-language': ' zh-CN,zh;q=0.9',
    'bx-v': ' 2.1.11',
    'cookie': ' miid=569742926381259424; thw=cn; cna=2JGkGsCIsCACAasr8IOp8nQT; tracknick=%5Cu8230%5Cu54E5668; _cc_=W5iHLLyFfA%3D%3D; enc=z%2B%2FshczMEyQvcG3BSZSaUu8vM3ku0lootiD0U%2FIQVLDNZfHgrNGpjc%2FTZo4grqSGfkvfgw2qyHIdjlFhfyc12w%3D%3D; sgcookie=E1001t9onOSGNlIluYTTuRfEx4zOj6BOaH8nlHxNqVi79Xxn4Dlc4FgXafdkFmenA8rKMpI6RipPmqbj7Dxa3DH2sFunR%2BZRHhqVLH5TTGzeE8YK0tvp6QM117pIw2xs5owo; t=e5a0999847ed09d8f24773fa2b6cc3db; cookie2=1074326b70f3542d3032f25d15efffa2; v=0; _tb_token_=e89e8354e416e; xlly_s=1; l=eBIt5otILxsWJGTjBO5ZPurza77tgIRbzsPzaNbMiInca1rRtFM7-NCHUsSwSdtjgtf3eetPUcfRbdUyWG4d0giMW_N-1NKc4xJw-; tfstk=cCp5B70eGz4SkNgfu_iqTgZxYy6FZCE1Ab_kVqV_lWNu-s-5i2yN5qX2tyBFvi1..; isg=BJOTxfv_9WyFK7nL9tRz0NDmIhe9SCcKCmEYt0WwerLpxLFmzRo-WrxS_jSq5H8C',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': ' ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': ' ?0',
    'sec-ch-ua-platform': ' "Windows"',
    'sec-fetch-dest': ' empty',
    'sec-fetch-mode': ' cors',
    'sec-fetch-site': ' same-origin',
    'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-requested-with': ' XMLHttpRequest',
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# 使用split切割
content = content.split('(')[1].split(')')[0]
# print(content)
# 将数据写入至文件中,并保存起来
with open('淘票票.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
# 创建obj接受json文件并读取
obj = json.load(open("淘票票.json", 'r', encoding='utf-8'))
city_list = jsonpath.jsonpath(obj,'$..regionName')
print(city_list)
