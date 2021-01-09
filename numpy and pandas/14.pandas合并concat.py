import pandas as pd
import numpy as np
####定义concatenate
df1 = pd.DataFrame(np.ones((3,4))*0,columns=["a","b","c","d"])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=["a","b","c","d"])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=["a","b","c","d"])

res = pd.concat([df1,df2,df3],axis=0)####向下合并
print(res)

res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)####忽略原来得标签，重新定义成012345678
print(res)

df3 = pd.DataFrame(np.ones((3,4))*0,columns=["a","b","c","d"],index=[1,2,3])
df4 = pd.DataFrame(np.ones((3,4))*1,columns=["b","c","d","e"],index=[2,3,4])####标签部分重合

ress = pd.concat([df3,df4])###这样输出，df3、df4没有的地方都用nan填充
print(ress)

resss = pd.concat([df3,df4],join="inner")###inner就是只合并重合部分，outer就是默认的，同样后面也可以加上ignore_index=True
print(resss)

abc=pd.concat([df3,df4],axis=1,join_axes=[df3.index])####代表按照df3得格式填充合并，后面用nan填充，不加join_axes,就两者都考虑
print(abc)

abb = df3.append([df1,df4],ignore_index = True)###可以加多个df，表示成列表就行，只有一个df加到后面，就不用列表得中括号了
print(abb)

s1 = pd.Series([1,2,3,4],index=["a","b","c","d"])####在后面加1234
red = df1.append(s1,ignore_index=True)
print(red)
