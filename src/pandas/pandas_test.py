from pandas import Series, DataFrame

ser = Series([1, 2, 3])
print(ser)
print(ser.index)
print(ser.values)

print('-' * 30)

ser2 = Series([1, 2, 3], index=['a', 'b', 'c'])
print(ser2)
print(ser2.index)
print(ser2.values)

print('-' * 30)

data = {
    'city': ['shanghai', 'shanghai', 'shanghai', 'beijing', 'beijing'],
    'year': [2016, 2017, 2018, 2017, 2018],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9]
}

df = DataFrame(data, columns=['city', 'pop', 'year'])
print(df)
print(df.sort_index(ascending=False, axis=0))
print('-' * 30)
print(df.sort_index(ascending=False, axis=1))
print(df.year)
print('-' * 30)
# 新建一列
df['new'] = [100, 200, 300, 400, 500]
print(df)

print('-' * 30)
# 根据某一列动态生成新列的值
df['isCapital'] = df['city'] == 'beijing'
print(df)
print('-' * 30)

data = {
    'beijing': {
        2008: 1.5,
        2009: 2.5,
        2010: 3.5,
    }, 'shanghai': {
        2008: 1.2,
        2009: 2.4,
        2010: 1.5,
    }
}

df2 = DataFrame(data)
print(df2)

from numpy import nan as NA

s3 = Series([1, NA, 3, 5])
# 删掉有缺失值的行
s4 = s3.dropna()
print(s3)
print(s4)

data2 = {
    'beijing': {
        2008: 1.5,
        2009: NA,
        2010: 3.5,
        2011: NA,
    }, 'shanghai': {
        2008: 1.2,
        2009: NA,
        2010: 1.5,
        2011: 3.4,
    }, 'sanya': {
        2008: NA,
        2009: NA,
        2010: 3.4,
        2011: 8.6,
    }
}

df3 = DataFrame(data2)
print(df3)

print('-' * 30)
# 只要包含缺失值就会删除
print(df3.dropna())

# 某一列的值全为缺失值
df3['guangzhou'] = NA

print(df3)
print('-' * 30)

# 删除一列全是缺失值的列
print(df3.dropna(axis=1, how='all'))

#将缺失值填充为0
df3 = df3.fillna(0)
print(df3)

print('-' * 30)
# 填充值
df3.fillna(0,inplace=True)
print(df3)