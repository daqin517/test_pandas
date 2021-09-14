#-*-coding=utf-8-*-
from matplotlib import pyplot as plt

x = range(1,13,1)
y = range(20,76,5)
plt.figure(num='图1',figsize=(5,4),facecolor='m')
dates = []
for i in range(1,13):
    dates.append(str(i) + "月")
print(dates)
plt.xlabel('月份（2021年）')
plt.ylabel('体重（kg）')
plt.xticks(range(1,13,1),dates)
plt.yticks(range(50,90,5))
# plt.xlim(1,12)

kg = [65,62,67,68,70,64,63,62,87,67,69,70]

# plt.plot(x,y,color='m',linestyle='--',marker='o',mfc='w')
plt.plot(dates,kg)
plt.grid()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.text(1,4,4,ha='center',va='bottom')

plt.show()