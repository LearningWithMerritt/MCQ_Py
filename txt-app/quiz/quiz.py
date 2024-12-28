import time
import random

from quiz.mcq import MCQ
from utils.utils import * 

class Quiz():

    def __init__(self,questions:list=[], num_of_questions:int=0):
        self.title = title
        self.num_of_questions:int = num_of_questions
        self.score:int = 0
        self.percent:float = 0
        
        self.start_time:float = 0.0 
        self.end_time:float = 0.0
        self.elasped_time:float = 0.0 

        self.questions = []
        self.load(questions)


    def load(self, questions: list) -> None:
        for q in questions:
            self.questions.append(MCQ(*q))


    def __question_loop(self):

        question = self.questions.pop(random.randint(0,len(self.questions)))
        no_answer = True
        while (no_answer):
            clear_screen()
            answer = question.choice_input()
            if(answer.upper() == "Q"):
                if(get_confirmation()):
                    self.end()
                    no_answer = False
                    raise KeyboardInterrupt

            elif(question.check_answer(answer)):
                no_answer = False
                self.score +=1

        time.sleep(1)
    
    def start(self) -> None:
        self.start_time = time.time()

        for _ in range(self.num_of_questions):
            self.__question_loop()

        self.end()
            

    def end(self) -> None:
        self.end_time = time.time()
        self.elasped_time = self.end_time - self.start_time
        self.calc_score()

    def calc_score(self):
        self.percent:float = round(self.score / self.num_of_questions * 100,0)

    def save(self):
        data = {}

    def quit(self):
        pass



        


