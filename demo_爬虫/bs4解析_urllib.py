from bs4 import BeautifulSoup

# bs4优点：人性化
# 通过解析本地文件来解析bs4
# 需要指定编码,默认编码为 GBK,
soup = BeautifulSoup(open('bs4.html', encoding='utf-8'), 'lxml')
# print(soup)

# 根据标签名查找节点
# print(soup.a)
#
# # 获取标签的属性和属性值
# print(soup.a.attrs)


# bs4 的一些函数

# 1.find
# 2.find_all
# 3.select

# 返回第一个符合条件的数据
# print(soup.find('a'))
# 返回特定值
# print(soup.find('a',title="a2"))
# 注意如果要返回class那么要在class后面加上下划线
# print(soup.find('a',class_="ss"))

# 返回所有a标签
# print(soup.find_all('a'))

# 返回需要的所有标签,那么需要返回的数据是列表的数据
# print(soup.find_all(['a','span']))

# 返回需要的数值  limit是使用在有几个
# print(soup.find_all('a',limit=2))

# select推荐
# ***select方法返回的是一个列表并且会返回多个数据
# print(soup.select('a'))
# 可以返回id
# print(soup.select('#li'))

# 属性选择器
# 可以通过属性来选择标签
# 查询li中有id的li标签
# print(soup.select('li[id]'))


# 层级选择器
# 后代选择器
# 找到的是div后面的li
# print(soup.select('div li'))

# 子代选择器
# 莫标签的第一级子标签
# 在大部分编程语言中，如果不加空格可能会不输出，但是在“bs4”中不会
# print(soup.select('div>ul>li'))


# 找到a标签和li标签的所有对象
# print(soup.select('a,li')).



# 节点信息