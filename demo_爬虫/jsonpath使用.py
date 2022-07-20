# jsonpath解析json数据
import json
import jsonpath

obj = json.load(open('JsonPath.json', 'r', encoding='utf-8'))

# 书店所有书的作者
# 创建一个作者列表来保存
# author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
# print(author_list)

# 所有作者
# author_list = jsonpath.jsonpath(obj,'$..author')
# print(author_list)

# store下面所有元素
# tag_list=jsonpath.jsonpath(obj,'$.*')
# print(tag_list)

# store里面所有的钱
# prices_list=jsonpath.jsonpath(obj,'$.store..price')
# print(prices_list)

# 第三本书
# book_list=jsonpath.jsonpath(obj,'$.store.book[2]')
# print(book_list)

# 最后一本书
# endbook_list=jsonpath.jsonpath(obj,'$...book[(@.length-1)]')
# print(endbook_list)

# 前两本
# book_list = jsonpath.jsonpath(obj, '$..book[:2]')
# print(book_list)


# 过滤书籍
# book_list=jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')
# print(book_list)

# 判断价格
book_list=jsonpath.jsonpath(obj,'$..book[?(@.price>10)]')
print(book_list)