import numpy as np
a=np.array([10,20,30,40])
b=np.arange(4)   #指的是0到3
c = a-b
d=a+b
e = b**2    ##加减乘除都可以算
h = 10*np.sin(a)   ##sin cos都可以的
print(b<3)  ###判断哪些小于3，返回true或者false,>  = 也可以算
print(a,b,c,d,e,h)




q=np.array([[1,1],[0,1]])
w=np.arange(4).reshape(2,2)   #定义矩阵
p=np.dot(q,w)   ####这是矩阵的正常运算，是叉乘，或者写成，q.dot(w)        
o=q*w    ###这是各个元素逐个相乘
print(q,w,p,o)




y=np.random.random((2,4))    ###random模块下的random方法，生成0到1的随机的2乘4的矩阵
print(y)
print(np.max(y))     #####可以找到array里面的最大值最小值 求和等等等，，sum min max
print(np.sum(y,axis = 1))  ###1代表在每一行之间求和，如果等于0就代表在每一列之间求和，max min同理


