import numpy as np
A=np.arange(2,14).reshape((3,4))
print(A)
print(np.argmin(A))##输出最小值的索引
print(np.argmax(A))##输出最大值的索引
print(np.mean(A))#####输出平均值，或者print(A.mean())，，，mean换成average也行
print(np.median(A))####求中位数
print(np.cumsum(A))###逐次累加出来，2，2+3，2+3+4
print(np.diff(A))###累差
print(np.nonzero(A))###找到非0元素的坐标位置
print(np.sort(A))###排序
print(np.transpose(A))###矩阵的转置，也可以写成print(A.T)
print((A.T).dot(A))###矩阵乘法可能会用到转置
print(np.clip(A,5,9))###所有大于9的数字都变成9，所有小于5都变成5
print(np.mean(A,axis=0))###对各列求平均值


