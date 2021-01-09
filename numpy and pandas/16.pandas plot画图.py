import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()##累加
data.plot()
plt.show()


data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list("ABCD"))
data = data.cumsum()
print(data.head())
data.plot()
plt.show()####bar  hist box  kde area  scatter   hexbin   pie

data.plot.scatter(x="A",y="B",color="DarkBlue",label="Class 1")
data.plot.scatter(x="A",y="C",color="DarkGreen",label="Class 2",ax=ax)  ####ax=ax是打印在一张图上面，这里运行出错，不清楚为什么
plt.show()  