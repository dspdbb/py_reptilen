from lxml import etree

# xpath解析
# 1）本地文件     etree。parse
# 2）服务器响应数据  etree。HTML（）    content=response。read（），decode（‘utf-8’）

# xpath解析本地文件
tree = etree.parse('1.html')
# tree.xpath('xpath路径')
a= tree.xpath('//body/ul/li')
# text获取标签中的内容
# 查找带有id的属性值
b=tree.xpath('//body/ul/li[@id]/text()')
b=tree.xpath('//body/ul/li[@id="wj"]/text()')
# 查找id为‘wj’,class的属性值
ab=tree.xpath('//body/ul/li[@id="qq"]/@class')
# 模糊查询
s=tree.xpath('//ul/li[contains(@id,"s")]/text()')
# 查询以什么开头的
svb=tree.xpath('//ul/li[starts-with(@id,"w")]/text()')
# 条件查询
qq=tree.xpath('//ul/li[@id="svs" and @class="qq"]/text()')
print(qq)