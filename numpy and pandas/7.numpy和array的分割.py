import numpy as np
A = np.arange(12).reshape((3,4))
print(np.split(A,2,axis=1))###按照列分成两块，如果是3就会报错，不能进行不等的分割
print(np.array_split(A,3,axis=1))###可以进行不等的分割
print(np.vsplit(A,3))###纵向分割成两块
print(np.hsplit(A,2))###横向分割成两块