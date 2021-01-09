import numpy as np
a=np.array([[2,23,4],[2,3,4]],dtype=np.int)   #创建array,可以定义它的类型，int，float32，int64等等等，注意是用dtype
print(a)
print(a.dtype)


b=np.zeros((3,4))  #生成3行4列全部为0的矩阵
print(b)



c = np.ones((3,4),dtype = np.int16)   #全部为1
print(c)



d = np.empty((3,4))     #生成空的，但是输出的数字就是初始化，随机生成的
print(d)


f = np.arange(10,20,2)   #和python的range差不多
print(f)



g = np.arange(12).reshape((3,4))   #生成0到11的三行四列，小括号表示元组
print(g)



h = np.linspace(1,10,6).reshape((2,3))  #生成20段的1到10的数列，linespace是线段,也可以reshape，但是注意是几段
print(h)



