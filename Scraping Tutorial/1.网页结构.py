####html,css,javascrit,,,html包括head，body，body得标签会显示在网页，head是一些源信息，不会显示，大多数时候爬取得是body信息。
from urllib.request import urlopen
import re

html = urlopen(“网址信息”).read().decode("utf-8")####存在中文，转换成utf-8得形式
print(html)

res = re.findall(r"<title>(.+?)</title>",html)####使用正则表达式规范输出title
print("\nPage title is:", res[0])

res = re.findall(r"<p>(.*?)</p>",html,flags=re.DOTALL)####使用正则表达式输出p之间的内容
print("\nPage paragraph is:",res[0])


