---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# numpy

```python
import array
a = array.array('i',range(10)) # i 表示为整型
a
```

```python
a[1] = 3
a
```

```python
type(a)
```

```python
a[0] = 0.6
```

## 生成数组


### 由列表转换

```python
import numpy as np

list1 = [1,2,3]
b = np.array(list1)
b,type(b)
```

### 生成都是0的数组

```python
a = np.zeros(10)
a,type(a),a.dtype
```

默认为float64

```python
a = np.zeros(10,dtype=int)
a.dtype
```

### 生成多维数组

```python
a = np.zeros((4,4),dtype=int)
a , type(a)
```

```python
# 可以用ones生成都是1的
a = np.ones((4,4),dtype=int)
a
```

```python
# 生成初始值为任意数的
np.full((3,3), 3.14)
```

```python
# 生成与其他相同大小,数据类型相同的矩阵
a = np.zeros((4,4),dtype=int)
a_ = np.full_like(a,5.6)
b = np.zeros_like(a)
print(a_)
print('-------------')
print(b)
```

```python
# 数据类型也可以改
a = np.zeros((4,4),dtype=int)
###
a = np.full_like(a,5.6,dtype=float)
a
```

### 生成随机数数组

```python
a = np.random.random((2,3))
a
```

```python
# 生成随机数组
a = np.random.randint(1,10,(9,9))
a
```

### 生成单位矩阵

```python
np.eye(10)
```

### 范围取值

```python
np.arange(0,10,2) # 用法与range相同
```

```python
np.linspace(0,1,100) # 均匀取[0,1]的100个 值
```

## 属性


### 秩

```python
x = np.array([[1,2,5],
             [2,4,10]])
x.ndim
```

### 形状

```python
x.shape
```

```python
x.shape = (3,2)
x
```

### 元素个数

```python
x.size
```

### 元素类型

```python
x.dtype
```

### 每个数据所占大小

```python
# 每个数据所占空间大小
x.itemsize
```

### 所占总字节数

```python
x.nbytes
```

### 数组对应列表

```python
x.tolist()
```

```python
x
```

```python
x[np.newaxis,:]
```

```python
x[:2,:]
```

```python
np.linalg.det(x[:2,:])
```

## 数据类型及取值



Data type | Description |
------------- |:------------- |
"bool| Boolean(True or False) stored as a byte|
"int| Default integer type(same as C"long"; normally either"int64"or"int32")|
"intc| Identical to C"int"(normally"int32'mm"or"int64)|
"intp| Integer used for indexing(same as C"ssize_t"; normally either"int32"or"int64)|
"int8|Byte (-128 to 127)|M
"int16| Integer {-32768 to 32767)|
"int32| Integer(-2147483648 to 214748364Z)|
"int64| Integer (-9223372836854775888 to 9223372836854775807)|
"uint8'| Unsigned integer (e to 255)|
uint16| Unsigned integer (e to 65535)|
"uint32'| Unsigned integer (0 to 4294967295)|
uint64| Unsigned integerf(e to 18446744073709551615)|
"float_| Shorthand for"float64.I
"float16'| Half precision float: sign bit,5 bits exponent,18 bits mantissal
"float32"| Single precision float: sign bit,8 bits exponent,23 bits mantissal float64'|Double precision float: sign bit,1l bits exponent,52 bits mantissal
"complex_"| Shorthand for "complex128,I complex64| Complex number, represented by two 32-bit floatsl I* complex128| Complex number, represented by two 64-bit floatsl
complex64|Complex number,represented by two 32-bit floats|
complex128|Complex number,represented by two 64-bit floats



## 访问数组中的元素

```python
a = np.array([[11,12,13],[21,22,23]])
a[0][1]
```

```python
# 最好这样访问
a[0,1]
```

```python
# 数组切片
a[:1][:2], a[:1,:2]
# 第一种方式切片之后再切片无效
```

## 运算


### 与常数运算

```python
a
```

```python
# 与常数运算,将每一位运算
a+10
```

```python
a + np.pi
```

```python
-a
```

```python
a * 10
```

```python
a - 10.0
```

```python
# a+10 等价于函数
np.add(a,10)
```

The following table lists the arithmetic operators implemented in Numpy:

| Operator | Equivalent ufunc | Description |
|----|----|----|
|`+`|`np. add`|Addition(e.g.,`1+1=2`)
|`-`|`np. subtract`|Subtraction(e.g.,`3-2=1)`|
|`-`|`np. negative`|Unary negation (e.g.,`-2`)|
|`*`|`np. multiply`|Multiplication(e.g.,`2*3=6`)|
|`/`|`np. divide`|Division(e.g.,`3/2=1.5`)|
|`//`|`np. floor_divide`|Floor division(e.g.,`3//2=1`)|
|`**`|`np, power`|Exponentiation (e.g.,`2**3=8`)|
|`% `|`np. mod`|Modulus/remainder(e.g.,`9%4=1`)


### 逻辑运算
就是每一个进行运算

```python
a
```

```python
a > 3
```

|Opgrator | Equivalent ufunc | operator | Equivalent ufunc |
|-|-|-|-|
|`==` |` np. equal`|`!=`|`np. not_equal`|
|`<`| `np. less`|`<=`|`np. less_equal`|
|'>'|`np. greater`|`>=`|`np. greater_equal`|

```python
# 判断每一个是否成立
np.all(a>1) 
```

```python
# 判断存在
np.any(a<1)
```

### 数组内置
的运算


#### 求和

```python
a = np.array([[1,2],
             [3,4]])
```

```python
# 对每一列求和
sum(a)
```

```python
# 求全部的和
np.sum(a)
```

```python
# np.sum求一列的值
np.sum(a,axis=0)
```

```python
# np.sum求一行的值
np.sum(a,axis=1)
```

```python
# 效率比较
n = np.random.rand(100000)
%timeit sum(n)
```

```python
%timeit np.sum(n)
```

#### 求最值

```python
np.max(a),np.min(a)
```

### 矩阵运算

```python
x = np.array([1,2,3])
y = np.array([[11,12,13],
              [21,22,23],
              [31,32,33]])
z = np.array([[21,22,99],[11,33,55]])
```

#### 生成对角矩阵

```python
# 一维数组直接构造对角矩阵
np.diag(x)
```

```python
# 矩阵直接输出对角阵
np.diag(y)
```

```python
np.diag(z)
```

#### dot()

```python
help(np.dot(x,y))
```

```python
a = np.array([1,0])
b = np.array([0,1])
```

$$ \vec{a} \cdot \vec{b} = \sum_{i=1}^n a_{i}b_{i} $$ 

```python
# 一维数组, 返回点积
np.dot(a,b)
```

```python
# 多维数组, 返回矩阵乘法
e = np.eye(2,2)
x = np.array([[11,12],[21,22]])
np.dot(e,x)
```

#### 矩阵内积

```python
a,b
```

```python
np.inner(a,b)
```

$$ {A} \cdot {B} = {A} {B}^{T} $$

```python
x = np.array([[2,3,4],[5,6,7]])
y = np.array([[8,9,10],[10,11,2]])
np.inner(x,y)
```

```python
np.dot(x,y.T)
```

## 变形


### 普通变形 

```python
a = np.array([[11,12],
              [21,22],
              [31,32]])
```

```python
a.reshape(2,3)
```

### 矩阵转置

```python
a.T
```

### 排序

```python
a = np.array([[23,4,8,19],
              [2,5,1,0]])
a
```

#### 对每一行排序

```python
# 临时排序
np.sort(a)
```

```python
a
```

```python
# 彻底排序
a.sort()
```

```python
a
```

```python
n = np.random.rand(100000)
%timeit np.sort(n)
```

```python
%timeit n.sort()
```

```python
a = np.array([[12,3,5]
              ,[0,6,2],
              [1,5,8]])
np.sort(a,axis=0) # 同时按照每行第一个数排列行
```

### 拼接

```python
a
```

```python
# 按行拼
np.concatenate([a,a,a])
# con共同 + caten链+ate v → concatenate链接,连锁
```

```python
# 按列拼
np.concatenate([a,a,a],axis=1)
```
