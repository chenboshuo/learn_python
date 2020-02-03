---
jupyter:
  jupytext:
    formats: ipynb,md,py:light
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

# 字典


## Hashable
An object is hashable if it has a hash value which never changes during its lifetime(it needs a `__hash__` method),
and can be compared to other objects(it needs an `__eq__()` method).

Hashable objects which compare equal must have the same hash value.

The atomic immutable(str, bytes, numeric types) are all hashable.
A frozen set is always hashable, because its elements must be hashable by definition.
A tuple is hashsble only if all its items are hashable

```python
tt = (1,2,(30,40))
hash(tt)
```

```python
tl = (1,2,[30,40])
hash(tl)
```

```python
tf = (1,2, frozenset([30, 40]))
hash(tf)
```

User-defined types are hashable by default because their hash value is their id() and they all compare not equal.

If an object implements a custom `__eq__` that takes into account its internal state,
it may be hashable only if all its attributes are immutable.


## 创建字典

```python
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two':2, 'three':3}
c = dict(zip(['one', 'two', 'three'],[1,2,3]))
d = dict([('two',2),('one',1), ('three',3)])
a == b == c == d
```

```python
y = {'x':'a', 2:'b'}
print(y['x'])
print(y[2])
```

### 用zip函数

```python
help(zip)
```

```python
name = ['a','b']
age = [18,19]
zip(name,age)
```

```python
# 先转化为列表
_ = list(zip(name,age))
```

```python
# 再转化为字典
dict(_)
```

### formkeys 函数

```python
help(dict.fromkeys)
```

```python
a = ['a','b','c']
dict.fromkeys(a,0)
```

### 推导式

```python
roots={x**2:x for x in range(5,0,-1)}
roots
```

## 使用字典


### 添加键-值对

```python
aim = {'color' :'green','point':5}
print(aim)
aim['x'] = 0
aim['z'] = 25
print(aim)
```

### 修改字典中键的值

```python
aim = {'color' :'green','point':5}
print(aim)
aim['color'] =  'yellow'
print(aim)
```

### 删除键-值对


#### del 语句

```python
aim = {'color': 'green', 'point': 5, 'x': 0, 'z': 25}
del aim['point']
print(aim)
```

#### pop 语句

```python
aim.pop('color')
```

```python
aim
```

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

确定用多行来字典,输入花括号后按回车,在下一行缩进四个空格,指定第一个键-值对


###  get()
Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。


- 参数    
- key -- 字典中要查找的键。
- default -- 如果指定键的值不存在时，返回该默认值值。

```python
help(dict.get)
```

```python
dict1 = {'Name': 'Zara', 'Age': 27}

print ("Value : %s" %  dict1.get('Age','never'))
print ("Value : %s" %  dict1.get('Sex', "Never"))
```

### 转化为列表

```python
dict1 = {1:'a', 2:'b'}
dict1.keys()
```

```python
dict1.values()
```

```python
dict1.items()
```

### setdefault() 函数

```python
help(dict.setdefault)
```

```python
dict_ = {1:'a', 2:'b'}
dict_.setdefault(1,'abc') # 如果键存在,返回键对应的值
```

```python
dict_
```

```python
dict_.setdefault(3,'abc') # 如果键不存在,创建这个
```

```python
dict_
```

## Dict Comprehension

```python
dial_codes = [(86,'China'), 
              (91,'India'),
              (1,'United States'), 
              (62, 'Indonestia'),
              (55,'Brizil'),
              (92,'Pakistan'),
              (880, 'Bangladesh'),
              (234,'Nigeria'),
              (7,'Russia'),
              (81, 'Japan'),
             ]
country_code = {country: code for code, country in dial_codes}
country_code
```

```python
{code: country.upper() for country, code in country_code.items() if code < 66}
```

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

## The `__missing__` method


Underlying way mappings deal with missing keys is the aptly named `__missing__` method.
This method is not defined in the `dict` class,
but `dict` is aware of it.
If you subclassdict and provide `__missing__` method,
the standard `dict.__getitem__` will call it whenever a key is not found,
instead of raising `KeyError`

```python
class StrKeyDict0():
    def __init__(self, d):
        self.d = dict(d)
    
    def __getitem__(self,k):
        return self.d[k]
    
    def __mising__(self, key):
        if isinstance(key, str):
            raise KeyError(key) # check wether key is already a str, 
                         # and it's missing, raise KeyError
        return self[str(key)] # Build str from key and look it up
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()
```

```python
d = StrKeyDict0([('2', 'two'),(4,'four')])
d['2']
```

```python
d[4]
```

```python
d[1]
```

```python
d.get(4)
```

```python
d.get(1,'N/A')
```

# 其他字典


## collections.Counter

A mapping that holds an integer count for each key.
Updating an existing keys adds to its count.
This can be used to count instances of hashable objects(keys) or as a multiset
-- a set that can hold several occurances of each element.
Counter implements the `+` and `-` operators to combine tallies, 
and other useful methods such as `most_common([n])`,
which returns an ordered list of tuples with the n most common items and their counts

```python
import collections
ct = collections.Counter('administrator')
ct
```

```python
ct.update('aaaaaaaaaaz')
ct
```

```python
ct.most_common(2)
```

## collections.UserDict
UserDict does not inherit from `dict`, but has an internal dict instance

```python
import collections
class StrKeyDict(collections.UserDict):
    # def __init__(self, d):
    #    self.d = dict(d)
    
    #def __getitem__(self,k):
    #    return self.d[k]
    
    def __mising__(self, key):
        if isinstance(key, str):
            raise KeyError(key) # check wether key is already a str, 
                         # and it's missing, raise KeyError
        return self[str(key)] # Build str from key and look it up
    # def get(self, key, default=None):
    #    try:
    #        return self[key]
    #    except KeyError:
            return default
    def __contains__(self, key):
        # return key in self.keys() or str(key) in self.keys()
        return str(key) in self.data
    
    def __setitem__(self, key, item):
        self.data[str(key)] = item
```

## Immutable Mappings
Since python 3.3, the types module provides a weapper class called `MappingProxy` Type, which,
given a mapping,
returns a mappingproxy instance that is a read-only mapping dynaic view of the original mapping.
This means that updates to the original mapping can be seen in the `mappingproxy`, 
but change cannot be made through it

```python
from types import MappingProxyType
d = {1:'A'}
d
```

```python
d_proxy = MappingProxyType(d)
d_proxy
```

```python
d_proxy[1]
```

```python
d_proxy[2] = 'B'
```

```python
d_proxy[1] = 'c'
```

```python

```
