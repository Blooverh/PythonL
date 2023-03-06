import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question="What language did you learn first? "
        self.my_survey=AnonymousSurvey(question) # creates a survey instance
        self.responses = ['English', 'Portuguese', 'Mandarin'] #creates a list of responses 

    def test_store_single_response(self): #function only checks the first item of the list is correspondent 
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        

    def test_store_three_responses(self):
        for response in self.responses:
           self. my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()