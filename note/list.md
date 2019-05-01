
# 列表
列表索引从0开始而不是从1开始


```python
list1 = ['a', 'b', 'cd', 'ef']
print(list1[0])
print(list1[-1])
```

    a
    ef
    

## 元素处理

### 在列表中修改元素


```python
list1 = ['a', 'b', 'c']
list1[0] = '1'
print(list1)
```

    ['1', 'b', 'c']
    

### 在列表中添加元素

#### 在末尾添加元素


```python
list1 = ['a', 'b', 'c']
list1.append('d')
print(list1)
```

    ['a', 'b', 'c', 'd']
    


```python
list1 = ['a', 'b', 'c']
list1 += ['a']
print(list1)
```

    ['a', 'b', 'c', 'a']
    

#### 在列表中插入元素
insert()可以在指定索引值前添加元素


```python
list1 = ['a', 'b', 'c']
list1.insert(0,'1')
print(list1)
```

    ['1', 'a', 'b', 'c']
    


```python
list1 = ['a', 'b', 'c']
list1.insert(2,'1')
print(list1)
```

    ['a', 'b', '1', 'c']
    

### 从列表中删除元素

#### 使用del语句
del可删除任意位置的元素,条件是知道其索引


```python
list1 = ['a', 'b', 'c']
del list1[1]
print(list1)
```

    ['a', 'c']
    

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

    ['a', 'b', 'c']
    ['a', 'b']
    c
    ['b']
    a
    

#### 根据值删除函数
如果不知道位置只知道值,可以用remove(),删除元素时仍然可用它的值


```python
list_ = ['a', 'b', 'b','c']
print(list_)

list_.remove('b')
print(list_)
```

    ['a', 'b', 'b', 'c']
    ['a', 'b', 'c']
    

### 成员运算符


```python
1 in [1,2,3]
```




    True




```python
'1' not in [1,2,3]
```




    True



## 组织列表

### 延长列表


```python
a = [1,2]
b = [3,4]
a.extend(b)
a
```




    [1, 2, 3, 4]




```python
a = [1,2]
b = [3,4]
a += b
a
```




    [1, 2, 3, 4]



### 使用sort()对列表进行永久排序


```python
list_ = ['a', 'd', 'ab' ,'a1', 'ad', '2', '23']
list_.sort()
print(list_)
```

    ['2', '23', 'a', 'a1', 'ab', 'ad', 'd']
    


```python
list_ = ['a', 'd', 'ab' ,'a1', 'ad', '2', '23']
list_.sort(reverse=True) # 进行相反排序
print(list_)
```

    ['d', 'ad', 'ab', 'a1', 'a', '23', '2']
    

### 使用sorted()进行临时排序


```python
list_ = ['a', 'd', 'ab' ,'a1', 'ad', '2', '23']
print(list_)
print(sorted(list_))
print(sorted(list_, reverse=True))
print(list_)
```

    ['a', 'd', 'ab', 'a1', 'ad', '2', '23']
    ['2', '23', 'a', 'a1', 'ab', 'ad', 'd']
    ['d', 'ad', 'ab', 'a1', 'a', '23', '2']
    ['a', 'd', 'ab', 'a1', 'ad', '2', '23']
    

### 倒着打印列表


```python
list_ = ['a', 'd', 'ab' ,'a1', 'ad', '2', '23']
print(list_)

list_.reverse()
print(list_)
```

    ['a', 'd', 'ab', 'a1', 'ad', '2', '23']
    ['23', '2', 'ad', 'a1', 'ab', 'd', 'a']
    


```python
list1=['a', 'b', 'c']
print(list1[::-1]) # 将步长设为负数
```

    ['c', 'b', 'a']
    

### 确定列表长度


```python
list_ = ['a', 'd', 'ab' ,'a1', 'ad', '2', '23']
print(len(list_))
```

    7
    

### 打乱列表


```python
from random import shuffle
mylist = [1,2,3,4,5]
shuffle(mylist)
mylist
```




    [3, 1, 5, 2, 4]



## 索引错误


```python
list_ = ['a', 'd', 'ab' ,'a1', 'ad', '2', '23']
print(list_[7])
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-28-7561fdd6ac68> in <module>()
          1 list_ = ['a', 'd', 'ab' ,'a1', 'ad', '2', '23']
    ----> 2 print(list_[7])
    

    IndexError: list index out of range


## 遍历整个列表


```python
list_ = ['a', 'b', 'c', 'd']
for i in list_:
    print(i)
else:
    print('no break') # 若for或while没有break,执行else
```

    a
    b
    c
    d
    no break
    


```python
costs = [1,2,3,400,5]
for cost in costs:
    print('消费{}元'.format(str(cost).center(10)))
```

    消费    1     元
    消费    2     元
    消费    3     元
    消费   400    元
    消费    5     元
    


```python
# for + enmuerate
list1=['a',True,3.14]
for i, element in enumerate(list1):
    print(i,list1[i])
```

    0 a
    1 True
    2 3.14
    


```python
# for + enmuerate
list1=['a',True,3.14]
for i, element in enumerate(list1):
    print(i+1,list1[i])
```

    1 a
    2 True
    3 3.14
    

### 忘记缩进


```python
list_ = ['a', 'b', 'c', 'd']
for i in list_:
print(i)
```


      File "<ipython-input-32-36b5a2787787>", line 3
        print(i)
            ^
    IndentationError: expected an indented block
    


### 不必要的缩进


```python
message = 'hello world'
    print(message)
```


      File "<ipython-input-33-6b39e7ddebfc>", line 2
        print(message)
        ^
    IndentationError: unexpected indent
    


### 忘记冒号


```python
list_ = ['a', 'b', 'c', 'd']
for i in list_
    print(i)
```


      File "<ipython-input-34-e3e92d8da34e>", line 2
        for i in list_
                      ^
    SyntaxError: invalid syntax
    


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

    1
    2
    3
    4
    


```python
for value in range(5):
    print(value)
```

    0
    1
    2
    3
    4
    


```python
for even_number in range(2, 11, 2):
    print(even_number)
```

    2
    4
    6
    8
    10
    

### 使用range创建数字列表
可以使用list()直接将range()转化为列表


```python
numbers = list(range(1,6))
print(numbers)
```

    [1, 2, 3, 4, 5]
    


```python
# 将前十个整数的平方放到列表中
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
```

    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    


```python
# 不使用变量square
squares = []
for value in range(1, 11):
    squares.append(value **2)
print(squares)
```

    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    

### 对列表执行的简单运算
使用内置函数可以轻松求和


```python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
```

    0
    9
    45
    

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

    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    

## 使用列表的一部分
列表的部分元素称为切片

### 切片


```python
a = ['1', '2', '3', '4']
print(a[0:2])
```

    ['1', '2']
    


```python
# 如果没有指定起始索引,则列表从头开始
a = ['1', '2', '3', '4']
print(a[:3])
print(a[1:])
```

    ['1', '2', '3']
    ['2', '3', '4']
    


```python
# 输出后三个元素
a = ['1', '2', '3', '4']
print(a[-3:])
```

    ['2', '3', '4']
    

### 复制切片


```python
a = ['1', '2', '3', '4']
b = a[:]
a.append('5a')
b.append('5b')
print(a)
print(b)
```

    ['1', '2', '3', '4', '5a']
    ['1', '2', '3', '4', '5b']
    


```python
# 这样行不通
a = ['1', '2', '3', '4']
b = a
a.append('5a')
b.append('5b')
print(a)
print(b)
```

    ['1', '2', '3', '4', '5a', '5b']
    ['1', '2', '3', '4', '5a', '5b']
    


```python
list1 = [0,[2,3]]
list2 = list1[:]
list1[1][0] = 999
list2
```




    [0, [999, 3]]




```python
id(list2[1]) == id(list1[1])
```




    True




```python
list1 = [0,[2,3]]
list2 = list1.copy()
list1[1][0] = 999
list2
```




    [0, [999, 3]]



## 元组
列表适合处理可能变化的数据集,有时需要创建一系列不可修改的元素,不可变的列表称为元组

### 定义元组


```python
a = (200, 50)
print(a[0])
print(a[1])
```

    200
    50
    


```python
mylist = [1,2]
mylist[0] = 3
mylist
```




    [3, 2]




```python
# 尝试修改
a = (200, 50)
a[0] = 250
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-61-f36fac2bccaf> in <module>()
          1 # 尝试修改
          2 a = (200, 50)
    ----> 3 a[0] = 250
    

    TypeError: 'tuple' object does not support item assignment


### 遍历元组的所有值


```python
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
```

    200
    50
    

### 修改元组变量


```python
dimensions = (200, 50)
print(dimensions)

dimensions = (220, 50)
print(dimensions)
```

    (200, 50)
    (220, 50)
    

### 元组的封装和解封装


```python
# 封装
mytuple=3,4,5
mytuple
```




    (3, 4, 5)




```python
# 解封装
x,y,z = mytuple
x+y+z
```




    12



### 元组与括号


```python
a = ()
type(a)
```




    tuple




```python
a = (1)
type(a),a
```




    (int, 1)



## 元组,字符串,列表

函数|元组|字符串|列表||
:-|-|-|-|-|
+|√|√|√|
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


```python

```
