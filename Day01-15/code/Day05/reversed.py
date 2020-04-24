# encoding: utf-8
"""
@version: 1.0
@author:
@file: reversed
@time: 2020-03-18 14:59
"""
"""正整数的反转"""
num = int(input("num = "))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
