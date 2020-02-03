---
jupyter:
  jupytext:
    formats: ipynb,py:light,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.3
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# 运行

```python
print('hello world')

```

```python
print('hello \nworld')

```

```python
print('hello \ world')

```

```python
print('''hello
world''')
```

```python
print('he said "hello"')
```

循环引用其它对象或引用自全局命名空间的对象的模块，在Python退出时并非完全释放。

另外，也不会释放C库保留的内存部分。

```python
help(print)
```

```python
print(1,2,sep='-')
```

```python
import time
print('123',end='\r')
time.sleep(1)
print('456')
```
