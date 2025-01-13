'''TODO:
Save the user name with saved work, and dont ask again
only ask for name when starting a new quiz
'''

import time
import random
from pathlib import Path

from quiz.mcq import MCQ
from utils.utils import * 

class Quiz():

    def __init__(self,title:str="QUIZ",questions:list=[], num_of_questions:int=0):
        self.username = ""
        self.title = title
        self.num_of_questions:int = num_of_questions
        self.question_number:int = 0
        self.score:int = 0
        self.percent:float = 0
        
        self.start_time:float = 0.0 
        self.end_time:float = 0.0
        self.elasped_time:float = 0.0 
        self.stop_switch:bool = False

        self.questions:list = []
        self.used: list = []
        self.load(questions)

    def load(self, questions: list) -> None:
        for q in questions:
            self.questions.append(MCQ(*q))

    def __question_loop(self):
        clear_screen()
        question = self.questions.pop(random.randint(0,len(self.questions)-1))
        

        status_header = f"NAME: {self.username}  SCORE: {self.score}/{self.num_of_questions}\n"
        sep = "-" * len(status_header) + "\n"
        status_header += sep
            
        question.make_prompt(status_header, self.question_number)

        answer = question.get_choice()
        if(answer.upper() == "Q"):
            if(get_confirmation()):
                self.end()
                self.stop_switch = True
                return

        elif(question.check_answer(answer)):
            self.score +=1

        time.sleep(1)
    
    def start(self) -> None:
        self.start_time = time.time()

        self.set_username()
        self.directions()

        for _ in range(self.num_of_questions):
            if self.stop_switch:
                break
            self.question_number += 1
            self.__question_loop()

        self.end()

    def directions(self):
        print("Answer the following multiple choice questions to best of your ability.")
        print(f"The number of questions on this quiz is: {self.num_of_questions}\n")
        input("Press ENTER to continue...\n")

    def set_username(self):
        clear_screen()
        name = check_input(
            r"[A-Z]+\s[A-Z]+",
            "Please type your FIRST and LAST name below.\n",
            "Make sure you enter your FIRST and LAST name with a single space in between."
        )
        while(len(name) > 20):
            clear_screen()
            print("The name you entered is to long, please limit your name to 20 characters or less.")
            name = check_input(
            r"[A-Z]+\s[A-Z]+",
            "Please type your FIRST and LAST name below.\n",
            "Make sure you enter your FIRST and LAST name with a single space in between."
        )
        
        self.username = name

    def end(self) -> None:
        self.end_time = time.time()
        self.elasped_time = self.end_time - self.start_time
        self.calc_score()
        self.save()

    def calc_score(self):
        self.percent:float = round(self.score / self.num_of_questions * 100,0)

    def save(self):
        path = Path(__file__).parent / "save.json"
        data = {
            self.title : {
                "username" : self.username,
                "number_of_questions" : self.num_of_questions,
                "question_number" : self.question_number,
                "score" : self.score,
                "used" : self.used,
            }
        }


        

    def quit(self):
        pass



        


