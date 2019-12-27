#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/24 17:52
# @Author: hongfei.shen
# @File  : verify.py

'''
用户身份验证
'''

import getpass

username = input('请输入用户名: ')
# password = input('请输入密码: ')
# 如果希望输入口令时 终端中没有回显 可以使用getpass模块的getpass函数\
password = getpass.getpass('请输入密码: ')
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')
