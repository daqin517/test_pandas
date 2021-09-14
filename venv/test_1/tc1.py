#-*-coding=utf-8-*-
import pandas as pd

pd.set_option('display.unicode.east_asian_width',True)
data = [[110,105,99],[105,88,115],[109,120,130]]
index = ['语文','数学','英语']
colunms = ['A','B','C']

df = pd.DataFrame(data=data,index=index,columns=colunms)
# print(df)

df.to_csv('test.csv')
print("-------------------------")
# for col in df.columns:
#     series = df[col]
#     print(series)

print(df['A'])