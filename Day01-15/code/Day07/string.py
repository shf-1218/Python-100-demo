# encoding: utf-8
"""
@version: 1.0
@author:
@file: string1
@time: 2020-03-19 10:23
"""

s1 = 'hello,world!'
s2 = "hello,world!"
s3 = """
     hello,
     world!
     """

print(s1, s2, s3)

"""可以在字符串中使用\（反斜杠）来表示转义"""
s1 = '\'Hello,World!\''
s2 = "\n\\Hello,World!\\\n"
print(s1, s2, end=' ')

"""在\后面还可以跟一个八进制或者十六进制数来表示字符"""

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)

"""不希望字符串中的\表示转义"""
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')

"""字符串类型运算"""

s1 = 'Hello' * 3
print(s1)
s2 = "world"
s1 += s2
print(s1)
print('ll' in s1)
print("good" in s1)
s3 = "adfdljjdfld"

# 从字符串中取出指定位置的字符(下标运算)
print(s3[2])
# 字符串切片(从指定的开始索引到指定的结束索引)
print(s3[2:5])
print(s3[2:])
print(s3[2::2])
print(s3[::2])
print(s3[::-1])
print(s3[-3:-1])

"""字符串的处理"""
str1 = "Hello,World!"
# 通过内置函数len计算字符串的长度
print(len(str1))
# 获得字符串首字母大写的拷贝
print(str1.capitalize())
# 获得字符串每个单词首字母大写的拷贝
print(str1.title())
# 获得字符串变大写后的拷贝
print(str1.upper())
# 从字符串中查找子串所在位置
print(str1.find('or'))
print(str1.find('shit'))
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith("He"))
print(str1.startswith('hel'))
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!'))
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))

str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())
# 检查字符串是否以字母构成
print(str2.isalpha())
# 检查字符串是否以数字和字母构成
print(str2.isalnum())
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())


"""格式化输出字符串"""
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b}')