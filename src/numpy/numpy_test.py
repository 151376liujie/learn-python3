import numpy as nu

a1 = nu.array([1, 2, 3, 4, 5])
a2 = nu.array([1.2, 2.3, 3.4, 4.5, 5.6])
print(a1 + a2)
print(a1 * a2)
# 定义一个长度为10的一维数组
a3 = nu.zeros(10)
print(a3)

#定义一个二维数组
a4 = nu.zeros((3,4))
print(a4)
# 定义一个4个长度的数组，其值为0-4
a5 = nu.arange(4)
print(a5)