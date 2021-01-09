import numpy as np
A = np.array([1,1,1])
B = np.array([2,2,2])
C = np.vstack((A,B))
D = np.hstack((A,B))
A = A[:,np.newaxis]###行向量变成列向量
print(np.vstack((A,B)))###上下的合并
print(np.hstack((A,B))###左右的合并
print(A.shape,B.shape,C.shape,D.shape)###查看类型


V = np.concatenate((A,B,B,A),axis = 1)####多个合并
print(V)
