# encoding: utf-8
"""
@version: 1.0
@author: 
@file: Exercise3
@time: 2020-03-29 15:50
"""


def get_suffix(fileName, has_dot=False):
    """
        获取文件名的后缀名

        :param filename: 文件名
        :param has_dot: 返回的后缀名是否需要带点
        :return: 文件的后缀名
        """
    pos = fileName.rfind('.')
    if 0 < pos < len(fileName) - 1:
        index = pos if has_dot else pos + 1
        return fileName[index:]
    else:
        return ''


if __name__ == "__main__":
    file_suffix = get_suffix("a.txt", True);
    print(file_suffix)
