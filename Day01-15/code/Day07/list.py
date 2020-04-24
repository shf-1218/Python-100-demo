# encoding: utf-8
"""
@version: 1.0
@author: 
@file: list
@time: 2020-03-19 10:46
"""

"""定义列表、如何遍历列表以及列表的下标运算"""
list1 = [1, 2, 34, 5454, 66]
print(list1)
# 乘号表示列表元素的重复
list2 = ['Hello'] * 3
print(list2)
# 计算列表长度(元素个数)
print(len(list1))
# 下标(索引)运算
print(list2[2])
print(list1[1])
# print(list1[5])  # IndexError: list index out of range
print(list1[-1])
print(list2[-3])
list1[2] = 300
print(list1)
# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
# 通过for循环遍历列表元素
for elem in list1:
    print(elem)
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)

"""向列表中添加元素以及从列表中移除元素"""

list1 = [1, 2, 34, 413, 343251, 343, ]
# 添加元素
list1.append(122334)
list1.insert(1, 334343)
print(list1)
# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
print(list1)
# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
    list1.remove(3)
if 34 in list1:
    list1.remove(34)
print(list1)
# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1)
# 清空列表元素
list1.clear()
print(list1)

"""列表切片操作"""
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
fruits2 = fruits[1:4]
print(fruits2)
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3)
fruits4 = fruits[-3: -1]
print(fruits4)
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5)

"""列表的排序操作"""
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)

"""生成式和生成器"""
f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)

# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
import sys
f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数
print(f)

# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
print(f)
for val in f:
    print(val)



def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()