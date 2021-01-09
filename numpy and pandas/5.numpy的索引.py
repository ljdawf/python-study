import numpy as np
A = np.arange(3,15)
print(A)
print(A[3])###找到第三个



B = np.arange(3,15).reshape(3,4)
print(B)
print(B[2])###输出第二行
print(B[2][2])###输出二行二列的
print(B[2,2])###输出二行二列的数
print(B[2,:])###输出第二行的所有数
print(B[:,1])###输出第一列所有的数
print(B[1,1:2])####输出第一行的第一个数到第二个数，，，，，，，！！！！注意这个所有的第一行第二行指的都是从0行0列开始的！！！！



for row in B:
    print(row)###迭代输出每一行

for column in A.T:
    print(column)###迭代输出每一列



print(B.flatten())###返回一个值，变成一行的向量
for item in B.flat:###迭代器
    print(item)

