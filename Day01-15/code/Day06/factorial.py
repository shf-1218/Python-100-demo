# encoding: utf-8
"""
@version: 1.0
@author: 
@file: factorial
@time: 2020-03-18 15:07
"""


def factorial(num):
    """求阶乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n

    return result

m = int(input('m = '))
n = int(input('n = '))
print(factorial(m) // factorial(n) // factorial(m - n))