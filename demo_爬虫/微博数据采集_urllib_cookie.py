# 使用场景，需要的采集数据，需要登陆，绕过登录进行采集
# 个人信息页面是utf—8，报错是因为默认跳转登录页面，而登录页面的编码不一定是utf—8
# 那么就会报错！！！！


# 什么情况下访问不成功
# 因为请求头的信息不够
import urllib.request

url='https://weibo.com/u/3027523851'

headers={
'cookie': 'SINAGLOBAL=5111098007097.559.1651972211072; PC_TOKEN=c381a445cd; login_sid_t=a3d87b24ee30c9f350761305af76bacd; cross_origin_proto=SSL; _s_tentry=weibo.com; Apache=6949789826877.612.1657952454921; ULV=1657952454927:2:1:1:6949789826877.612.1657952454921:1651972211079; appkey=; SSOLoginState=1657952505; ALF=1689488555; SUB=_2A25P1il8DeRhGeVO6VUU8i3Ezj2IHXVsoh20rDV8PUNbmtANLVnFkW9NTWkYQRqYUcwm2vWMB6IrWSwNVouxC-ve; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WheN_HFSqHqKB24xYd5PIGh5JpX5KzhUgL.Foe7eoMfeoeRSK22dJLoIEXLxK-LBKBLBK.LxKML1h-L1--LxK.L1h2L1hMLxK-LBKBLBK.LxKBLB.BLB.qt',
# 'access-control-allow-origin':' *',
# 'age':' 76621',
# 'cache-control':' max-age=31536000',
# 'content-encoding':' gzip',
# 'content-length':' 637',
# 'content-type':' text/css',
# 'date: Sat, 16 Jul 2022 06:20':'22 GMT',
# 'edge-copy-time':' 1657904068270',
# 'etag':' W/"62d11c48-6ed"',
# 'expires: Sat, 15 Jul 2023 09:03':'20 GMT',
# 'last-modified: Fri, 15 Jul 2022 07:50':'32 GMT',
# 'ruri':' /m/weibo-pro/css/chunk-04dd4069.47a5a2b0.css',
# 'server':' nginx',
# 'vary':' Accept-Encoding',
# 'via':' http/1.1 cnc.beixian.union.197 (ApacheTrafficServer/6.2.1 [cRs f ]), http/1.1 tvn.hubei.union.100 (ApacheTrafficServer/6.2.1 [cRs f ])',
# 'x-cache':' HIT.unknown',
# 'x-via-cdn':' f=edge,s=tvn.hubei.union.98.nb.sinaedge.com,c=10.207.126.82;f=Edge,s=tvn.hubei.union.100,c=119.36.52.98',
# 'x-via-edge':' 1657952422658527ecf0a6234247777d7a90a',
}
# 请求对象定制
request=urllib.request.Request(url=url,headers=headers)

# 获取网页源码
response=urllib.request.urlopen(request)

# 获取响应内容
content=response.read().decode('utf-8')
print(content)

with open('web.html','w',encoding='utf-8') as fp:
    fp.write(content)