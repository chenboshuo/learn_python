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


unittest.main()
'''
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
'''