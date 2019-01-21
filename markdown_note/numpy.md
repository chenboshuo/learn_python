
# numpy


```python
import array
a = array.array('i',range(10)) # i 表示为整型
a
```




    array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
a[1] = 3
a
```




    array('i', [0, 3, 2, 3, 4, 5, 6, 7, 8, 9])




```python
type(a)
```




    array.array




```python
a[0] = 0.6
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-7-84902d50a6c7> in <module>
    ----> 1 a[0] = 0.6
    

    TypeError: integer argument expected, got float


## 生成数组

### 由列表转换


```python
import numpy as np

list1 = [1,2,3]
b = np.array(list1)
b,type(b)
```




    (array([1, 2, 3]), numpy.ndarray)



### 生成都是0的数组


```python
a = np.zeros(10)
a,type(a),a.dtype
```




    (array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]),
     numpy.ndarray,
     dtype('float64'))



默认为float64


```python
a = np.zeros(10,dtype=int)
a.dtype
```




    dtype('int32')



### 生成多维数组


```python
a = np.zeros((4,4),dtype=int)
a , type(a)
```




    (array([[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]), numpy.ndarray)




```python
# 可以用ones生成都是1的
a = np.ones((4,4),dtype=int)
a
```




    array([[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]])




```python
# 生成初始值为任意数的
np.full((3,3), 3.14)
```




    array([[3.14, 3.14, 3.14],
           [3.14, 3.14, 3.14],
           [3.14, 3.14, 3.14]])




```python
# 生成与其他相同大小,数据类型相同的矩阵
a = np.zeros((4,4),dtype=int)
a_ = np.full_like(a,5.6)
b = np.zeros_like(a)
print(a_)
print('-------------')
print(b)
```

    [[5 5 5 5]
     [5 5 5 5]
     [5 5 5 5]
     [5 5 5 5]]
    -------------
    [[0 0 0 0]
     [0 0 0 0]
     [0 0 0 0]
     [0 0 0 0]]
    


```python
# 数据类型也可以改
a = np.zeros((4,4),dtype=int)
###
a = np.full_like(a,5.6,dtype=float)
a
```




    array([[5.6, 5.6, 5.6, 5.6],
           [5.6, 5.6, 5.6, 5.6],
           [5.6, 5.6, 5.6, 5.6],
           [5.6, 5.6, 5.6, 5.6]])



### 生成随机数数组


```python
a = np.random.random((2,3))
a
```




    array([[0.72881893, 0.0986384 , 0.42959311],
           [0.07181068, 0.53850421, 0.25193518]])




```python
# 生成随机数组
a = np.random.randint(1,10,(9,9))
a
```




    array([[5, 6, 2, 6, 7, 8, 2, 5, 6],
           [5, 5, 7, 8, 9, 9, 6, 8, 8],
           [4, 4, 9, 4, 8, 1, 9, 8, 1],
           [2, 2, 2, 1, 4, 9, 7, 5, 4],
           [8, 8, 6, 1, 6, 4, 5, 1, 1],
           [8, 2, 4, 3, 9, 8, 6, 9, 2],
           [7, 9, 8, 2, 9, 7, 2, 6, 5],
           [6, 4, 8, 6, 6, 3, 2, 6, 6],
           [9, 5, 5, 2, 7, 2, 7, 1, 3]])



### 生成单位矩阵


```python
np.eye(10)
```




    array([[1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
           [0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
           [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
           [0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
           [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
           [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
           [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]])



## 范围取值


```python
np.arange(0,10,2) # 用法与range相同
```




    array([0, 2, 4, 6, 8])




```python
np.linspace(0,1,100) # 均匀取[0,1]的100个 值
```




    array([0.        , 0.01010101, 0.02020202, 0.03030303, 0.04040404,
           0.05050505, 0.06060606, 0.07070707, 0.08080808, 0.09090909,
           0.1010101 , 0.11111111, 0.12121212, 0.13131313, 0.14141414,
           0.15151515, 0.16161616, 0.17171717, 0.18181818, 0.19191919,
           0.2020202 , 0.21212121, 0.22222222, 0.23232323, 0.24242424,
           0.25252525, 0.26262626, 0.27272727, 0.28282828, 0.29292929,
           0.3030303 , 0.31313131, 0.32323232, 0.33333333, 0.34343434,
           0.35353535, 0.36363636, 0.37373737, 0.38383838, 0.39393939,
           0.4040404 , 0.41414141, 0.42424242, 0.43434343, 0.44444444,
           0.45454545, 0.46464646, 0.47474747, 0.48484848, 0.49494949,
           0.50505051, 0.51515152, 0.52525253, 0.53535354, 0.54545455,
           0.55555556, 0.56565657, 0.57575758, 0.58585859, 0.5959596 ,
           0.60606061, 0.61616162, 0.62626263, 0.63636364, 0.64646465,
           0.65656566, 0.66666667, 0.67676768, 0.68686869, 0.6969697 ,
           0.70707071, 0.71717172, 0.72727273, 0.73737374, 0.74747475,
           0.75757576, 0.76767677, 0.77777778, 0.78787879, 0.7979798 ,
           0.80808081, 0.81818182, 0.82828283, 0.83838384, 0.84848485,
           0.85858586, 0.86868687, 0.87878788, 0.88888889, 0.8989899 ,
           0.90909091, 0.91919192, 0.92929293, 0.93939394, 0.94949495,
           0.95959596, 0.96969697, 0.97979798, 0.98989899, 1.        ])



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




    12




```python
# 最好这样访问
a[0,1]
```




    12




```python
# 数组切片
a[:1][:2], a[:1,:2]
# 第一种方式切片之后再切片无效
```




    (array([[11, 12, 13]]), array([[11, 12]]))



## 数组属性


```python
a = np.array([[11,12,13],
              [21,22,23],
              [31,32,33]])
```


```python
# 维度
a.ndim
```




    2




```python
# shape
a.shape
```




    (3, 3)




```python
# 数据
a.size
```




    9




```python
# 数据类型
a.dtype
```




    dtype('int32')




```python
# 每个数据所占空间大小
a.itemsize
```




    4




```python
# 所占的总字节数
a.nbytes
```




    36



## 运算

### 与常数运算


```python
a
```




    array([[11, 12, 13],
           [21, 22, 23],
           [31, 32, 33]])




```python
# 与常数运算,将每一位运算
a+10
```




    array([[21, 22, 23],
           [31, 32, 33],
           [41, 42, 43]])




```python
a + np.pi
```




    array([[14.14159265, 15.14159265, 16.14159265],
           [24.14159265, 25.14159265, 26.14159265],
           [34.14159265, 35.14159265, 36.14159265]])




```python
-a
```




    array([[-11, -12, -13],
           [-21, -22, -23],
           [-31, -32, -33]])




```python
a * 10
```




    array([[110, 120, 130],
           [210, 220, 230],
           [310, 320, 330]])




```python
a - 10.0
```




    array([[ 1.,  2.,  3.],
           [11., 12., 13.],
           [21., 22., 23.]])




```python
# a+10 等价于函数
np.add(a,10)
```




    array([[21, 22, 23],
           [31, 32, 33],
           [41, 42, 43]])



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




    array([[1, 2],
           [3, 4]])




```python
a > 3
```




    array([[False, False],
           [False,  True]])



|Opgrator | Equivalent ufunc | operator | Equivalent ufunc |
|-|-|-|-|
|`==` |` np. equal`|`!=`|`np. not_equal`|
|`<`| `np. less`|`<=`|`np. less_equal`|
|'>'|`np. greater`|`>=`|`np. greater_equal`|


```python
# 判断每一个是否成立
np.all(a>1) 
```




    False




```python
# 判断存在
np.any(a<1)
```




    False



### 数组内字的运算

#### 求和


```python
a = np.array([[1,2],
             [3,4]])
```


```python
# 对每一列求和
sum(a)
```




    array([4, 6])




```python
# 求全部的和
np.sum(a)
```




    10




```python
# np.sum求一列的值
np.sum(a,axis=0)
```




    array([4, 6])




```python
# np.sum求一行的值
np.sum(a,axis=1)
```




    array([3, 7])




```python
# 效率比较
n = np.random.rand(100000)
%timeit sum(n)
```

    13.7 ms ± 2.02 ms per loop (mean ± std. dev. of 7 runs, 100 loops each)
    


```python
%timeit np.sum(n)
```

    65.9 µs ± 7.27 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
    

#### 求最值


```python
np.max(a),np.min(a)
```




    (4, 1)



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




    array([[11, 12, 21],
           [22, 31, 32]])



### 矩阵转置


```python
a.T
```




    array([[11, 21, 31],
           [12, 22, 32]])



### 排序


```python
a = np.array([[23,4,8,19],
              [2,5,1,0]])
a
```




    array([[23,  4,  8, 19],
           [ 2,  5,  1,  0]])



#### 对每一行排序


```python
# 临时排序
np.sort(a)
```




    array([[ 4,  8, 19, 23],
           [ 0,  1,  2,  5]])




```python
a
```




    array([[23,  4,  8, 19],
           [ 2,  5,  1,  0]])




```python
# 彻底排序
a.sort()
```


```python
a
```




    array([[ 4,  8, 19, 23],
           [ 0,  1,  2,  5]])




```python
n = np.random.rand(100000)
%timeit np.sort(n)
```

    8.6 ms ± 347 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    


```python
%timeit n.sort()
```

    1.09 ms ± 105 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    


```python
a = np.array([[12,3,5]
              ,[0,6,2],
              [1,5,8]])
np.sort(a,axis=0) # 同时按照每行第一个数排列行
```




    array([[ 0,  3,  2],
           [ 1,  5,  5],
           [12,  6,  8]])



### 拼接


```python
a
```




    array([[12,  3,  5],
           [ 0,  6,  2],
           [ 1,  5,  8]])




```python
# 按行拼
np.concatenate([a,a,a])
# con共同 + caten链+ate v → concatenate链接,连锁
```




    array([[12,  3,  5],
           [ 0,  6,  2],
           [ 1,  5,  8],
           [12,  3,  5],
           [ 0,  6,  2],
           [ 1,  5,  8],
           [12,  3,  5],
           [ 0,  6,  2],
           [ 1,  5,  8]])




```python
# 按列拼
np.concatenate([a,a,a],axis=1)
```




    array([[12,  3,  5, 12,  3,  5, 12,  3,  5],
           [ 0,  6,  2,  0,  6,  2,  0,  6,  2],
           [ 1,  5,  8,  1,  5,  8,  1,  5,  8]])


