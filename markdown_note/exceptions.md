
# 异常 
每当python不知所措时,会创建一个异常对象,若没有对异常进行处理,程序停止,返回一个traceback


```python
5/0
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-1-0106664d39e8> in <module>()
    ----> 1 5/0
    

    ZeroDivisionError: division by zero



```python
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divided by zero")
```

    you can't divided by zero
    

## else 代码块


```python
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
```

    Give me two numbers, and I'll divide them
    Enter 'q' to quit
    
     first number: 1
    Second number: 3
    0.3333333333333333
    
     first number: 2
    Second number: 4
    0.5
    
     first number: 1
    Second number: 0
    You can't divide by 0!
    
     first number: q
    

## 处理FileNotFoundError

 filename = 'alice.txt'

with open(filename) as f_obj:
    contents = f_obj.tead()

try 语句引发异常,所以放到try里


```python
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.tead()
except FileNotFoundError:
    print('Sorry the file',filename,'does not exist')
```

    Sorry the file alice.txt does not exist
    

## assert 断言
断言不成立,程序崩溃


```python
age = 18
assert age == 19, 'age不是19'
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-1-254c69178ac1> in <module>()
          1 age = 18
    ----> 2 assert age == 19, 'age不是19'
    

    AssertionError: age不是19


## EOF处理

### pyhton 没有EOF


```python
a = input()
while a != EOF:
    print(a)
```

    a
    


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-1-255962570bc2> in <module>
          1 a = input()
    ----> 2 while a != EOF:
          3     print(a)
    

    NameError: name 'EOF' is not defined



```python
# EOF 可以用try实现
while True:
    try:
        a = input()
    except EORError:
        print('EOF')
```

    a
    


```python

```
