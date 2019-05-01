
# if 语句


```python
 y = ['audi','bmw','subaru','toyota']
for a in y:
    if a == 'bmw':
       print(a.upper())
    else:
       print(a.title())
```

    Audi
    BMW
    Subaru
    Toyota
    

不像C++，我们在Python中没有?:，但我们有这个：
```python
[on true] if [expression] else [on false]
```


```python
a,b = 2, 3
min = a if a<b else b
print(min)
```

    2
    

## 条件测试


```python
car = 'bmw'
print(car == 'bmw')
```

    True
    


```python
# pyrhon 检查相等时区分大小写
car = 'bmw'
print(car == 'BMW')
```

    False
    


```python
# 条件语句中包含各种数学比较
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)
print(age != 21) # 不等于
```

    True
    True
    False
    False
    True
    

### 检查多个条件


```python
18 > 17 and 19 > 21
```




    False




```python
18 > 17 or 19 > 21
```




    True



### 检查特定值是否在列表中


```python
n = ['a', 'b', 'c', 'd']
'a' in n
```




    True




```python
n = ['a', 'b', 'c', 'd']
'e' in n
```




    False




```python
n = ['a', 'b', 'c', 'd']
i = 'e'
if i not in n:
    print(i,'not in',n)
```

    e not in ['a', 'b', 'c', 'd']
    

##  if 语句

### 简单if语句


```python
age = 19
if age >= 18:
    print('you are old enough to vote')
```

    you are old enough to vote
    

### if-else 语句


```python
age = 17
if age >= 18:
	print('you are old enough to vote')
else:
	print('23333')
```

    23333
    

### if-elif-else 结构


```python
age = 22
a = 'you admission cost is '
if age<4:
    print(a + '$0')
elif age<8:
    print(a + '$5')
else :
    print(a + '$10')
```

    you admission cost is $10
    

### 确定列表是否为空


```python
zs = []
if zs:
    for z in zs:
        print('adding ' + z +'.')
    print('we finish it')
else:
    print('404')
```

    404
    
