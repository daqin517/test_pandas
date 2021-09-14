import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

x = [0.3,0.1,0.2,0.4]
labels = ['A','B','C','D']

plt.rcParams['font.sans-serif'] = ['SimHei']
colors = ['r','g','b','m']

plt.figure(num='test',facecolor='y')
plt.grid()
plt.pie(x,labels=labels,colors=colors,autopct='%.1f%%',shadow=True, explode=(0.1,0,0,0))

plt.savefig('pie.jpg')

plt.show()