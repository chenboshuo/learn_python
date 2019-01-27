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
'''
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
'''