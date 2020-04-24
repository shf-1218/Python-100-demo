#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/24 16:39
# @Author: hongfei.shen
# @File  : operator.py
'''
赋值运算符和复合赋值运算符
'''

a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= d
a /= e
print('a = ', a)



'''比较、逻辑和算身份运算符的使用'''
flag1 = 3 > 2
flag2 = 3 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)
