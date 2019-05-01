
# 运行


```python
print('hello world')

```

    hello world
    


```python
print('hello \nworld')

```

    heollo 
    world
    


```python
print('hello \ world')

```

    hello \ world
    


```python
print('''hello
world''')
```

    hello
    world
    


```python
print('he said "hello"')
```

    he said "hello"
    

循环引用其它对象或引用自全局命名空间的对象的模块，在Python退出时并非完全释放。

另外，也不会释放C库保留的内存部分。


```python
help(print)
```

    Help on built-in function print in module builtins:
    
    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
        
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
    
    


```python
print(1,2,sep='-')
```

    1-2
    


```python
import time
print('123',end='\r')
time.sleep(1)
print('456')
```

    456
    
