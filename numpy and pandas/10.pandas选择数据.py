import pandas as pd
import numpy as np
dates = pd.date_range("20200101",periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=["A","B","C","D"])
print(df["A"],df.A)###输出A列
print(df[0:3],df["20200102":"20200103"])###输出某几行
print(df.loc["20200103"])###输出20200103的数据
print(df.loc[:,["A","B"]])###打印这两列中所有行的数据
print(df.loc["20200103",["A","B"]])####只打印20200103对应的AB
print(df.iloc[3])###第几行
print(df.iloc[3:5,1:3])##筛选第三行，第一个和第二个
print(df.ix[:3,["A","C"]])###筛选AC两列和012行
print(df[df.A>8])###筛选大于8的数列
