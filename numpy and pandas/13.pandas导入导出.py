import pandas as pd
import os
path = r"C:\Users\LJD\Desktop\莫烦python笔记\student.csv"
data = pd.read_csv(path,engine="python")####把engine定义为python，避免默认调用c,不认识中文
print(data)

data.to_pickle("student.pickle")###另存为pickle文件
