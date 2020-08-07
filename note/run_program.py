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

# # 运行

print('hello world')


print('hello \nworld')


print('hello \ world')


print('''hello
world''')

print('he said "hello"')

# 循环引用其它对象或引用自全局命名空间的对象的模块，在Python退出时并非完全释放。
#
# 另外，也不会释放C库保留的内存部分。

help(print)

print(1,2,sep='-')

import time
print('123',end='\r')
time.sleep(1)
print('456')

# # 参考 

# -  [Your Guide to the Python print() Function](https://realpython.com/python-print/)
