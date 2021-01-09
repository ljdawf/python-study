import copy
a=[1,2,3]
b=a
id(a)
id(b)
a[1]=22
print(b)
print(id(a)==id(b))