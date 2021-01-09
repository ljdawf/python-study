import urllib.request
response=urllib.request.urlopen("http://www.baidu.com/")
print(response.info())
print('\n**************************************\n')
print(response.getcode())
print('\n*************************************\n')
print(response.read())