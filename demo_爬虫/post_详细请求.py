import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers = {
    'Cookie': 'BIDUPSID=23188E39ED3929A29C47402D7A2E80F7; PSTM=1646103978; __yjs_duid=1_cf468b42cfadcdf353eba59d42baca4f1646107053327;  BAIDUID=DC97383977B3A0DA7A0763B87AE5475D:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_10_0_2=1; MCITY=-%3A; BDUSS=jNYWjROR2xlcjN1NnFPYm1XYmFGTzFPSnR0TkRNSHUtQkVxMlpoOXh-LVRTZHRpRVFBQUFBJCQAAAAAAQAAAAEAAADwLWFNY25tZHNiZHgyMjIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJO8s2KTvLNiW; BDUSS_BFESS=jNYWjROR2xlcjN1NnFPYm1XYmFGTzFPSnR0TkRNSHUtQkVxMlpoOXh-LVRTZHRpRVFBQUFBJCQAAAAAAQAAAAEAAADwLWFNY25tZHNiZHgyMjIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJO8s2KTvLNiW; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=DC97383977B3A0DA7A0763B87AE5475D:FG=1; ZFY=eTFyAbgsu6XBGm2reuy6E9xTzL8AznczfFqsZVfMxnA:C; delPer=0; PSINO=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1655604084,1657273122,1657674407,1657692799; BA_HECTOR=ag040l0g8g0h80800l2jj6g51hcsp3917; H_PS_PSSID=36561_36624_36819_36454_36452_36691_36165_36693_36698_36777_36773_36740_36761_36771_36766_26350_36717; ab_sr=1.0.1_ZTljM2FkZDcxMjhhODIwOGJmZWRjMWJlZTUyMGRmNGU2ZTIzNmRlNWNhOGMzZjJmYTYwMGI1ZTg0MjVjNDFkMmY0OWI5NzQ4NDZjNGU1ODM4YWMwM2Y2NDY4NjRlMzZiM2ExMGZhMTFlZGM3YTNiNmVmNzViZGIwYWM5MWUyNmE4NTMyYWI0OGEyNmRkYWVlODEyZDQ1ZjY1ZDZjZTJjMDA4YTNmOWRhMjdiODQxZjdhNWYwN2FlODEyYzYyNmNh; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1657694783',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
data = {
    'from': ' en',
    'to': ' zh',
    'query': ' love',
    'simple_means_flag': ' 3',
    'sign': ' 198772.518981',
    'token': ' 77e96945be337cbda53411e5e61c7c41',
    'domain': ' common'
}
# post必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象的定制
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取响应数据   并且转换编码
content = response.read().decode("utf-8")

obj = json.loads(content)
print(obj)
