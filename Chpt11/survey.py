class AnonymousSurvey:

    def __init__(self, question):
        self.question= question
        self.responses=[] # default value is an empty list of responses 

    def show_question(self):
        print(self.question)

    def store_response(self, newResponse):
        self.responses.append(newResponse)

    def show_result(self):
        print("Survey results: ")
        for response in self.responses:
            print(f"- {response}")
             
