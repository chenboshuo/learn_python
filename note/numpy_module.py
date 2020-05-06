# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,md,py:light
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

# # numpy

import array
a = array.array('i',range(10)) # i 表示为整型
a

a[1] = 3
a

type(a)

a[0] = 0.6

# ## 生成数组

# ### 由列表转换

# +
import numpy as np

list1 = [1,2,3]
b = np.array(list1)
b,type(b)
# -

# ### 生成都是0的数组

a = np.zeros(10)
a,type(a),a.dtype

# 默认为float64

a = np.zeros(10,dtype=int)
a.dtype

# ### 生成多维数组

a = np.zeros((4,4),dtype=int)
a , type(a)

# 可以用ones生成都是1的
a = np.ones((4,4),dtype=int)
a

# 生成初始值为任意数的
np.full((3,3), 3.14)

# 生成与其他相同大小,数据类型相同的矩阵
a = np.zeros((4,4),dtype=int)
a_ = np.full_like(a,5.6)
b = np.zeros_like(a)
print(a_)
print('-------------')
print(b)

# 数据类型也可以改
a = np.zeros((4,4),dtype=int)
###
a = np.full_like(a,5.6,dtype=float)
a

# ### 生成随机数数组

a = np.random.random((2,3))
a

# 生成随机数组
a = np.random.randint(1,10,(9,9))
a

# ### 生成单位矩阵

np.eye(10)

# ### 范围取值

np.arange(0,10,2) # 用法与range相同

np.linspace(0,1,100) # 均匀取[0,1]的100个 值

# ## 属性

# ### 秩

x = np.array([[1,2,5],
             [2,4,10]])
x.ndim

# ### 形状

x.shape

x.shape = (3,2)
x

# ### 元素个数

x.size

# ### 元素类型

x.dtype

# ### 每个数据所占大小

# 每个数据所占空间大小
x.itemsize

# ### 所占总字节数

x.nbytes

# ### 数组对应列表

x.tolist()

x

x[np.newaxis,:]

x[:2,:]

np.linalg.det(x[:2,:])

# ## 数据类型及取值
#

# Data type | Description |
# ------------- |:------------- |
# "bool| Boolean(True or False) stored as a byte|
# "int| Default integer type(same as C"long"; normally either"int64"or"int32")|
# "intc| Identical to C"int"(normally"int32'mm"or"int64)|
# "intp| Integer used for indexing(same as C"ssize_t"; normally either"int32"or"int64)|
# "int8|Byte (-128 to 127)|M
# "int16| Integer {-32768 to 32767)|
# "int32| Integer(-2147483648 to 214748364Z)|
# "int64| Integer (-9223372836854775888 to 9223372836854775807)|
# "uint8'| Unsigned integer (e to 255)|
# uint16| Unsigned integer (e to 65535)|
# "uint32'| Unsigned integer (0 to 4294967295)|
# uint64| Unsigned integerf(e to 18446744073709551615)|
# "float_| Shorthand for"float64.I
# "float16'| Half precision float: sign bit,5 bits exponent,18 bits mantissal
# "float32"| Single precision float: sign bit,8 bits exponent,23 bits mantissal float64'|Double precision float: sign bit,1l bits exponent,52 bits mantissal
# "complex_"| Shorthand for "complex128,I complex64| Complex number, represented by two 32-bit floatsl I* complex128| Complex number, represented by two 64-bit floatsl
# complex64|Complex number,represented by two 32-bit floats|
# complex128|Complex number,represented by two 64-bit floats
#

# ## 访问数组中的元素

a = np.array([[11,12,13],[21,22,23]])
a[0][1]

# 最好这样访问
a[0,1]

# 数组切片
a[:1][:2], a[:1,:2]
# 第一种方式切片之后再切片无效

# ## 运算

# ### 与常数运算

a

# 与常数运算,将每一位运算
a+10

a + np.pi

-a

a * 10

a - 10.0

# a+10 等价于函数
np.add(a,10)

# The following table lists the arithmetic operators implemented in Numpy:
#
# | Operator | Equivalent ufunc | Description |
# |----|----|----|
# |`+`|`np. add`|Addition(e.g.,`1+1=2`)
# |`-`|`np. subtract`|Subtraction(e.g.,`3-2=1)`|
# |`-`|`np. negative`|Unary negation (e.g.,`-2`)|
# |`*`|`np. multiply`|Multiplication(e.g.,`2*3=6`)|
# |`/`|`np. divide`|Division(e.g.,`3/2=1.5`)|
# |`//`|`np. floor_divide`|Floor division(e.g.,`3//2=1`)|
# |`**`|`np, power`|Exponentiation (e.g.,`2**3=8`)|
# |`% `|`np. mod`|Modulus/remainder(e.g.,`9%4=1`)

# ### 逻辑运算
# 就是每一个进行运算

a

a > 3

# |Opgrator | Equivalent ufunc | operator | Equivalent ufunc |
# |-|-|-|-|
# |`==` |` np. equal`|`!=`|`np. not_equal`|
# |`<`| `np. less`|`<=`|`np. less_equal`|
# |'>'|`np. greater`|`>=`|`np. greater_equal`|

# 判断每一个是否成立
np.all(a>1) 

# 判断存在
np.any(a<1)

# ### 数组内置
# 的运算

# #### 求和

a = np.array([[1,2],
             [3,4]])

# 对每一列求和
sum(a)

# 求全部的和
np.sum(a)

# np.sum求一列的值
np.sum(a,axis=0)

# np.sum求一行的值
np.sum(a,axis=1)

# 效率比较
n = np.random.rand(100000)
# %timeit sum(n)

# %timeit np.sum(n)

# #### 求最值

np.max(a),np.min(a)

# ### 矩阵运算

x = np.array([1,2,3])
y = np.array([[11,12,13],
              [21,22,23],
              [31,32,33]])
z = np.array([[21,22,99],[11,33,55]])

# #### 生成对角矩阵

# 一维数组直接构造对角矩阵
np.diag(x)

# 矩阵直接输出对角阵
np.diag(y)

np.diag(z)

# #### dot()

help(np.dot(x,y))

a = np.array([1,0])
b = np.array([0,1])

# $$ \vec{a} \cdot \vec{b} = \sum_{i=1}^n a_{i}b_{i} $$ 

# 一维数组, 返回点积
np.dot(a,b)

# 多维数组, 返回矩阵乘法
e = np.eye(2,2)
x = np.array([[11,12],[21,22]])
np.dot(e,x)

# #### 矩阵内积

a,b

np.inner(a,b)

# $$ {A} \cdot {B} = {A} {B}^{T} $$

x = np.array([[2,3,4],[5,6,7]])
y = np.array([[8,9,10],[10,11,2]])
np.inner(x,y)

np.dot(x,y.T)

# ## 变形

# ### 普通变形 

a = np.array([[11,12],
              [21,22],
              [31,32]])

a.reshape(2,3)

# ### 矩阵转置

a.T

# ### 排序

a = np.array([[23,4,8,19],
              [2,5,1,0]])
a

# #### 对每一行排序

# 临时排序
np.sort(a)

a

# 彻底排序
a.sort()

a

n = np.random.rand(100000)
# %timeit np.sort(n)

# %timeit n.sort()

a = np.array([[12,3,5]
              ,[0,6,2],
              [1,5,8]])
np.sort(a,axis=0) # 同时按照每行第一个数排列行

# ### 拼接

a

# 按行拼
np.concatenate([a,a,a])
# con共同 + caten链+ate v → concatenate链接,连锁

# 按列拼
np.concatenate([a,a,a],axis=1)
