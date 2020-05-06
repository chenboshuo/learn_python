# -*- coding: utf-8 -*-
---
jupyter:
  jupytext:
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

```python
from IPython.core.
```

# 列表
列表索引从0开始而不是从1开始

```python
list1 = ['a', 'b', 'cd', 'ef']
print(list1[0])
print(list1[-1])
```

<!-- #region toc-hr-collapsed=true -->
## 元素处理
<!-- #endregion -->

### 在列表中修改元素

```python
list1 = ['a', 'b', 'c']
list1[0] = '1'
print(list1)
```

<!-- #region toc-hr-collapsed=true -->
### 在列表中添加元素
<!-- #endregion -->

#### 在末尾添加元素

```python
list1 = ['a', 'b', 'c']
list1.append('d')
print(list1)
```

```python
list1 = ['a', 'b', 'c']
list1 += ['a']
print(list1)
```

#### 在列表中插入元素
insert()可以在指定索引值前添加元素

```python
list1 = ['a', 'b', 'c']
list1.insert(0,'1')
print(list1)
```

```python
list1 = ['a', 'b', 'c']
list1.insert(2,'1')
print(list1)
```

#### 按顺序插入元素
Sorting is expensive, so once you have a sorted sequence, it's good to keep it that way.That's way **bisect.insort** was created.

**insort(seq, item)** inserts item into seq so as to keep seq ascending order.

```python
import bisect
import random

SIZE = 7

random.seed()

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
```

<!-- #region toc-hr-collapsed=true -->
### 从列表中删除元素
<!-- #endregion -->

#### 使用del语句
del可删除任意位置的元素,条件是知道其索引

```python
list1 = ['a', 'b', 'c']
del list1[1]
print(list1)
```

#### 使用pop()删除元素

```python
list1 = ['a', 'b', 'c']
print(list1)

poped = list1.pop()# 不填默认是最后一个
print(list1)
print(poped)

poped = list1.pop(0)# 不填默认是最后一个
print(list1)
print(poped)
```

#### 根据值删除函数
如果不知道位置只知道值,可以用remove(),删除元素时仍然可用它的值

```python
list_ = ['a', 'b', 'b','c']
print(list_)

list_.remove('b')
print(list_)
```

#### 过滤函数

```python
l = [0,'',None,1,2,3]
list(filter(bool,l))
```

### 成员运算符

```python
1 in [1,2,3]
```

```python
'1' not in [1,2,3]
```

<!-- #region toc-hr-collapsed=true -->
## 组织列表
<!-- #endregion -->

### 求和

```python
a = [1,1,1,1,1]
sum(a), sum(a,100) # 第二个表示求和初始值为100
```

### 延长列表

```python
a = [1,2]
b = [3,4]
a.extend(b)
a
```

```python
a = [1,2]
b = [3,4]
a += b
a
```

### 使用sort()对列表进行永久排序

```python
list_ = ['a', 'd', 'ab' ,'a1', 'ad', '2', '23']
list_.sort()
print(list_)
```

```python
list_ = ['a', 'd', 'ab' ,'a1', 'ad', '2', '23']
list_.sort(reverse=True) # 进行相反排序
print(list_)
```

### 使用sorted()进行临时排序

```python
list_ = ['a', 'd', 'ab' ,'a1', 'ad', '2', '23']
print(list_)
print(sorted(list_))
print(sorted(list_, reverse=True))
print(list_)
```

```python
fruits = ['grape', 'respberry', 'apple', 'Apple', 'banana']
sorted(fruits)
```

```python
sorted(fruits, reverse=True)
```

```python
sorted(fruits, key=len)
```

### 倒着打印列表

```python
list_ = ['a', 'd', 'ab' ,'a1', 'ad', '2', '23']
print(list_)

list_.reverse()
print(list_)
```

```python
list1=['a', 'b', 'c']
print(list1[::-1]) # 将步长设为负数
```

### 确定列表长度

```python
list_ = ['a', 'd', 'ab' ,'a1', 'ad', '2', '23']
print(len(list_))
```

### 打乱列表

```python
from random import shuffle
mylist = [1,2,3,4,5]
shuffle(mylist)
mylist
```

### 二分搜索
**bisect** is actually an alias for **bisect_right**, and there is a sister function called **bisect_left** .Their difference is apparent only when the neddle compares equal to an item in the list: *bisect_right* return an insertion point after the existing term, and *bisect_left* returns the position of the existing item

```python
import bisect
import sys 

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}     {2}{0:<2d}'

def demo(binsect_fn):
    for needle in reversed(NEEDLES):
        position = binsect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    
    print('DEMO:', bisect_fn.__name__)
    print('haystack -> ', ' '.join('%2d' % n for n in HAYSTACK))
    print('   index -> ', ' '.join('%2d' % n for n in range(0,14)))
    demo(bisect_fn)
```

```python
bisect_fn = bisect.bisect_left

print('DEMO:', bisect_fn.__name__)
print('haystack -> ', ' '.join('%2d' % n for n in HAYSTACK))
print('   index -> ', ' '.join('%2d' % n for n in range(0,14)))
demo(bisect_fn)
```

## 索引错误

```python
list_ = ['a', 'd', 'ab' ,'a1', 'ad', '2', '23']
print(list_[7])
```

## 遍历整个列表

```python
list_ = ['a', 'b', 'c', 'd']
for i in list_:
    print(i)
else:
    print('no break') # 若for或while没有break,执行else
```

```python
costs = [1,2,3,400,5]
for cost in costs:
    print('消费{}元'.format(str(cost).center(10)))
```

```python
# for + enmuerate
list1=['a',True,3.14]
for i, element in enumerate(list1):
    print(i,list1[i])
```

```python
# for + enmuerate
list1=['a',True,3.14]
for i, element in enumerate(list1):
    print(i+1,list1[i])
```

### 忘记缩进

```python
list_ = ['a', 'b', 'c', 'd']
for i in list_:
print(i)
```

### 不必要的缩进

```python
message = 'hello world'
    print(message)
```

### 忘记冒号

```python
list_ = ['a', 'b', 'c', 'd']
for i in list_
    print(i)
```

## 创建数值列表
列表很适合存储数字集合,python提供很多工具处理数字列表;


### 使用range
- range()从第一个值开始数,在到达第二个值之后停止,因此输出不包含第二个值;
- 第一个参数不填视为0
- 使用range时还可以指定步长

```python
for value in range(1,5):
    print(value)
```

```python
for value in range(5):
    print(value)
```

```python
for even_number in range(2, 11, 2):
    print(even_number)
```

### 使用range创建数字列表
可以使用list()直接将range()转化为列表

```python
numbers = list(range(1,6))
print(numbers)
```

```python
# 将前十个整数的平方放到列表中
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
```

```python
# 不使用变量square
squares = []
for value in range(1, 11):
    squares.append(value **2)
print(squares)
```

### 对列表执行的简单运算
使用内置函数可以轻松求和

```python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
```

### 列表解析
列表解析将for循环和新建元素的代码合并为一行;

```python
squares = [value ** 2 for value in range(1, 11)]
'''
首先指定一个列表名;
定义一个表达式,用来生成储存列表的值
编写一个for循环
'''
print(squares)
```

### 创建列表的比较

```python
board = [['_'] * 3 for i in range(3)]
board
```

```python
board[1][2] = 'x'
board
```

```python
weird_board = [['_'] * 3] * 3
weird_board
```

```python
weird_board[1][2] = '0'
weird_board
```

```python
# 上面这个方法的等效代码
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
# The simple row is appended three times to board
```

## 使用列表的一部分
列表的部分元素称为切片


### 切片

```python
a = ['0','1', '2', '3', '4']
a[0:2]
```

```python
# 如果没有指定起始索引,则列表从头开始
a = ['1', '2', '3', '4']
print(a[:3])
print(a[1:])
```

```python
# 输出后三个元素
a = ['1', '2', '3', '4']
print(a[-3:])
```

### 复制切片

```python
a = ['1', '2', '3', '4']
b = a[:]
a.append('5a')
b.append('5b')
print(a)
print(b)
```

```python
# 这样行不通
a = ['1', '2', '3', '4']
b = a
a.append('5a')
b.append('5b')
print(a)
print(b)
```

```python
list1 = [0,[2,3]]
list2 = list1[:]
list1[1][0] = 999
list2
```

```python
id(list2[1]) == id(list1[1])
```

```python
list1 = [0,[2,3]]
list2 = list1.copy()
list1[1][0] = 999
list2
```

### 切片对象
`class slice(start, stop[, step])`

返回一个表示由 range(start, stop, step) 所指定索引集的 slice对象，它让代码可读性、可维护性变好。

```python
a = [0,1,2,3,4,5]
odds = slice(1,5,2)
a[odds],a[1:5:2]
```

### 切片的其他操作

```python
l = list(range(10))
l
```

```python
l[2:5] = [20,30]
l
```

```python
l = list(range(10))
l
```

```python
del l[5:7]
l
```

```python
l = list(range(10))
l
```

```python
l[3::2] = [33,55,77]
```

```python
l[3::2] = [33,55,77,99]
l
```

## 元组
列表适合处理可能变化的数据集,有时需要创建一系列不可修改的元素,不可变的列表称为元组


### 定义元组

```python
a = (200, 50)
print(a[0])
print(a[1])
```

```python
mylist = [1,2]
mylist[0] = 3
mylist
```

```python
# 尝试修改
a = (200, 50)
a[0] = 250
```

### 遍历元组的所有值

```python
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
```

### 修改元组变量

```python
dimensions = (200, 50)
print(dimensions)

dimensions = (220, 50)
print(dimensions)
```

### 元组的封装和解封装

```python
# 封装
mytuple=3,4,5
mytuple
```

```python
# 解封装
x,y,z = mytuple
x+y+z
```

### 元组与括号

```python
a = ()
type(a)
```

```python
a = (1)
type(a),a
```

## 元组的解开

```python
divmod(20,8)
```

```python
t = (20,8)
divmod(t)
```

```python
t = (20,8)
divmod(*t)
```

## 小应用


### 获取文件名

```python
import os
_, filename = os.path.split('../jupyter_note/list.ipynb')
filename
```

### 用*获取多余条目

```python
a, b, rest = range(5)
```

```python
a, b, *rest = range(5)
a, b, rest
```

```python
a, b, *rest = range(2)
a, b, rest
```

## named Tuples
The `collection.nametuple`function is a factory that produces subclass subclasses of tuple enhanced with field names and a class name--which helps debugging

```python
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
City
```

Two parameters are required to create a name tuple: a class name and a list of field name, which can be given as an iterable of strings or as a single space-delimited string.

```python
tokyo = City('Tokyo', 'JP', 36.933, (35.69, 139.69))
tokyo
```

Data must be passed as positional arguments to the constructor(in contrast, the tuple constructor takes a single iterable)

```python
tokyo.population
```

```python
tokyo[1]
```

<!-- #region heading_collapsed=true -->
## 元组,字符串,列表
<!-- #endregion -->

<!-- #region hidden=true -->
函数|元组|字符串|列表||
:-|-|-|-|-|
# +|√|√|√|
\*|√|√|√|
\>\<|√|√|√|
\[index\]|√|√|√|列表可以索引赋值,字符串,元组不可以|
\[::\]|√|√|√|
len|√|√|√|
bool|√|√|√|空字符串元组列表返回False|
count|√|√|√|
index|√|√|√|
replace|×|√|×|replace返回一个新的字符串,原来的不变|
sort| ×|×|√|
reverse| ×| ×|√|字符串不可更改,只能生成新的字符串来反转|
append|×|×|√|
extend|×|×|√|
remove|×|×|√|
pop|×|×|√|
<!-- #endregion -->

# 数组(Arrays)
The list type is flexible and easy to use, but depending on specific requirements, there are better options.

For example, if you need to store 10 million floating-point values, an array is more efficient, because an array does not actually hold full-fledged float objects, but only the packed bytes representing their machine values- just array in C language. On the other hand, if you are constantly adding and 

```python
from array import array # Import the array type
from random import random

floats = array('d', (random() for _ in range(10**7)))
'''
Create an array of double-precision floats (typecode 'd') from any iterable object
-- in this case, a generator expression
'''
floats[-1]
```

```python
fp = open('text_files/floats.bin', 'wb') 
floats.tofile(fp) # Save the array to a binary file
fp.close()

floats2 = array('d') # Create an empty array of doubles
fp = open('text_files/floats.bin', 'rb')
floats2.fromfile(fp, 10**7) # Read 10 million numbers from the binary file
fp.close()
floats2[-1] # Inspect the last number in the array
```

```python
floats ==floats # Verify that the contents of the arrays match
```

A quick experiments show that it takes about 0.1s for `array.fromfile` to load 10 million double-precision floats from a binary file created with `array.tofile`.
That is nearly 60 times faster than reading the numbers from a text file, which also involoves parsing each line with the float built-in.
Saving with `array.tofile` is about 7 times faster than writing one float per line in a text file.

In addition, the size of the binary file with 10 billion doubles is `80,000,000` bytes (8 bites per double, zero overhead),
while the text file has `181,515,739` bytes, for the same data


## Numpy and Scipy


```python
import numpy as np # It's not in the standard library
a = np.arange(12) 
a
```

```python
type(a)
```

```python
a.shape # Inspect the dimensions of the array: this is a one-dimensional, 12-element array
```

```python
a.shape = 3,4 # Change the shape of the array, adding one dimension, the inspecting the result
a
```

```python
a[2] # Get row at index 2
```

```python
a[2][1] 
```

```python
a[2,1] # Get element at the index 2,1
```

```python
a[:,1] # Get the column at index 1
```

```python
a.transpose() # Create a new array by transposing (swapping cloumns with rows)
```

## Deques and Othter Quenes
The `.append` and `.pop` methods make a list unable as a stack or a quene( if you use `.append` and `.pop(0)`, you get LIFO behavior).
But inserting and removing from the left of a list( thre 0-index end) is costly because the entire list must be shifted.

The class `collections.deque` is a thread-safe double-ended queue designed for fast inserting and removing from both ends.
It is also the way to go if you need to keep a list of "last seen irems" or something like that, because a deque can be bounded-- i.e.,created with a maximum length-- and then, when it is full, it discards items from the opposite end when you append new ones.

```python
from collections import deque
dq = deque(range(10), maxlen=10) # The opional maxlen argument sets the maxium number of items allowed in the instance of deque;
                                 # this sets a read-only maxlen instance attribute
dq
```

```python
'''
Rotating with n > 0 takes items from the right end and prepends them to the left;
when n < 0 items are taken from left and appended to the right.
'''
dq.rotate(3)
dq
```

```python
dq.rotate(-4)
dq
```

```python
dq.appendleft(-1)
dq
```

Appending to a deque that is full(len(d) == d.maxlen) deicards items from the other end;

note in teh next line that 0 is dropped.

```python
dq.extend([11, 22, 33])
dq
```

Adding three items to the right pushes out the leftmost `-1`,`1`and `2`

```python
dq.extendleft([10, 20, 30, 40])
dq
```

```python

```
