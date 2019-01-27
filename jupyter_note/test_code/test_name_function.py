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
'''
错误时输出
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

'''