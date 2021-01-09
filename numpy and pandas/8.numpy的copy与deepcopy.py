import numpy as np
a = np.arange(4)
b=a
c=a
d=b
a[0]=11
print(a)
print(d)
d[1:3]=[22,33]
print(a)#####以上就证明了大家都相等

b=a.copy()####deep copy,只是把值赋给b,但是没有把a和b关联起来，b的改变不会影响a，可以类比指针
a[3]=44
print(b)
print(a)