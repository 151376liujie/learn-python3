# 请在...补充一行或多行代码
from random import random


def prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


n = round(eval(input()))
string = ""
count = 0
while True:
    if count == 5:
        break
    if prime(n):
        count = count + 1
        string += (str(n) + ",")
    n = n + 1
print(string[0:len(string) - 1])