# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
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

# # 函数

# ## 定义函数

# +
def greet_user():
    """显示简单问候"""
    print('hello')

greet_user()

# -

greet_user.__doc__

type(greet_user)

help(greet_user)


# ### 向函数传递信息

# +
def greet_user(username):
    """显示简单问候"""
    print('hello',username)

greet_user('A')


# -

# ### 形参和实参     
# 前面的username是一个形参--函数完成其工作所需的一项信息;  
#
# 前面的'A'是实参,是调用函数时传递给函数的信息; 
#
# 实参是调用函数时传递给函数的信息.上一个例子,把实参'A'传给了函数,这个值被储存在形参username中

# ## 传递实参

# ### 位置实参
# 调用函数时,python将每一个实参关联到函数定义中的形参,最简单的方式是基于实参顺序,这种关联方式称为位置实参3

# +
def describe_pet(animal_type,pet_name):
    '''显示宠物信息'''
    print('\nI have a',animal_type)
    print('My',animal_type,"'s name is", pet_name.title())
    
describe_pet('hamster','harry')#hamster 仓鼠
describe_pet('dog','willie')


# -

# ### 关键字实参
# 关键字实参是传递给函数的名称-值对,在实参中将名称和值关联起来

# +
def describe_pet(animal_type,pet_name):
    '''显示宠物信息'''
    print('\nI have a',animal_type)
    print('My',animal_type,"'s name is", pet_name.title())

describe_pet(animal_type='hamster',pet_name='harry')#hamster 仓鼠
describe_pet(pet_name='willie',animal_type='dog')


# -

# ### 默认值
# 编写函数时,可为每个形参指定默认值.使用默认值可以简化函数调用, 还可以指出函数典型用法

def describe_pet(pet_name,animal_type='dog'):
    ''' the information of pet'''
    print('\nI have a '+animal_type)
    print('My '+animal_type+"'sname is "+pet_name.title())
describe_pet('willie')


# 在这个函数中,修改了形参的排列顺序. 由于给了animal_type默认值,无需通过实参指定动物类型; 然而,python依然将这个实参视为位置实参,如果函数调用中只包含宠物名字,这个实参会关联到是第一个形参,这就是把pet_name放在列表开头的原因

# ### 避免实参错误

# +
def describe_pet(animal_type,pet_name):
    '''显示宠物信息'''
    print('\nI have a',animal_type)
    print('My',animal_type,"'s name is", pet_name.title())

describe_pet()


# -

# ## 返回值
# 函数并非总是直接显示输出,相反,他可以处理一些数据,并返回一个或一组值.可使用return语句将值返回到函数的代码行.返回值能让程序大部分繁重工作移动到函数中完成

# ### 返回简单值

# +
def get_formatted_name(first_name, last_name):
    '''返回整洁姓名'''
    full_name = first_name + ' ' +last_name
    #resturn full_name.tittle()
    #resturn full_name.title()
    return full_name.title()


    
musician = get_formatted_name('jimi', 'hedrix')
print(musician)


# -

# ### 让实参变成可选的

# +
def get_formatted_name(first_name,last_name,middle_name=''):
    '''返回整洁的姓名'''
    if middle_name:
        full_name = first_name + ' ' + middle_name+' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

print(get_formatted_name('stephen','hawking','willian'))
print(get_formatted_name('albert','einstein'))


# -

# ### 返回字典
# 函数可返回任何类型的值,包括列表和字典等复杂的数据结构.

def build_person(first_name,last_name,age=''):
    '''返回字典，其中包含一个人的信息'''
    person = {'first': first_name, 'last': first_name}
    if age:
        person['age'] = age
    return person
person = build_person('albert','einstein',27)
print(person)


# ## 传递列表
# 将参数传递到函数后,函数能直接访问内容

def greet_users(names):
    '''向列表中每位用户发出问候'''
    for name in names:
        message = 'Hellow, ' + name.title() + '!'
        print(message)
usernames = ['a','b','c']
greet_users(usernames)


# ### 在函数中修改列表

# +
#用函数重新组织
def print_models(unprinted_designs,completed_models):
    '''
    模拟打印每个设计，直到没有打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #模拟根据设计制作打印模型的过程
        print('priinting model:',current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    '''显示打印好的所有模型'''
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case','robot pedant','dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

# -

# ### 禁止函数修改列表
# 有时也要保留原来列表,可用function_name(last_name[:])实现

# ## 传递任意数量的实参

def make_pizza(*toppings): # 创建topping的空元组,并将所有值都装到元组中
    '''打印顾客所有配料'''
    print(toppings)
make_pizza('pepperoni') #  pepperoni 意大利香肠
make_pizza('mushroom', 'green papers', 'extra cheese')


# ### 结合使用位置实参和任意数量的实参

def make_pizza(size,*toppings): # 创建topping的空元组,并将所有值都装到元组中
    '''打印顾客所有配料'''
    print('Making a',str(size)+'-inch pizza with the following toppings:')
    for topping in toppings:
        print('-',topping)
make_pizza(16,'pepperoni') #  pepperoni 意大利香肠
make_pizza(12,'mushroom', 'green papers', 'extra cheese')


# +
def f(*a):
    print(a)

f('a','b')


# +
def g(*a):
    print(*a)

g('a', 'b')


# -

# ### 使用任意数量的关键字实参

#接受任意数量的关键字实参
def build_profile(first,last,**user_info):
    '''创建一个字典,包含我们知道的用户的一切'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert','einstein',
location = 'princeton'
,field ='physics')
print(user_profile)

# ## Higher-Order Functions
# A function that takes a function as argument or returns a function as
# the result is a higher-order function.

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted(fruits, key = len) # Any one-argument function can be used as the key.

# ##  lambda函数

f = lambda x :x*2
f(2)

(lambda x :x*2)(2)

my_functions = [(lambda x : x**2), (lambda x : x**3)]
my_functions[0](3)

f = lambda *x:print(x)
f(1,2,3,4)

lisst1 = [1,4,5,6,7,8]
a = list(filter(lambda x :(x%2 == 0),lisst1))
print(a)

max_ = lambda a,b:a if (a>b) else b
max_(2,3)

# ## map 函数
# map() 会根据提供的函数对指定序列做映射。
#
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

help(map)


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

# ## reduce 函数
# - reduce接受两个参数,即reduce(func, seq)
# - 第一个参数func是一个二元函数(接受两个值作为输入)
# - seq 是一个序列
# - reduce()将第一次从seq序列中取前两个元素,给函数func调用,得到一个中间结果,再将该结果和seq的下一个元素给func,如此反复,直到seq所有元素被遍历完

# +
# 导入reduce
from functools import reduce

# 计算阶乘
reduce(lambda x, y: x * y, range(1, 10))

# -

# ## Filter()函数
# - filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
# - filter(function, iterable)

# 挑出列表中所有奇数
list(filter(lambda x:x&1,[0,1,2,3,4,5,6]))


# 删除 None 或者空字符串
def is_not_empty(s):
    return s and len(s.strip()) > 0
list(filter(is_not_empty, ['test', None, '', 'str', '  ', 'END']))


# ## 将函数保存到模块中

# 导入整个模块
# ```python
# import pizza
# pizza.function
# ```
# 导入特定函数
# ```python
# from module_name import function_name
# from module_name import function0,function_name1
# ```
# 使用as指定别名
# ```python
# import matplotlib.pyplot as plt
# ```
# 导入所有函数
# ```python
# from pizza import *
# ```
# 无需使用.表示方法

# ## 函数装饰器
# 形如
# ```python
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         # Do something before function called
#         ans = func(*args, **kwargs)
#         # Do something after function called
#         return ans
#     return wrapper
# ```

# ### 在python里函数和其他东西一样都是对象

# +
def my_fun(a):
    print(a)

a = my_fun
a
# -

a.__class__

a.__name__


# +
def my_print():
    print("function_run")

def f(function):
    return function

f(my_print).__name__
# -

f(my_print)()

# +
import random

# 返回一个0到1的浮点数
def float_random():
    return random.random()

def a_decorator(func):
    '''调用func'''
    def wrapper():
        return round(func(),3)
    return wrapper

f = a_decorator(float_random)
f()
# -

f.__name__

# ### 使用装饰器

# #### 生成3位随机数

# +
import random

# 返回一个0到1的浮点数
def a_decorator(func):
    '''调用func'''
    def wrapper():
        return round(func(),3)
    return wrapper

@a_decorator # 装饰器,完全等价于f = a_decorator(float_random)
def float_random():
    return random.random()



float_random.__name__
# -

float_random()


# #### 打印函数日志

# +
def logger(func):
    def wrapper(*args, **kw):
        print('我准备计算:{}函数了'.format(func.__name__))
        func(*args, **kw) # 执行函数
        print('啊哈,计算完了')
    return wrapper

@logger
def add(x,y):
    print('{}+{}={}'.format(x, y, x+y))
    
add(200,50)

# +
# 计时器
import time

def timer(func):
    '''计时器'''
    def wrapper(*args,**kw):
        t1 = time.time()
        func(*args,**kw)
        t2 = time.time()
        
        # 计算时长
        cost_time = t2 - t1
        print('花费时间:{}秒'.format(cost_time))
    return wrapper
 
@timer
def sleep(sleep_time):
    time.sleep(sleep_time)

sleep(2)


# -

# #### 多次调用函数
# [原文](https://zhuanlan.zhihu.com/p/27382232)

# +
def repeat(n):
    def repeat_n(func):
        def wrapper(*args,**kwargs):
            for i in range(n):
                func(*args,**kwargs)
        return wrapper
    return repeat_n


@repeat(3)
def f():
    print('hello world')

f()
# -

# 到这里，如果你已经明白了装饰器的原理，你可能会意识到一个问题：
#
# 既然被装饰的函数已经是新的函数，那它的元属性岂不是也不见了？
#
# 没错，如果我们对上述例子进行检查，会发现被装饰过的f函数，它的元属性都变成了wrapper函数(装饰器最终返回的那个函数)的信息。比如

f.__name__

# 这个问题在实际工程中，可能会是个坑。所以python标准库的functools包提供了一个解决办法，用来消除这个副作用。我们可以这样改写上面的例子：

from functools import wraps # 引入wrap装饰器方法
help(wraps)

# +
from functools import wraps # 引入wrap装饰器方法

def repeat(n):
    def repeat_n(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for i in range(n):
                func(*args,**kwargs)
        return wrapper
    return repeat_n


@repeat(3)
def f():
    print('hello world')

f()
f.__name__


# -

# ### 进阶用法：带参数的函数装饰器
# [参考 Python编程时光](https://mp.weixin.qq.com/s?__biz=MzU4OTUwMDE1Mw==&mid=2247483801&idx=1&sn=10ce0416ecf4c370b3d5db2821bec9e0&chksm=fdcdda0fcaba5319cfbe6f5996cc5b85cbdc0c900f457d387dfbb8a3a90ec919744843149aa3)

# +
# 根据国籍,说出问候的话
def say_hello(country):
    def wrapper(func):
        def deco(*args, **kwargs):
            if country == 'china':
                print('你好')
            elif country == 'america':
                print('hello.')
            else:
                return
            func(*args,**kwargs)
        return deco
    return wrapper


@say_hello('china')
def to_american():
    print('我来自中国')

@say_hello('america')
def to_chinese():
    print('I am from America.')



to_american()
print('------')
to_chinese()
