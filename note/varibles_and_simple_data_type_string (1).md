
# 变量和简单数据

## 变量的命名与使用

1. 变量名只包含字母数字下划线,变量名可以以字母或下划线打头,不能以数字打头
2. 变量名不能包含空格
3. 不能用保留关键字命名

##  字符串


```python
s = '1234567890x'
type(s)
```




    str




```python
str(True)
```




    'True'




```python
s = '123'
s[0]
```




    '1'




```python
s = 'He said : I\'m a string'
print(s)
```

    He said : I'm a string
    


```python
s = '''
123
456
'''
print(s)
```

    
    123
    456
    
    

### 修改字符大小写
title以首字母大写的方式显示每个单词;
upper全部改为大写;   
lower全部改为小写;


```python
name = 'ada lovelace'
#print(name.tittle())
print(name.title())
print(name.upper())
print(name.lower())
print(name.capitalize()) # 首字母大写,其他字母小写
```

    Ada Lovelace
    ADA LOVELACE
    ada lovelace
    Ada lovelace
    

### 合并字符串

ncall：函数运行次数

tottime： 函数的总的运行时间，减去函数中调用子函数的运行时间

第一个percall：percall = tottime / nclall 

cumtime:函数及其所有子函数调整的运行时间，也就是函数开始调用到结束的时间。

第二个percall：percall = cumtime / nclall 

####  '+' 链接


```python
import cProfile
def concat_way1():
   fir = 'Hello' * 1000000
   sec = '极客猴' * 1000000
   result = fir + sec
cProfile.run('concat_way1()')
```

             4 function calls in 0.017 seconds
    
       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.014    0.014    0.014    0.014 <ipython-input-8-8f035c05710e>:2(concat_way1)
            1    0.003    0.003    0.017    0.017 <string>:1(<module>)
            1    0.000    0.000    0.017    0.017 {built-in method builtins.exec}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    
    
    

#### 使用 "%" 运算符连接


```python
import cProfile
def concat_way2():
   fir = 'Hello' * 1000000
   sec = '极客猴' * 1000000
   result = '%s%s' % (fir, sec)
cProfile.run('concat_way2()')
```

             4 function calls in 0.019 seconds
    
       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.016    0.016    0.016    0.016 <ipython-input-9-56fd1f3be12b>:2(concat_way2)
            1    0.002    0.002    0.019    0.019 <string>:1(<module>)
            1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    
    
    

#### 使用format()


```python
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
 
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
 
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的
```

    网站名：菜鸟教程, 地址 www.runoob.com
    网站名：菜鸟教程, 地址 www.runoob.com
    网站名：菜鸟教程, 地址 www.runoob.com
    


```python
# 使用 format() 格式化连接, 隐藏参数位置
def concat_way3():
    str1 = 'Hello' * 1000000
    sec = '极客猴' * 1000000
    result = '{}{}'.format(str1, sec)
cProfile.run('concat_way3()')
```

             5 function calls in 0.021 seconds
    
       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.005    0.005    0.017    0.017 <ipython-input-11-b491d5d993bc>:2(concat_way3)
            1    0.003    0.003    0.021    0.021 <string>:1(<module>)
            1    0.000    0.000    0.021    0.021 {built-in method builtins.exec}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
            1    0.012    0.012    0.012    0.012 {method 'format' of 'str' objects}
    
    
    


```python
# 使用 format() 格式化连接, 指定参数位置
def concat_way4():
   fir = 'Hello' * 1000000
   sec = '极客猴' * 1000000
   result = '{0}{1}'.format(fir, sec)
cProfile.run('concat_way4()')
```

             5 function calls in 0.020 seconds
    
       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.005    0.005    0.016    0.016 <ipython-input-12-b5b83870fad9>:2(concat_way4)
            1    0.003    0.003    0.020    0.020 <string>:1(<module>)
            1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
            1    0.011    0.011    0.011    0.011 {method 'format' of 'str' objects}
    
    
    

#### 使用join()链接


```python
# 使用 join()
def concat_way5():
   fir = 'Hello' * 1000000
   sec = '极客猴' * 1000000
   result = ' '.join([fir,sec])
cProfile.run('concat_way5()')
```

             5 function calls in 0.017 seconds
    
       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.005    0.005    0.013    0.013 <ipython-input-13-65d5b0b0965e>:2(concat_way5)
            1    0.003    0.003    0.017    0.017 <string>:1(<module>)
            1    0.000    0.000    0.017    0.017 {built-in method builtins.exec}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
            1    0.008    0.008    0.008    0.008 {method 'join' of 'str' objects}
    
    
    


```python
print("{:.2f}".format(3.1415926))
# 保留小数点后两位
```

    3.14
    


```python
# 带符号保留小数点后两位
print("{:+.2f}".format(-3.1415926))
```

    -3.14
    

<tbody><tr><th width="10%">数字</th><th width="30%">格式</th><th width="30%">输出
</th><th width="30%">描述</th></tr>
<tr><td> 3.1415926 </td>
    <td> {:.2f} </td>
    <td> 3.14 </td>
    <td> 保留小数点后两位 </td>
</tr>
<tr><td> 3.1415926 </td>
    <td> {:+.2f} </td>
    <td> +3.14 </td>
    <td> 带符号保留小数点后两位 </td>
</tr>
<tr><td> -1 </td>
    <td> {:+.2f} </td>
    <td> -1.00 </td>
    <td> 带符号保留小数点后两位 </td>
</tr>
<tr><td> 2.71828 </td>
    <td> {:.0f} </td>
    <td> 3 </td>
    <td> 不带小数 </td>
</tr>
<tr><td> 5 </td>
    <td> {:0&gt;2d} </td>
    <td> 05 </td>
    <td> 数字补零 (填充左边, 宽度为2) </td>
</tr>
<tr><td> 5 </td>
    <td> {:x&lt;4d} </td>
    <td> 5xxx </td>
    <td> 数字补x (填充右边, 宽度为4) </td>
</tr>
<tr><td> 10 </td>
    <td> {:x&lt;4d} </td>
    <td> 10xx </td>
    <td> 数字补x (填充右边, 宽度为4) </td>
</tr>
<tr><td> 1000000 </td>
    <td> {:,} </td>
    <td> 1,000,000 </td>
    <td> 以逗号分隔的数字格式 </td>
</tr>
<tr><td> 0.25 </td>
    <td> {:.2%} </td>
    <td> 25.00% </td>
    <td> 百分比格式 </td>
</tr>
<tr><td> 1000000000 </td>
    <td> {:.2e} </td>
    <td> 1.00e+09 </td>
    <td> 指数记法 </td>
</tr>
<tr><td> 13 </td>
    <td> {:10d} </td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;13</td>
    <td> 右对齐 (默认, 宽度为10) </td>
</tr>
<tr><td> 13 </td>
    <td> {:&lt;10d} </td>
    <td> 13 </td>
    <td> 左对齐 (宽度为10)</td>
</tr>
<tr><td> 13 </td>
    <td> {:^10d} </td>
    <td> &nbsp;&nbsp;&nbsp;&nbsp;13 </td>
    <td> 中间对齐 (宽度为10) </td>
</tr>
<tr><td> 11 </td>
    <td><pre>'{:b}'.format(11)
'{:d}'.format(11)
'{:o}'.format(11)
'{:x}'.format(11)
'{:#x}'.format(11)
'{:#X}'.format(11)</pre></td>
    <td><pre>1011
11
13
b
0xb
0XB
</pre></td>
    <td> 进制</td>
</tr>
</tbody></table>
<p><span class="marked">^</span>, <span class="marked">&lt;</span>, <span class="marked">&gt;</span> 分别是居中、左对齐、右对齐，后面带宽度， <span class="marked">:</span> 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。</p><p>
<span class="marked">+</span> 表示在正数前显示 <span class="marked">+</span>，负数前显示 <span class="marked">-</span>；<span class="marked">&nbsp;</span> （空格）表示在正数前加空格</p>
<p>b、d、o、x 分别是二进制、十进制、八进制、十六进制。</p>



^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。
'+' 表示在正数前显示 +，负数前显示 -；' '（空格）表示在正数前加空格
b、d、o、x 分别是二进制、十进制、八进制、十六进制。
此外我们可以使用大括号 {} 来转义大括号

### 使用制表符添加空白


```python
print('python')
print('\tpython')
```

    python
    	python
    

###  删除空白
- restrip删除末尾空白;
- lstrip删除开头空白;
- strip删除两边空白


```python
a = '   hello  world              '
print(a)
print(a.rstrip())
print(a.lstrip())
print(a.strip())
```

       hello  world              
       hello  world
    hello  world              
    hello  world
    


```python
# 换成其他符号也可以
a = '....hello....world........'
print(a)
print(a.rstrip('.'))
print(a.lstrip('.'))
print(a.strip('.'))
```

    ....hello....world........
    ....hello....world
    hello....world........
    hello....world
    


```python
a = '....hello....world 23. .. .....'
print(a.rstrip('. 3'))
```

    ....hello....world 2
    


```python
a = '....hello....world 23. .. .....'
print(a.rstrip('. 2'))
```

    ....hello....world 23
    

以上函数删除末尾符号直到末尾不存在符号为止

###  统计字符串大写字母数量


```python
s = 'AbcefG'
count = 0
for i in s:
    if i.isupper():
        count += 1
count
```




    2



###  合并拆分字符串 


```python
s = '1 2 3 4 5'
#s.spilt()
print(s.split())
s2 = 'a,b'
b = s2.split(',')
print(b)
'-'.join(b)
```

    ['1', '2', '3', '4', '5']
    ['a', 'b']
    




    'a-b'



### 替换
replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。


```python
s = 'a a b c d'
s.replace('a','1')
```




    '1 1 b c d'




```python
s = 'a a b c d'
s.replace('a','1',1)
```




    '1 a b c d'



### 查找字符串


```python
s = 'hello world'
s.find('cat')
```




    -1




```python
a = 'asdfghjkla'
a.find('a',2)
```




    9




```python
help(str.find)
```

    Help on method_descriptor:
    
    find(...)
        S.find(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
    
    

find()找不到内容返回-1


```python
s = 'hello world'
s.index('cat')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-27-34e7bd34f307> in <module>()
          1 s = 'hello world'
    ----> 2 s.index('cat')
    

    ValueError: substring not found



```python
s = 'hello world'
s.index('hello')
```




    0




```python
a = 'asdfghjkla'
a.find('a',2)
```




    9




```python
help(str.index)
```

    Help on method_descriptor:
    
    index(...)
        S.index(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found, 
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
    
    

index()找不到内容会报错

### 排版布局(layout)

center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。


```python
s = 'a'
print('*'*30)
s.center(30)
```

    ******************************
    




    '              a               '




```python
s = 'a'
print('*'*30)
s.center(30,'-')
```

    ******************************
    




    '--------------a---------------'




```python
s = 'a'
print('*'*30)
s.ljust(30)
```

    ******************************
    




    'a                             '




```python
s = 'a'
print('*'*30)
s.rjust(30)
```

    ******************************
    




    '                             a'



###  反转字符串


```python
'''
reversing string with special case of slice step param
slice 切片
param 参数
'''

a = 'asdfghjjkl'
print(a[::-1])

'''iterating over string contents in reverse efficiently'''

for char in reversed(a):
    print(char)

'''reversing an integer through type conversion and slicing'''
num = 123456789
print(int(str(num)[::-1]))
```

    lkjjhgfdsa
    l
    k
    j
    j
    h
    g
    f
    d
    s
    a
    987654321
    

### 字符串组成判断与比较


```python
# 判断是否全部为小写字母
s = '1d%a@cb'
s.islower()
```




    True




```python
# 判断是否全部为大写字母
s = '1d%D@cb'
s.isupper()
```




    False




```python
# 判断首字符是否为英文大写
s = 'Hello 1World'
s.istitle()
```




    True




```python
# 字符为十进制或双字节整数
s = 's2gdr'
s.isdecimal()
```




    False




```python
s = 's2.0'
s.isdecimal()
```




    False




```python
s = '2'
s.isdecimal()
```




    True




```python
s = '0b10'
s.isdecimal()
```




    False




```python
# 判断字符串是否为十进制/单字节/双字节整数
s = '0b10'
s.isdigit()
```




    False




```python
# 字符串是否为十进制/单字节/双字节整数/汉字数字
s = '二'
s.isnumeric()
```




    True




```python
# 判断字符串是不是有效标识符(可用来判断变量名是否合法)
s = '_ 1'
s.isidentifier()
```




    False




```python
# 判断字符串是否全部为空格
s = ' 0 '
s.isspace()
```




    False




```python
str1 = 'ab'
str2 = 'abc'
str1 < str2
```




    True




```python
str1 = 'ac'
str2 = 'abc'
str1 > str2
```




    True



###  其他工具


```python
s = '123445'
# s.startwith('1')
s.startswith('1')
```




    True




```python
s = '123445'
s.endswith('1')
```




    False




```python
s='1123112'
s.count('1')
```




    4



isalnum() 方法检测字符串是否由字母和数字组成。


```python
s = ' 1234abv'
s.isalnum()
```




    False




```python
s = '1234abv'
s.isalnum()
```




    True



使用isupper()和islower()方法检查字符春是否全为大写或小写。


```python
'AyuShi'.isupper()
```




    False




```python
'@yu$hi'.islower()
```




    True



像@和$这样的字符既满足大写也满足小写。

Istitle()能告诉我们一个字符串是否为标题格式


```python
'The Corpse Bride'.istitle()
```




    True




```python
'The Corpse 1Bride'.istitle()
```




    True



通过成员运算符‘in’和‘not in’，我们可以确认一个值是否是另一个值的成员。


```python
'me' in 'disappointment'
```




    True




```python
'me' in 'disappointm ent'
```




    False




```python
'us' not in 'disappointment'
```




    True



### 字符串不能干什么

#### 受限的序列

与典型的序列类型相比，字符串不具备列表的如下操作：append()、clear()、copy()、insert()、pop()、remove()，等等。这是为什么呢？

有几个很好理解，即append()、insert()、pop() 和 remove()，它们都是对单个元素的操作，但是，字符串中的单个元素就是单个字符，通常没有任何意义，我们也不会频繁对其做增删操作，所以，字符串没有这几个方法也算合理。

列表的 clear() 方法会清空列表，用来节省内存空间，效果等于anylist[:] = []，但是，奇怪的是，Python 并不支持清空/删除操作。

首先，字符串没有 clear() 方法，其次，它是不可变对象，不支持这种赋值操作anystr[:] = ''，也不支持del anystr[:]操作：


```python
s = 'Hello world'

s[:] = ''
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-59-5b29fea538c7> in <module>()
          1 s = 'Hello world'
          2 
    ----> 3 s[:] = ''
    

    TypeError: 'str' object does not support item assignment


当然，你也别想通过del s来删除字符串，因为变量名 s 只是字符串对象的引用（挖坑，以后写写这个话题），只是一个标签，删除标签并不会直接导致对象实体的消亡。

如此看来，想要手动清空/删除 Python 字符串，似乎是无解。

最后还有一个 copy() 方法，这就是拷贝嘛，可是字符串也没有这个方法。为什么呢？难道拷贝字符串的场景不多么？在这点上，我也没想出个所以然来，搁置疑问。

通过以上几个常用列表操作的比较，我们可以看出字符串这种序列是挺受限的。列表可以看成多节车厢链接成的火车，而字符串感觉就只像多个座椅联排成的长车厢，真是同源不同相啊。

##  数字

### 整数


```python
print(3 ** 2)
```

    9
    

###  浮点数
有时结果包含的位数是不确定的,python寻找一种方式,尽可能精确表示结果


```python
print(0.1 + 0.1)
print(0.2 + 0.1)
print(3 * 0.1)
```

    0.2
    0.30000000000000004
    0.30000000000000004
    


```python
2/3
```




    0.6666666666666666



用除法默认是浮点数


```python
2//3
```




    0



这样输出是整数

### 其他数值也可以数字识别


```python
# 16进制
print(0x10)
# 8进制
print(0o10)
# 2进制
print(0b10)
# 指数
print(1.25e3)
```

    16
    8
    2
    1250.0
    


```python
# 转化
a = int(input('输入十进制数据'))
print('二进制为',bin(a))
print('八进制为',oct(a))
print('十六进制为',hex(a))
```

    输入十进制数据123
    二进制为 0b1111011
    八进制为 0o173
    十六进制为 0x7b
    

###  使用str()避免错误
python无法理解13.在这里,python发现一个int变量,但不知如何解读


```python
age = 13
a = 'My age is ' + age
print(a)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-67-66c3aaa54df2> in <module>()
          1 age = 13
    ----> 2 a = 'My age is ' + age
          3 print(a)
    

    TypeError: must be str, not int



```python
age = 13
a = 'My age is ' + str(age)
print(a)
```

    My age is 13
    

## 数据类型

###  整型 int
python3 int没有长度限制


```python
int('-123')
```




    -123



### 浮点型 float


```python
2/3
```




    0.6666666666666666




```python
10/5
```




    2.0



除法默认是浮点数


```python
2//3 #这样取整
```




    0




```python
1 + 2.0
```




    3.0



### 布尔值 boolean


```python
type(1<2)
```




    bool




```python
(2<1)or(1<2)
```




    True




```python
True +1
```




    2




```python
not (2 < 1)
```




    True




```python
{1,3,2,2}=={1,2,3} #这是一个集合
```




    True



## python之禅


```python
import this
```

    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    
