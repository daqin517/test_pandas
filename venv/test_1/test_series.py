import pandas as pd

pd.set_option('display.unicode.east_asian_width',True)

list = [1,5,9,'aaaaaa']
# s1 = pd.Series(list,index=['数字1','数字2','数字3','字母1'])
s1 = pd.Series(list)
print(len(s1))
print('s1.index:',s1.index)
print(s1.values)

b = s1.index
print(type(b))