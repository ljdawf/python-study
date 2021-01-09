import pandas as pd
import numpy as np
dates = pd.date_range("20200101",periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=["A","B","C","D"])

df.iloc[2,2]=1111###把2，2改成1111
print(df)


df.loc["20200103","B"] = 2222###用标签改
print(df)


df[df.A>4] = 0####大于4得改成0
print(df)


df.A[df.A>4] = 0000###只改A列
print(df)

df.B[df.A>2] = 0000###只改B列
print(df)


df["F"]= np.nan######加一个F列
print(df)


df["E"] = pd.Series([1,2,3,4,5,6],index = pd.date_range("20200101",periods = 6))####后面的操作是为了对齐
print(df)


