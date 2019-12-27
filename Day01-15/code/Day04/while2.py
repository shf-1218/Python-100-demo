# encoding: utf-8
"""
@version: 1.0
@author: 
@file: while2
@time: 2019-12-28 00:11
"""

'''
用while循环实现1～100之间的偶数求和
'''

sum, num = 0, 1
while num <= 100:
    if num % 2 == 0:
        sum += num
    num += 1
print(sum)
