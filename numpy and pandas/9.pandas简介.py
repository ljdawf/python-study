###pandas相对于numpy就像一个字典，各行各列可以定义
import pandas as pd
import numpy as np
s = pd.Series([1,3,6,np.nan,44,4])
print(s)

###输出矩阵
dates = pd.date_range("20200101",periods=6)
print(dates)


###自定义名称，否则名字就是012345......还定义了各列的索引columns，各行的索引是日期
df = pd.DataFrame(np.random.randn(6,4),index = dates,columns=["a","b","c","d"])
print(df)


###这种没有定义行列标签的就是默认0123表示了
df1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df1)

####随机生成的不带名字的
g = pd.DataFrame(np.random.randn(6,4))
print(g)

###输出各列的类型
print(df1.dtypes)


####输出序号
print(df1.index)


###打印行的名字
print(df1.columns)


###打印值
print(df1.values)


###打印出描述值
print(df1.describe())


###转置
print(df1.T)


###排序,对列倒叙排列
print(df1.sort_index(axis=1,ascending=False))



####对行倒叙
print(df1.sort_index(axis = 0,ascending = False))




###还可以对values排序
print(df1.sort_values(by='里面写某一列的名称即可'))
