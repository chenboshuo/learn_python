
# 运算

## 算术运算

### 除法
除法默认是浮点数


```python
2/1
```




    2.0



#### 取整的除法


```python
2//1
```




    2



## 逻辑运算

| operation| result |
| :--: | :--: |
| x or y| if x is false,then y,else x |
| x and y| if x is false,then x,else y |
| not x| if x is false,then `True`, else `False` |

1. This is a short-circuit operator, so it only evaluates the second argument if the first one is false.
2. This is a short-circuit operator, so it only evaluates the second argument if the first one is true.
3. not has a lower priority than non-Boolean operators, so `not a == b` is interpreted as` not (a == b)`, and `a == not b` is a syntax error.


```python
0 or 8b
```




    8




```python
4 or 5
```




    4




```python

```

## 成员运算

## 位运算
该运算符按二进制位对值进行操作。

###  与（&）
按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0


```python
0b110 & 0b010
```




    2




```python
bin(0b110 & 0b010)
```




    '0b10'



#### 应用:　判断奇数偶数


```python
3 & 1 # 结果是1 证明是奇数
```




    1



### 或（|）
按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。


```python
3|2
```




    3




```python
bin(0b11 | 0b10)
```




    '0b11'



### 异或（^）
按位异或运算符：当两对应的二进位相异时，结果为1


```python
3^2
```




    1




```python
bin(0b11 ^ 0b10)
```




    '0b1'



### 取反（~）
按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1


```python
~2
```




    -3




```python
bin(~0b10)
```




    '-0b11'




```python
bin(~0b010)
```




    '-0b11'




```python
bin(~0b110)
```




    '-0b111'




```python
bin(~-0b10)
```




    '0b1'



### 左位移（<<）
运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0


```python
1<<2
```




    4




```python
bin(0b1<<2)
```




    '0b100'



### 右位移（>>）
把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数


```python
4>>2
```




    1


