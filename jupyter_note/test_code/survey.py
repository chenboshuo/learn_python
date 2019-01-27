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

if __name__ == '__main__':
    # 定义问题,创建对象
    question = 'What language did you first learn to speak'
    my_survey = AnonyousSurvey(question)

    # 显示问题并存储答案
    my_survey.show_question()
    print('Enter "q" to quit')
    while True:
        response = input('Languages:')
        if response == 'q':
            break
        my_survey.store_response(response)

    # 显示调查结果
    print('\nThank you to everyone who participed in the survey')
    my_survey.show_results()