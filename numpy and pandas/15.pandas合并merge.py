import numpy as np
import pandas as pd
left = pd.DataFrame({"key":["K0","K1","K2",'K3'],'A':['A0','A1','A2','A3'],"B":["B0",'B1','B2','B3']})
right = pd.DataFrame({"key":["K0","K1","K2","K3"],"C":["C0","C1","C2","C3"],"D":["D0","D1","D2","D3"]})

res = pd.merge(left,right,on="key")
print(res)

left1 = pd.DataFrame({"key1":["K0","K1","K2",'K3'],"key2":["K0","K1","K0","K1"],'A':['A0','A1','A2','A3'],"B":["B0",'B1','B2','B3']})
right1 = pd.DataFrame({"key1":["K0","K1","K2","K3"],"key2":["K0","K0","K0","K0"],"C":["C0","C1","C2","C3"],"D":["D0","D1","D2","D3"]})

ress = pd.merge(left1,right1,on = ["key1","key2"],how="outer",indicator=True)###默认是inner，outer就是不管是否一样，都复制下来，inner重复的不复制，差不多就是交集吧。
print(ress)#####也可以how=“right”，how=“left”，就是基于左边或者右边合并,,indicator说的是merge得方式

###suffixes可以加后缀，suffixes=["_boy","_gril"]



