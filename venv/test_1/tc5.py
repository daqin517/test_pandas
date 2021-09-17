import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_csv('test.csv')
df['物理'] = [88,79,60]
df = df.set_index(['学号'],drop=True)
print(df)

print('===============')

print(df['数学'][110])


print('===============')
print(df.at[110,'数学'])

print('===============')
print(df['语文']<110)
print(df[df['语文']<110].index)

print(type(df['语文']))
# print(df['英语']>110)
# print(df[df['英语']>110].index)
