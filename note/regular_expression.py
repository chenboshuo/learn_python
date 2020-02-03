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

# # 导入

# 正则表达式可以帮我们判断某个字符串是否符合某一个模式，其次正则表达式可以帮我们提取某个字符串中的重要部分，做子字符串的提取。今天简单的给大家讲解几个正则表达式的特殊字符—— “^”、“.”、“*”，并且用实例进行演示，让大家对正则表达式有个初步的了解。

#   1、正则表达式在Python中有个专门的库叫re模块，首先进行导入模块。再定义一个字符串str，然后定义一个正则表达式匹配规则regex。

#   2、“^d”代表的意思是以d元素开头的任意一个字符串，也就是说只要是以d开头的字符串，后面的元素不论是什么，都是符合规则的，总之必须要以d开头。

#  3、“.” 较为常用，其代表的意思是任意字符，其表示的范围非常广，可以接任意字符，不论是中英文，还是下划线之类的特殊字符，都是可以代表的。举个栗子，正则表达式“^d.”就是代表以d开头的字符串，b后边接任意字符都可以。

#  4、“*” 也十分常用，其代表的意思是前面的字符可以重复任意多遍，可以是0次，1次，2次等任意多次。

#   5、了解好这几个特殊字符的用法之后，接下来通过代码简单的感受一下。如下图所示，如果匹配成功，则返回yes；如果没有匹配成功，则不返回任何东西。

# +
import re
string = 'dedc1234'
regex_str = '^d.*'
'''
“^d”代表的意思是以d元素开头的任意一个字符串，
也就是说只要是以d开头的字符串，后面的元素不论是什么，
都是符合规则的，总之必须要以d开头。

“.” 较为常用，其代表的意思是任意字符，
其表示的范围非常广，可以接任意字符，不论是中英文，
还是下划线之类的特殊字符，都是可以代表的。
举个栗子，正则表达式“^d.”就是代表以d开头的字符串，b后边接任意字符都可以。

“*” 也十分常用，其代表的意思是前面的字符可以重复任意多遍，可以是0次，1次，2次等任意多次。
'''
match_obj = re.match(regex_str, string)

if match_obj:
    print('yes')
else:
    print('no')

# +
import re
string = 'aedc1234 dedc1234'
regex_str = '^d.*'

match_obj = re.match(regex_str, string)

if match_obj:
    print('yes')
else:
    print('no')
# -

# 特殊字符“$”代表的意思是结尾字符。举个栗子，正则表达式“3$”，表示匹配以3为结尾的字符串。代码演示如下图所示。

# +
import re
string = 'aedc1234 dedc123'
regex_str = '.*3$'
'''
代表以3结尾的任意字符的字符串
'''
match_obj = re.match(regex_str, string)

if match_obj:
    print('yes')
else:
    print('no')
