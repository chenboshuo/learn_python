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

# # if 语句

 y = ['audi','bmw','subaru','toyota']
for a in y:
    if a == 'bmw':
       print(a.upper())
    else:
       print(a.title())

# 不像C++，我们在Python中没有?:，但我们有这个：
# ```python
# [on true] if [expression] else [on false]
# ```

a,b = 2, 3
min = a if a<b else b
print(min)

# ## 条件测试

car = 'bmw'
print(car == 'bmw')

# pyrhon 检查相等时区分大小写
car = 'bmw'
print(car == 'BMW')

# 条件语句中包含各种数学比较
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)
print(age != 21) # 不等于

# ### 检查多个条件

18 > 17 and 19 > 21

18 > 17 or 19 > 21

# ### 检查特定值是否在列表中

n = ['a', 'b', 'c', 'd']
'a' in n

n = ['a', 'b', 'c', 'd']
'e' in n

n = ['a', 'b', 'c', 'd']
i = 'e'
if i not in n:
    print(i,'not in',n)

# ##  if 语句

# ### 简单if语句

age = 19
if age >= 18:
    print('you are old enough to vote')

# ### if-else 语句

age = 17
if age >= 18:
	print('you are old enough to vote')
else:
	print('23333')

# ### if-elif-else 结构

age = 22
a = 'you admission cost is '
if age<4:
    print(a + '$0')
elif age<8:
    print(a + '$5')
else :
    print(a + '$10')

# ### 确定列表是否为空

zs = []
if zs:
    for z in zs:
        print('adding ' + z +'.')
    print('we finish it')
else:
    print('404')
