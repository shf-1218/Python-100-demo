#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/24 17:20
# @Author: hongfei.shen
# @File  : leap.py
'''
输入年份 如果是闰年输出True 否则输出False
'''
year = int(input("请输入年份:"))

is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)

print(is_leap)
