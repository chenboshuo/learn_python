# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     formats: ipynb,py:light,md
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # tips

# ## - 交换变量

# pythonic way of value swapping
a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b)

# ## 查找列表中频率最高的值 

# +
' ''most frent element in a list'''

a = [1, 2, 3, 1, 3, 5, 3]

print(max(set(a), key=a.count))

'''using counter from collections'''

from collections import Counter

cnt = Counter(a)
print(cnt.most_common(3))
# -

help(set)
# iterable 可迭代对象,可遍历的
# builtin 内嵌指令

import collections
help (collections)

# ## 检查两个字符串是否由相同字母不同顺序组成

# +
from collections import Counter

str1 = 'asdfghjk'
str2 = 'kjhgfdsa'
Counter(str1) == Counter(str2)
# -

# ## - 同步赋值

# 同步赋值
a, b = 1, 2
# a = a+b, b=a 同时运行,运算时用原始值
a, b = a+b,a
'''
a = a+b = 1+2 =3
b= a =1
'''
a,b

list1 = [1,2,3,4,5]
# list1[0,1] = ['a', 'b'] TypeError: list indices must be integers or slices, not tuple
list1[0:1] = ['a', 'b']
list1

list1 = [1,2,3,4,5]
list1[0:2] = ['a', 'b']
list1

# ## - 在列表开头插入元素

list1 = [0, 1, 2, 3, 4]
list1[:0] = ['a']
list1

# ## - 字符与ASCII码

chr(65)

str(ord('a'))

ord('a')

# ## - 推导式

# ### 1.普通推导式

list1 = [i for i in range(5)]
list1

# 生成奇数
list2 = [i for i in range(1,15) if i&1]
list2

# ### 2.二维推导式

# 2-19 输出所有合数
composite = [j for i in range(2, 20) for j in range(i*i,20,i)]
print(composite)
# 输出2-19的质数
prime = [i for i in range(2,20) if i not in composite]
prime

# ## enumerate(iterable [,start=0])

list_ =[1,2,3]
for i, item in enumerate(list_):
    # so stuff with item, for example print it
    print (i, item)

# ## 生成器

tuple1 = (x for x in range (10))
tuple1

tuple(tuple1)

tuple(tuple1)

# 生成器将需要的生成一次

tuple1 = (x for x in range (3))
tuple1[0]

for i in tuple1:
    print(i)

tuple(tuple1)

# ## all or any

x = [True, True, False]
if any(x):
    print("At lesat one True")
if all(x):
    print("Not one False")
if any(x) and not all(x):
    print("At least one True or False")


# + [markdown] {"heading_collapsed": true}
# # math

# + [markdown] {"hidden": true}
# ## 角度与弧度转化

# + {"hidden": true}
import math
math.radians(180)

# + [markdown] {"hidden": true}
# ## 取整

# + {"hidden": true}
# 向上取整
math.ceil(3.1)

# + {"hidden": true}
# 向下取整
math.floor(3.9)
# -

# # time

# +
import time

time.sleep(10) # 程序暂停10s
# -

# # 小函数

min(1, 3, 5)

sum([2,3,5]) # 必须是列表

# 生成(商,余数)对
divmod(10,3)

10 // 3, 10 % 3

line = 'abcdL'
line.capitalize()

help(str.capitalize)

# ## pow(x, y)

import cProfile

cProfile.run('pow(1234567,4567676,56)')


def power(x,y,z):
    a = x**y % z
# cProfile.run(power(1234567,4567676))
# ypeError: exec() arg 1 must be a string, bytes or code object
cProfile.run('power(1234567,4567676,56)')

cProfile.run('pow(1234567,4567676)')


# +
def power(x,y):
    a = x**y
    
cProfile.run('power(1234567,4567676)')    
# -

# ## filter
# Filter函数接受一个列表和一条规则，就像map一样，但它通过比较每个元素和布尔过滤规则来返回原始列表的一个子集。

seq = [1,2,3,4,5]
list(filter(lambda x:x > 2,seq))


# ## bisect
# -  [reference](https://stackoverflow.com/questions/62110746/is-there-a-better-way-to-check-if-a-number-is-range-of-two-numbers)

def checkRange(number):
    if number in range(0, 5499):
        return 5000
    elif number in range(5500, 9499):
        return 10000
    elif number in range(9500, 14499):
        return 15000
    elif number in range(14500, 19499):
        return 20000
    elif number in range(19500, 24499):
        return 25000
    elif number in range(24500, 29499):
        return 30000
    elif number in range(29500, 34499):
        return 35000
    elif number in range(34500, 39499):
        return 40000
    elif number in range(39500, 44499):
        return 45000
print(checkRange(10000))

# +
import bisect

break_points = [5499,  9499, 14499, 19499, 24499, 29499, 34499, 39499, 44499]
values       = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000]

n = 10000
index = bisect.bisect_left(break_points, n)

values[index]
# -

# ## numpy

import numpy as np

# ### arange 返回等差列表
# Arange返回给定步长的等差列表。它的三个参数start、stop、step分别表示起始值，结束值和步长， 请注意，stop点是一个“截止”值，因此它不会包含在数组输出中。

np.arange(3,7,2)

# ### linspace 等距离分割区间
# Linspace和Arrange非常相似，但略有不同。Linspace以指定数目均匀分割区间。所以给定区间start和end，以及等分分割点数目num，linspace将返回一个NumPy数组。这对绘图时数据可视化和声明坐标轴特别有用。

# np.llinspace(start,stop,num)
np.linspace(2.0,3.0,num=5)

# # python mutable 和 immutable
# python中有一个比较有意思的地方，变量是指向某一个数据的地址的，改变数据就是改变指向就行了。而在c语言等中，一个变量的地址是不变的，变量的值改变只是这个地址里面的内存数据发生变化。

a = 1  
print(id(a))  
a = 2  
id(a)  


a = 1
b = a
b+=1
print(a)
print(b)
id(a) == id(b), id(a), id(b)

# python里面的类型其实也分为immutable和mutable二种，之所以会导致上面的现象，就是因为常数是immutable类型，回想之前说python任何数据都是对象，既然1,2也是对象，而且还是immutable，当然不能被b修改，所以会为b重新开辟空间存放这个immutable的对象2。
#
# 那好，如果a是一个mutable的引用呢？

a = [1,2]
b = a
b += [3]
print(a)
print(b)
id(a) == id(b)

a = [1,2]
b = a
id(a) == id(b)


# 这里并没有开辟新的内存，不需要作何解释了。
#
# 那么在python那些是immutable呢？
#
# numbers, strings, tuples, frozensets

# # switch 的python实现

# ## 多次使用if-else

# +
something = 'something'

if something == 'this':
    the_thing = 1
elif something == 'that':
    the_thing = 2
elif something == 'there':
    the_thing = 3
else:
    the_thing = 4
print(the_thing)
# -

# ## 用get设置默认值的字典提取

something = input()
options = {'this': 1, 'that':2 , 'there': 3}
the_thing = options.get(something, 4)
print(the_thing)

# ## 利用if-else配合不设默认值的字典提取

something = input()
options = {'this': 1, 'that': 2, 'there': 3}
if something in options:
    the_thing = options[something]
else:
    the_thing = 4
print(the_thing)

# ## 用collections模块设置默认值进行字典提取

from collections import defaultdict
something = input()
default_options = defaultdict(lambda: 4, {'this': 1, 'that': 2, 'there': 3})
the_thing = default_options[something]
print(the_thing)

# ## 速度比较

# 1. 四种方法之间的对比，后两种方法明显比前两种方法快，且最后一种方法总是最快的。
#
# 2. 待判断内容是否在字典中设置的对比
#
# 第一种全程if-else判断的情况下，早判断出来程序就会早结束，所以if-else判断的内容顺序是有讲究的
# 而从字典里提取则没有看出显著的不同
# 由于使用collections模块中的defaultdict虽然最快，但是会占用较多内存，所以最推荐的是第三种方法，使用if-else配合无默认字典提取方法。

# #  python中输入多个数字

# ## 基础方法 

# +
list1 = [] # 定义一个空字符串
str1 = input('请输入数值,用空格隔开')
list2 = str1.split(' ')# list2用来存储输入字符串,用空格分隔


while list2:
    list1.append(int(list2.pop()))
    
list1.reverse()
print(list1)


# -

# ## map()函数
# map() 会根据提供的函数对指定序列做映射。
#
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

# +
# 计算平方数
def square(x):
    return x ** 2
print(list(map(square,[1,2,3,4,5])))
print(list(map(lambda x:x**2,[1, 2, 3, 4, 5])))

# 提供两个列表,对相同位置数据相加
print(list(map(lambda x, y:x+y,[1,3,5],[2,4,6])))
# -

# 一行实现输出多个数字
print(list(map(int, input().split())))

nums = [2,11,7,15]
target = 9
buff_dict = {}
for i in range(len(nums)):
    if 7 in buff_dict:
        print([buff_dict[7], i])
    else:
        buff_dict[target - nums[i]] = i
buff_dict
