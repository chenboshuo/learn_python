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

# # 文件

# ## 从文件中读取数据

# ### 读取整个文件

with open('pi_digits.txt') as file_objects:
    contents = file_objects.read()
    print(contents)
print('***********')

# - 函数open()接受一个参数:要打开文件的名称.
# - open('pi_digits.txt')返回一个表示pi_digits.txt的对象,存储到后面的变量中
# - 关键词with在不需要访问文件时将其关闭
# - read()到达文件末尾时返回一个空字符串,这个空字符串显示出来一个空行

with open('text_files\pi_digits.txt') as file_objects:
    contents = file_objects.read()
    print(contents.rstrip())

# - 文件路径用反斜杠'\',也可以使用绝对路径

# ### 逐行读取

# +
filename = 'text_files\pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
# -

# - 文件中,每行末尾都有一个换行符,print又会加上一个换行符

# ### 创建一个包含各行内容的列表
# 使用关键字with()的时候,open()返回的文件对象只在with代码块可用,如果要在代码块之外访问文件内容,可以将各行存储在一个列表中.

# +
filename = 'text_files\pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
# -

# ### 使用文件内容

# +
filename = 'text_files\pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))
# -

# 读取文本文件python全部视为字符串

# ### 圆周率包含你的生日吗

# +
filename = 'text_files\pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input('Enter your birthday , in the form mmddyy: ')
if birthday in pi_string:
    print('Your birthday appears in the first million of pi')
else:
    print('Your birthday does not appear in the first million digits of pi.')
# -

# ## 写入文件

# +
filename = 'text_files\programing.txt'

with open(filename,'w') as file_object:
    file_object.write('I love programing.')
    
with open(filename) as file_object:    
    contents = file_object.read()
    print(contents.rstrip())

# -

# open()的第一个实参是要打开文件的名称,第二个('w')告诉python以写入模式打
#
#
# | 第二个实参 | 模式|
# :- |:-
# 'w'|写入模式
# 'r'|读取模式
# 'a'|附加模式
# 'r+'|能读取和写入文件的模式
#
# - 省略模式实参,python以只读方式打开

# ### 写入多行

# +
filename = 'text_files\programing121.txt'

with open(filename,'w') as file_object:
    file_object.write('I love programing.')
    file_object.write('I love programing.')
    
with open(filename) as file_object:    
    contents = file_object.read()
    print(contents.rstrip())

# -

# 如果要写入多行,需要加上换行符

# ### 分析文本

# +
filename = 'text_files/alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print('Sorry the file',filename,'does not exist')
else:
    words = contents.split()
    num_words = len(words)
    print('The file',filename,'has about',str(num_words),'words')
# -

# ## 存储数据
# 模块json可以将简单的数据转存到文件中

# ### 使用json.dump() ,json.load()

# - json.dump()接受两个实参:要存储的数据和可用于存储的文件对象

# +
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'text_files/numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)

# +
import json

# 读取数据
filename = 'text_files/numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)
# -

# ### 保存和读取用户生成的数据

# +
import json

username = input('What is your name: ')

filename = 'text_files/username.json'
with open(filename,'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back,",username)

# +
'''问候用户'''
import json

filename = 'text_files/username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print('Welcome back,',username)

# +
# 合并两个程序
import json

# 如果以前存储用户名,就加载它
# 否则提示用户存储他
filename = 'text_files/user_name.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input('What is your name: ')

    filename = 'text_files/username.json'
    with open(filename,'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back,",username)
else:
    print('Welcome back,',username)

# +
# 重构

import json

def greet_user():
    '''问候用户,并指出名字'''
    filename = 'text_files/user_name.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input('What is your name: ')

        filename = 'text_files/username.json'
        with open(filename,'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back,",username)
    else:
        print('Welcome back,',username)

greet_user()

# +
# 继续重构
import json

def get_sorted_username():
    '''如果用户存储用户名,就读取它'''
    filename = 'text_files/user_name.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        # username = input('What is your name: ')
        return None
    else:
        return username

def greet_user():
    '''问候用户,并指出名字'''
    username = get_sorted_username()
    if username:
        print('Welcome back,',username)
    else:
        username = input('What is your name: ')

        filename = 'text_files/username.json'
        with open(filename,'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back,",username)
            

greet_user()
# -


