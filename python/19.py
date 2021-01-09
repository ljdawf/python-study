import pickle 
a_dict={"a":1,"b":2,"c":3}#以前的字典无序
file=open("pickle_example.pickle","wb")
pickle.dump(a_dict,file)
file.close()
file=open("pickle_example.pickle","rb")
a_dict1=pickle.load(file)
file.close()
print(a_dict1)

with open("pickle_example.pickle","rb") as file:     ##使用with的好处就是不用担心文件关闭的问题，不用使用close 
    a_dict1=pickle.load(file)
    print(a_dict1)