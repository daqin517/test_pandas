import matplotlib.pyplot as plt
import pandas as pd
import os

base_path =  os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
excel_path = os.path.join(base_path,'data','tizhong.xlsx')
print(excel_path)
df = pd.read_excel(excel_path)
x = df['月份']
y1 = df['狗子A']
y2 = df['狗子B']
y3 = df['狗子C']
# print(y)

plt.rcParams['font.sans-serif'] = ['SimHei']

plt.figure(num='图1',figsize=(6,4),facecolor='m',edgecolor='g')
plt.grid(axis='y')
width = 0.25
plt.bar(x,y1,label='狗子A',linestyle='-.',color='b',width=width)
plt.bar(x+width,y2,label='狗子B',linestyle='--',color='g',width=width)
plt.bar(x+width*2,y3,label='狗子C',linestyle=':',color='r',width=width)
plt.xlabel('月份（2021年）')
plt.ylabel('体重（kg）')
plt.yticks(range(50,90,5))
plt.xticks(range(1,13,1))
plt.ylim(50,90)
for a,b in zip(x,y1):
    # plt.text(a,b+1,'%0.1f'%b,ha='center',va='bottom',fontsize=9)
    pass
plt.title('体重变化曲线图')
plt.legend(loc='upper right')

# plt.annotate('最高体重',xy=('九月',82),xytext=('九月',78),arrowprops=dict(facecolor='r',shrink=0.05))

plt.savefig('tc2.jpg')
plt.show()