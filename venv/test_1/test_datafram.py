import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
df = pd.DataFrame({
    '语文':[110,105,99,120],
    '数学':[105,88,115,118],
    '英语':[109,120,130,98],
    '班级':['高一7班']
},index=[0,1,2,3])


print(df)

