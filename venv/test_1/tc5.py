import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_csv('test.csv')

for d in df['数学']:
    if d < 100:
        # print(d.index)
        pass


print(df['英语']>110)
# print(df[df['英语']>110].index)
