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

#  类


## 创建和使用类

```python
class Dog(): # 根据约定,首字母大写为类
    '''一次模拟小狗的的简单尝试'''

    def __init__(self, name, age):
        '''初始化属性name和age'''
        self._name = name
        self._age = age

    def sit(self):
        '''模拟小狗被命令时蹲下'''
        print(self._name.title(),'is now sitting.')
        
    def roll_over(self):
        '''模拟小狗被命令打滚'''
        print(self._name.title(),'rolled over')

my_dog = Dog('while',6)
print("my dog's name is",my_dog._name.title()+'.')
print('my dog is',str(my_dog._age),'years old.')
my_dog.sit()
my_dog.roll_over()
your_dog = Dog('lucy',3)
your_dog.sit()
```

`__init()__`是个特殊的方法,当你根据Dog类创建实例时,python都会自动运行它

这里self包含三个形参,self,name,age.形参self必不可少,必须位于其他形参前面.python调用__init__()的方法创建Dog类时,将自动传入实参self, 每个与类相关联的方法调用都自动传递实参self,它是一个指向实例本身的引用,让实例能访问类中的属性和方法.我们创建Dog实例时,python调用Dog类的方法__init__()方法,通过实参Dog()传递名字和年龄;self将自动传递,我们不需要传递它.

 `__init()__`中的变量都有前缀self,以self为前缀的变量可以供类中所有方法调用,我们还可以通过类的任何实例访问这些变量


名称前的单下划线（如：`_shahriar`）

程序员使用名称前的单下划线，用于指定该名称属性为“私有”。这有点类似于惯例，为了使其他人（或你自己）使用这些代码时将会知道以`_`开头的名称只供内部使用。正如Python文档中所述：

以下划线`_`为前缀的名称（如`_spam`）应该被视为API中非公开的部分（不管是函数、方法还是数据成员）。此时，应该将它们看作是一种实现细节，在修改它们时无需对外部通知。

正如上面所说，这确实类似一种惯例，因为它对解释器来说确实有一定的意义，如果你写了代码`from <模块/包名> import *`，那么以`_`开头的名称都不会被导入，除非模块或包中的`__all__`列表显式地包含了它们。了解更多请查看[Importing * in Python](http://shahriar.svbtle.com/importing-star-in-python)。

```python
class Dog(): # 根据约定,首字母大写为类
    '''一次模拟小狗的的简单尝试'''

    def __init__(self, name, age):
        '''初始化属性name和age'''
        self._name = name
        self._age = age

    def name(self):
        return self._name
    
my_dog = Dog('while',6)
my_dog.name()
```

```python
class Dog(): # 根据约定,首字母大写为类
    '''一次模拟小狗的的简单尝试'''

    def __init__(self, name, age):
        '''初始化属性name和age'''
        self._name = name
        self._age = age
    
    @property # 这样省略括号访问
    def name(self):
        return self._name
    
my_dog = Dog('while',6)
my_dog.name
```

### 根据类创建实例


#### 1.访问属性


访问实例的属性,用句点表示法
- my_dog.name


#### 调用方法


点名实例名称和调用方法,用句点分隔

my_dog.set()


### 给属性指定默认值

```python
class Car():
    '''一次模拟汽车的简单尝试'''

    def __init__(self,make,model,year):
        '''初始化汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   ###### 1 ########
        # odom 里程表

    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year)+' ' + self.make +' '+self.model
        return long_name.title()
    def read_odometer(self):
        '''打印一条汽车里程的消息'''
        print('this car has',str(self.odometer_reading),'miles on it')
    def update_odometer(self,mileage):
        '''
        将里程表读数改为指定值
        禁止里程表往回调
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you can\'t roll back an odometer')
    def increment_odometer(self,miles):
        '''将里程表读数增加指定量'''
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print('you can\'t roll back an odometer')
    def fill_gas_tank(self):
        print('done')

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())


my_new_car.increment_odometer(100)
my_new_car.read_odometer()
my_new_car.increment_odometer(-5)
my_new_car.read_odometer()
```

在1处初始化里程表的里程数为0


### 修改属性的值


#### 直接修改属性的值

```python
my_new_car.odometer_reading = 23       
my_new_car.read_odometer()
```

可以用句点表示法设置属性的值


#### 通过方法修改属性的值

```python
my_new_car.update_odometer(25)
my_new_car.read_odometer()
my_new_car.update_odometer(2)
my_new_car.read_odometer()
my_new_car.update_odometer(120)
my_new_car.read_odometer()
```

##  继承
一个类继承另一个类的时候,自动获取原来类的属性和方法,原来的类称为父类,新的类成为子类,子类继承所有属性和方法,同时定义自己的属性和方法

```python
class ElectricCar(Car):
    '''电动车的独到之处'''

    def __init__(self,make,model,year):
        '''
        初始化父类的属性,在初始化电动汽车的特有属性
        '''
        super().__init__(make,model,year)
        


my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
```

- 定义子类时,父类必须包含在括号中

super()是个特殊函数,帮助python将父类和子类关联起来, 这行代码让python调用父类的__init__(),让子类包含父类的所有属性,父类也被称为超类(superclass),所以函数名为super


### 重写父类的方法

```python
class ElectricCar(Car):
    '''电动车的独到之处'''

    def __init__(self,make,model,year):
        '''
        初始化父类的属性,在初始化电动汽车的特有属性
        '''
        super().__init__(make,model,year)
        
    
    def fill_gas_tank(self):
        '''电动车没有油箱'''
        print('this car doesn\'t need a gas tank')


my_tesla = ElectricCar('tesla','model s',2016)
my_tesla.fill_gas_tank()       
```

###  将实例用作属性
    当属性和方法越来越长时,可能将类的一部分提取出来.你可以将大类分成多个协同工作的小类

```python
class Battery():
    '''一次模拟电动车电瓶的简单尝试'''
    
    def __init__(self, battery_size=70):
        '''初始化电瓶的属性'''
        self.battery_size = battery_size
    
    def describe_battery(self):
        '''的打印一条描述电瓶容量的信息'''
        print('This car has a',str(self.battery_size)+'-kwhbattery')
  

class ElectricCar(Car):
    '''电动车的独到之处'''

    def __init__(self,make,model,year):
        '''
        初始化父类的属性,在初始化电动汽车的特有属性
        '''
        super().__init__(make,model,year)
#         self.battery_size = 70
        self.battery = Battery()   #######  1  #############
        
    '''一开始的结构是这样
    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print('This car has a',str(self.battery_size)+'-kwhbattery')
    '''
    def fill_gas_tank(self):
        '''电动车没有油箱'''
        print('this car doesn\'t need a gas tank')

my_tesla = ElectricCar('tesla','model s',2016)
my_tesla.battery.describe_battery()
```

## 导入类
<code>
 from car import Car,ElectricCat
 import car # 导入整个模块
 from car import * # 导入所有类
</code>


## 9.5 python 标准库


### OrderedDict 类
collections的OrderedDict类创建字典并记录了我键值对的添加顺序

```python
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jens'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'

for name, language in favorite_languages.items():
    print(name.title(),"'s favorite language is'",language.title())
```

## 类编码风格
- 类名采用驼峰命名法,类名中每个单词首字母大写,不使用下划线. 实例名和模块名都采用小写格式,单词之间加上下划线.
- 对于每个类,都紧跟类定义后面包含一个文档字符串. 这种文档字符串简要地描述类的功能, 并遵循编写函数文档字符串时采用的格式约定. 每个模块也应包含一个文档字符串,对于其中的类可以用于做什么进行描述.
- 可使用空行组织代码, 但不要滥用. 在类中,可用一个空格分隔方法;在模块中,用两个空行分隔类.
- 需要同时导入标准库中的模块时,先编写标准库中的import,再添加一个空行,编写导入自己编写的模块的import语句.
