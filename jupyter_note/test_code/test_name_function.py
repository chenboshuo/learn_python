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
output 
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

'''