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

# # 异常 
# 每当python不知所措时,会创建一个异常对象,若没有对异常进行处理,程序停止,返回一个traceback

5/0

try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divided by zero")

# ## else 代码块

# +
print('Give me two numbers, and I\'ll divide them')
print("Enter 'q' to quit")

while True:
    first_number = input('\n first number: ')
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    try:
        answer = int(first_number)/ int(second_number)
    except ZeroDivisionError:
        print('You can\'t divide by 0!')
    else:
        print(answer)
# -

# ## 处理FileNotFoundError

#  filename = 'alice.txt'
#
# with open(filename) as f_obj:
#     contents = f_obj.tead()

# try 语句引发异常,所以放到try里

# +
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.tead()
except FileNotFoundError:
    print('Sorry the file',filename,'does not exist')
# -

# ## assert 断言
# 断言不成立,程序崩溃

age = 18
assert age == 19, 'age不是19'

# ## EOF处理

# ### pyhton 没有EOF

a = input()
while a != EOF:
    print(a)

# # EOF 可以用try实现
# ```python
# while True:
#     try:
#         a = input()
#     except EORError:
#         print('EOF')
# ```


