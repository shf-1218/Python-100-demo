#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/24 17:15
# @Author: hongfei.shen
# @File  : circle.py

'''
输入半径计算圆的周长和面积
'''

import math

redius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * redius
area = math.pi * redius * redius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
