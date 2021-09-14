import os
import pandas as pd
import matplotlib.pyplot as plt
import xlrd


file_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'test_result.xlsx')
data = xlrd.open_workbook(file_path)
table = data.sheet_by_name('Sheet1')
list = table.col_values(0)
# list.remove('mcs')
list.pop(0)
print(list)
x = range(1,table.nrows,1)
print(x)
# df = pd.read_excel(file_path)
# x = df.index+1
# print(x)
# y = df['mcs']
# print(type(y))

plt.rcParams['font.sans-serif'] = ['SimHei']

plt.figure(num='mcs折线图',facecolor='y')

plt.plot(x, list, linestyle='--',color='m')

plt.show()