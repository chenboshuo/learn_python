# -*- coding: utf-8 -*-
---
jupyter:
  jupytext:
    cell_metadata_json: true
    formats: ipynb,py:light,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.3
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# tips


## - 交换变量

```python
# pythonic way of value swapping
a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b)
```

## 查找列表中频率最高的值 

```python
' ''most frent element in a list'''

a = [1, 2, 3, 1, 3, 5, 3]

print(max(set(a), key=a.count))

'''using counter from collections'''

from collections import Counter

cnt = Counter(a)
print(cnt.most_common(3))
```

```python
help(set)
# iterable 可迭代对象,可遍历的
# builtin 内嵌指令
```

```python
import collections
help (collections)
```

## 检查两个字符串是否由相同字母不同顺序组成

```python
from collections import Counter

str1 = 'asdfghjk'
str2 = 'kjhgfdsa'
Counter(str1) == Counter(str2)
```

## - 同步赋值

```python
# 同步赋值
a, b = 1, 2
# a = a+b, b=a 同时运行,运算时用原始值
a, b = a+b,a
'''
a = a+b = 1+2 =3
b= a =1
'''
a,b
```

```python
list1 = [1,2,3,4,5]
# list1[0,1] = ['a', 'b'] TypeError: list indices must be integers or slices, not tuple
list1[0:1] = ['a', 'b']
list1
```

```python
list1 = [1,2,3,4,5]
list1[0:2] = ['a', 'b']
list1
```

## - 在列表开头插入元素

```python
list1 = [0, 1, 2, 3, 4]
list1[:0] = ['a']
list1
```

## - 字符与ASCII码

```python
chr(65)
```

```python
str(ord('a'))
```

```python
ord('a')
```

## - 推导式


### 1.普通推导式

```python
list1 = [i for i in range(5)]
list1
```

```python
# 生成奇数
list2 = [i for i in range(1,15) if i&1]
list2
```

### 2.二维推导式

```python
# 2-19 输出所有合数
composite = [j for i in range(2, 20) for j in range(i*i,20,i)]
print(composite)
# 输出2-19的质数
prime = [i for i in range(2,20) if i not in composite]
prime
```

## enumerate(iterable [,start=0])

```python
list_ =[1,2,3]
for i, item in enumerate(list_):
    # so stuff with item, for example print it
    print (i, item)
```

## 生成器

```python
tuple1 = (x for x in range (10))
tuple1
```

```python
tuple(tuple1)
```

```python
tuple(tuple1)
```

生成器将需要的生成一次

```python
tuple1 = (x for x in range (3))
tuple1[0]
```

```python
for i in tuple1:
    print(i)
```

```python
tuple(tuple1)
```

## all or any

```python
x = [True, True, False]
if any(x):
    print("At lesat one True")
if all(x):
    print("Not one False")
if any(x) and not all(x):
    print("At least one True or False")
```


<!-- #region {"heading_collapsed": true} -->
# math
<!-- #endregion -->

<!-- #region {"hidden": true} -->
## 角度与弧度转化
<!-- #endregion -->

```python hidden=true
import math
math.radians(180)
```

<!-- #region {"hidden": true} -->
## 取整
<!-- #endregion -->

```python hidden=true
# 向上取整
math.ceil(3.1)
```

```python hidden=true
# 向下取整
math.floor(3.9)
```

# time

```python
import time

time.sleep(10) # 程序暂停10s
```

# 小函数

```python
min(1, 3, 5)
```

```python
sum([2,3,5]) # 必须是列表
```

```python
# 生成(商,余数)对
divmod(10,3)
```

```python
10 // 3, 10 % 3
```

```python
line = 'abcdL'
line.capitalize()
```

```python
help(str.capitalize)
```

## pow(x, y)

```python
import cProfile
```

```python
cProfile.run('pow(1234567,4567676,56)')
```

```python
def power(x,y,z):
    a = x**y % z
# cProfile.run(power(1234567,4567676))
# ypeError: exec() arg 1 must be a string, bytes or code object
cProfile.run('power(1234567,4567676,56)')
```

```python
cProfile.run('pow(1234567,4567676)')
```

```python
def power(x,y):
    a = x**y
    
cProfile.run('power(1234567,4567676)')    
```

## filter
Filter函数接受一个列表和一条规则，就像map一样，但它通过比较每个元素和布尔过滤规则来返回原始列表的一个子集。

```python
seq = [1,2,3,4,5]
list(filter(lambda x:x > 2,seq))
```

## numpy

```python
import numpy as np
```

### arange 返回等差列表
Arange返回给定步长的等差列表。它的三个参数start、stop、step分别表示起始值，结束值和步长， 请注意，stop点是一个“截止”值，因此它不会包含在数组输出中。

```python
np.arange(3,7,2)
```

### linspace 等距离分割区间
Linspace和Arrange非常相似，但略有不同。Linspace以指定数目均匀分割区间。所以给定区间start和end，以及等分分割点数目num，linspace将返回一个NumPy数组。这对绘图时数据可视化和声明坐标轴特别有用。

```python
# np.llinspace(start,stop,num)
np.linspace(2.0,3.0,num=5)
```

# python mutable 和 immutable
python中有一个比较有意思的地方，变量是指向某一个数据的地址的，改变数据就是改变指向就行了。而在c语言等中，一个变量的地址是不变的，变量的值改变只是这个地址里面的内存数据发生变化。

```python
a = 1  
print(id(a))  
a = 2  
id(a)  
```


```python
a = 1
b = a
b+=1
print(a)
print(b)
id(a) == id(b), id(a), id(b)
```

python里面的类型其实也分为immutable和mutable二种，之所以会导致上面的现象，就是因为常数是immutable类型，回想之前说python任何数据都是对象，既然1,2也是对象，而且还是immutable，当然不能被b修改，所以会为b重新开辟空间存放这个immutable的对象2。

那好，如果a是一个mutable的引用呢？

```python
a = [1,2]
b = a
b += [3]
print(a)
print(b)
id(a) == id(b)
```

```python
a = [1,2]
b = a
id(a) == id(b)
```


这里并没有开辟新的内存，不需要作何解释了。

那么在python那些是immutable呢？

numbers, strings, tuples, frozensets


# switch 的python实现


## 多次使用if-else

```python
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
```

## 用get设置默认值的字典提取

```python
something = input()
options = {'this': 1, 'that':2 , 'there': 3}
the_thing = options.get(something, 4)
print(the_thing)
```

## 利用if-else配合不设默认值的字典提取

```python
something = input()
options = {'this': 1, 'that': 2, 'there': 3}
if something in options:
    the_thing = options[something]
else:
    the_thing = 4
print(the_thing)
```

## 用collections模块设置默认值进行字典提取

```python
from collections import defaultdict
something = input()
default_options = defaultdict(lambda: 4, {'this': 1, 'that': 2, 'there': 3})
the_thing = default_options[something]
print(the_thing)
```

## 速度比较


1. 四种方法之间的对比，后两种方法明显比前两种方法快，且最后一种方法总是最快的。

2. 待判断内容是否在字典中设置的对比

第一种全程if-else判断的情况下，早判断出来程序就会早结束，所以if-else判断的内容顺序是有讲究的
而从字典里提取则没有看出显著的不同
由于使用collections模块中的defaultdict虽然最快，但是会占用较多内存，所以最推荐的是第三种方法，使用if-else配合无默认字典提取方法。


#  python中输入多个数字


## 基础方法 

```python
list1 = [] # 定义一个空字符串
str1 = input('请输入数值,用空格隔开')
list2 = str1.split(' ')# list2用来存储输入字符串,用空格分隔


while list2:
    list1.append(int(list2.pop()))
    
list1.reverse()
print(list1)
```

## map()函数
map() 会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

```python
# 计算平方数
def square(x):
    return x ** 2
print(list(map(square,[1,2,3,4,5])))
print(list(map(lambda x:x**2,[1, 2, 3, 4, 5])))

# 提供两个列表,对相同位置数据相加
print(list(map(lambda x, y:x+y,[1,3,5],[2,4,6])))
```

```python
# 一行实现输出多个数字
print(list(map(int, input().split())))
```

```python
nums = [2,11,7,15]
target = 9
buff_dict = {}
for i in range(len(nums)):
    if 7 in buff_dict:
        print([buff_dict[7], i])
    else:
        buff_dict[target - nums[i]] = i
buff_dict
```
