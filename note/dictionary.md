
# 字典

## 创建字典


```python
y = {'x':'a', 2:'b'}
print(y['x'])
print(y[2])
```

    a
    b
    

### 用zip函数


```python
help(zip)
```

    Help on class zip in module builtins:
    
    class zip(object)
     |  zip(iter1 [,iter2 [...]]) --> zip object
     |  
     |  Return a zip object whose .__next__() method returns a tuple where
     |  the i-th element comes from the i-th iterable argument.  The .__next__()
     |  method continues until the shortest iterable in the argument sequence
     |  is exhausted and then it raises StopIteration.
     |  
     |  Methods defined here:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __next__(self, /)
     |      Implement next(self).
     |  
     |  __reduce__(...)
     |      Return state information for pickling.
    
    


```python
name = ['a','b']
age = [18,19]
zip(name,age)
```




    <zip at 0x1b2b1b88248>




```python
# 先转化为列表
_ = list(zip(name,age))
```


```python
# 再转化为字典
dict(_)
```




    {'a': 18, 'b': 19}



### formkeys 函数


```python
help(dict.fromkeys)
```

    Help on built-in function fromkeys:
    
    fromkeys(iterable, value=None, /) method of builtins.type instance
        Returns a new dict with keys from iterable and values equal to value.
    
    


```python
a = ['a','b','c']
dict.fromkeys(a,0)
```




    {'a': 0, 'b': 0, 'c': 0}



### 推导式


```python
roots={x**2:x for x in range(5,0,-1)}
roots
```




    {25: 5, 16: 4, 9: 3, 4: 2, 1: 1}



## 使用字典

### 添加键-值对


```python
aim = {'color' :'green','point':5}
print(aim)
aim['x'] = 0
aim['z'] = 25
print(aim)
```

    {'color': 'green', 'point': 5}
    {'color': 'green', 'point': 5, 'x': 0, 'z': 25}
    

### 修改字典中键的值


```python
aim = {'color' :'green','point':5}
print(aim)
aim['color'] =  'yellow'
print(aim)
```

    {'color': 'green', 'point': 5}
    {'color': 'yellow', 'point': 5}
    

### 删除键-值对

#### del 语句


```python
aim = {'color': 'green', 'point': 5, 'x': 0, 'z': 25}
del aim['point']
print(aim)
```

    {'color': 'green', 'x': 0, 'z': 25}
    

#### pop 语句


```python
aim.pop('color')
```




    'green'




```python
aim
```




    {'x': 0, 'z': 25}



删除的键-值对永远消失了

### 由类似对象组成的字典


```python
favorite_lanuages = {
    'jen':'python',
    'sarah':'c',
    'lihua':'ruby',
    'A':'python',
    }
print(favorite_lanuages)
```

    {'jen': 'python', 'sarah': 'c', 'lihua': 'ruby', 'A': 'python'}
    

确定用多行来字典,输入花括号后按回车,在下一行缩进四个空格,指定第一个键-值对

###  get()
Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。

- 参数    
- key -- 字典中要查找的键。
- default -- 如果指定键的值不存在时，返回该默认值值。


```python
help(dict.get)
```

    Help on built-in function get:
    
    get(...) method of builtins.dict instance
        D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
    
    


```python
dict1 = {'Name': 'Zara', 'Age': 27}

print ("Value : %s" %  dict1.get('Age','never'))
print ("Value : %s" %  dict1.get('Sex', "Never"))
```

    Value : 27
    Value : Never
    

### 转化为列表


```python
dict1 = {1:'a', 2:'b'}
dict1.keys()
```




    dict_keys([1, 2])




```python
dict1.values()
```




    dict_values(['a', 'b'])




```python
dict1.items()
```




    dict_items([(1, 'a'), (2, 'b')])



### setdefault() 函数


```python
help(dict.setdefault)
```

    Help on built-in function setdefault:
    
    setdefault(...) method of builtins.dict instance
        D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
    
    


```python
dict_ = {1:'a', 2:'b'}
dict_.setdefault(1,'abc') # 如果键存在,返回键对应的值
```




    'a'




```python
dict_
```




    {1: 'a', 2: 'b'}




```python
dict_.setdefault(3,'abc') # 如果键不存在,创建这个
```




    'abc'




```python
dict_
```




    {1: 'a', 2: 'b', 3: 'abc'}



##  遍历字典


```python
a = {
    'use_name' : 'abc',
    'first' : 'cbs',
    'last' : 'fermi',
    }
for key,value in a.items():
    print('\nkey:' + key)
    print('value:' + value)

for key in sorted(a.keys()):
    print('\nkey:' + key)
for value in sorted(a.values()):
    print('\nvalue:' + value)
```

    
    key:use_name
    value:abc
    
    key:first
    value:cbs
    
    key:last
    value:fermi
    
    key:first
    
    key:last
    
    key:use_name
    
    value:abc
    
    value:cbs
    
    value:fermi
    

## 嵌套

### 字典列表


```python
aliens = []
for alien_number in range(30):
    new = {'color':'green','point':5,'speed':'slow'}
    aliens.append(new)

# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print('...')
print('total number of aliens is '+str(len(aliens)))
```

    {'color': 'green', 'point': 5, 'speed': 'slow'}
    {'color': 'green', 'point': 5, 'speed': 'slow'}
    {'color': 'green', 'point': 5, 'speed': 'slow'}
    {'color': 'green', 'point': 5, 'speed': 'slow'}
    {'color': 'green', 'point': 5, 'speed': 'slow'}
    ...
    total number of aliens is 30
    

### 在字典中储存列表


```python
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
    }
print('you ordered a '+pizza['crust']+'-crust pizza with the foolwing troopings:')

for topping in pizza['toppings']:
    print('\t '+ topping)
```

    you ordered a thick-crust pizza with the foolwing troopings:
    	 mushrooms
    	 extra cheese
    

### 在字典中储存字典


```python
users = {
    'aeinstein':{
       'first':'albert',
       'last':'eistein',
       'location':'princeton',
       },
    'mcuire':{
        'first':'maire',
       'last':'curie',
       'location':'pairs',
       },
    }
for username,user_info in users.items():
    print('\nUser name:'+ username)
    full_name = user_info['first']+' ' + user_info['last']
    location = user_info['location']
    
    print('\tFull name: ' + full_name.title())
    print('\tLocation: '+ location.title())
```

    
    User name:aeinstein
    	Full name: Albert Eistein
    	Location: Princeton
    
    User name:mcuire
    	Full name: Maire Curie
    	Location: Pairs
    
