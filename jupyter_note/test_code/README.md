
# 测试代码

## 测试函数
模块unittest提供了代码测试工具. **单元测试**用于核实函数某个方面没有问题;**测试用例**是一组单元测试,这些单元测试一起核实函数在各种情形下的行为都符合要求

### 可通过的测试

name_function.py

```python
def get_formatted_name(first, last):
    '''Generate a neatly formatted name'''
    full_name = first + ' '  + last
    return full_name.title()

```

```python
import unittest 
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''测试name_function.py'''

    def test_first_last_name(self):
        '''能够处理像Janis Joplin 这样的姓名吗'''
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

        formatted_name = get_formatted_name('stephen', 'hawking')
        self.assertEqual(formatted_name, 'Stephen Hawking')


unittest.main()
```
output 
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

```

首先导入了模块
```python
import unittest 
```
```python
class NamesTestCase(unittest.TestCase):
```

然后创建类`NameTestCase`,包含一系列单元测试,命名尽量与函数相关,并包含字样Test,这个类必须继承`unittest.TestCase`,这样python才知道如何运行这个单元测试
```python
self.assertEqual(formatted_name, 'Janis Joplin')
```
我们使用了 **断言** 方法. 断言方法一般来核实结果是否与期望一致


### 不能通过的测试

接下来修改`name_function`
```python
def get_formatted_name(first, middle , last):
    '''Generate a neatly formatted name'''
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()
```

```
E
======================================================================
ERROR: test_first_last_name (__main__.NamesTestCase)
能够处理像Janis Joplin 这样的姓名吗
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:/OneDrive - JJXY/文档/python/python_learning/jupyter_note/test_code/test_name_function.py", line 9, in test_first_last_name
    formatted_name = get_formatted_name('janis', 'joplin')
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
```

`E`指出测试中有一个单元测试导致了错误

接下来看到`ERROR: test_first_last_name (__main__.NamesTestCase)`是`NamesTestCase`中的`test_first_last_name`导致错误,测试用例包含众多单元测试时,知道那个未通过至关重要

接下来有个标准`Traceback`,指出位置实参

`FAILED (errors=1)`告诉我们一共发生一个错误

### 添加新的测试 

现在函数改为
```python
def get_formatted_name(first, last,middle=''):
    '''Generate a neatly formatted name'''
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
```

```python
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''测试name_function.py'''

    def test_first_last_name(self):
        '''能够处理像Janis Joplin 这样的姓名吗'''
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('stephen', 'hawking','william')
        self.assertEqual(formatted_name, 'Stephen William Hawking')


unittest.main()
```

测试结果
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## 测试类
如果针对类的测试通过了, 可以确信对类做出的改变没有破坏原有的行为

### 各种断言方法

方法|用途
:-|:-
assertEqual(a,b)|核实a==b
assertNotEqual(a,b)| a!=b
assertTrue(a)| a为True
assertFalse(a)| a为false
assertIn(item, liset)|item在listzhong
assertNotIn(item, list)|item不在list中

### 一个要测试的类

```python
class AnonyousSurvey():
    '''收集匿名调查问卷的答案'''

    def __init__(self, question):
        '''存储一个问题,并为答案做准备'''
        self.question = question
        self.responses = []

    def show_question(self):
        '''显示调查问卷'''
        print(self.question)

    def store_response(self,new_response):
        '''存储单份调查答卷'''
        self.responses.append(new_response)

    def show_results(self):
        '''显示所有收集到的答案'''
        print('Survey results:')
        for response in self.responses:
            print('-',response)
```

```python
import unittest
from survey import AnonyousSurvey

class TestAnonymousSurney(unittest.TestCase):
    '''针对Testcase的测试'''

    def test_store_single_response(self):
        '''单个答案是否会被妥善保存'''
        question = 'What language did you first lesrn to speak'
        my_survey = AnonyousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English',my_survey.responses)

    def test_store_three_responses(self):
        '''测试三个答案是否能被存储'''
        question = 'What language did you first learn to speak'
        my_survey = AnonyousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)
unittest.main()
```

### 方法setUp()
unittest.TestCase包含方法setUp(),只需创建对象一次,可以在测试方法中使用它们

```python
import unittest
from survey import AnonyousSurvey

class TestAnonymousSurney(unittest.TestCase):
    '''针对Testcase的测试'''

    def setUp(self):
        '''
        创建一个调查对象和一组答案, 供使用的测试方法调用
        '''
        question = 'What language did you first lesrn to speak'
        self.my_survey = AnonyousSurvey(question)# 将他们存储到属性中
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        '''单个答案是否会被妥善保存'''
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):
        '''测试三个答案是否能被存储'''
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)



```

```
unittest.main()
'''
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
'''
```

