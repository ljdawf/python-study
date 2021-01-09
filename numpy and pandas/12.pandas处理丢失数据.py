import pandas as pd
import numpy as np
dates = pd.date_range("20200101",periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=["A","B","C","D"])

df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan

print(df.dropna(axis=0,how="all"))###某一行存在nan，这一行就丢掉了，，，，，，如果这一行都是nan，才丢掉是all，，，，默认是any

print(df.fillna(value=0))####把nan填成0

print(df.isnull())####判断哪里有缺失，即哪里有nan

print(np.any(df.isnull()) == True)####丢失得地方返回True



