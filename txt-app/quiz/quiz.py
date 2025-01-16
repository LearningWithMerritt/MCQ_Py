'''TODO:
Save the user name with saved work, and dont ask again
only ask for name when starting a new quiz
'''

import time
import random
import os
from pathlib import Path

from quiz.mcq import MCQ
from utils.utils import * 
from utils.file_hander import write_json,read_json
from utils.json_handler import Save

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
        self.elapsed_time:float = 0.0 
        self.previous_time:float = 0.0
        self.stop_switch:bool = False

        self.save_file = Save(Path(__file__).parent / "save.json")

        self.questions:list = []
        self.used: list = []
        self.load_questions(questions)

    def load_questions(self, questions: list) -> None:
        for q in questions:
            self.questions.append(MCQ(*q))

    def __question_loop(self):
        clear_screen()
        question = self.get_question()
        header = self.set_header()
        question.make_prompt(header, self.question_number)

        answer = question.get_choice()
        if(answer.upper() == "Q"):
            if(get_confirmation()):
                self.end()
                self.stop_switch = True
                return

        elif(question.check_answer(answer)):
            self.score +=1

        self.used.append(question.question)
        time.sleep(1)
    
    def start(self) -> None:
        try:
            self.load()

            if self.question_number >= self.num_of_questions:
                self.show_report()
                return

            if not self.username:
                self.set_username()
            clear_screen()
            self.directions()

            self.start_time = time.time()

            while(self.question_number < self.num_of_questions):
                if self.stop_switch:
                    break
                self.question_number += 1
                self.__question_loop()

            self.end()
        except KeyboardInterrupt as e:
            self.end()
            raise KeyboardInterrupt

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
        self.elapsed_time = self.previous_time + self.end_time - self.start_time
        self.calc_score()
        self.save()
        self.show_report()

    def calc_score(self):
        self.percent:float = round(self.score / self.num_of_questions * 100,0)

    def save(self):
        data = {
            self.title : {
                "username" : self.username,
                "num_of_questions" : self.num_of_questions,
                "question_number" : self.question_number-1,
                "score" : self.score,
                "used" : self.used,
                "elapsed_time" : self.elapsed_time,
            }
        }

        self.save_file.save(data)

    def load(self):
        data = self.save_file.load()
            
        if self.title in data.keys():
            data = data[self.title]
            self.username = data["username"]
            self.num_of_questions = data["num_of_questions"]
            self.question_number = data["question_number"]
            self.score = data["score"]
            self.used = data["used"]
            self.previous_time = data["elapsed_time"]

    def get_question(self):
        question = self.questions.pop(random.randint(0,len(self.questions)-1))

        while(question.question in self.used):
            question = self.questions.pop(random.randint(0,len(self.questions)-1))
        
        return question

    def set_header(self):
        status_header = f"NAME: {self.username}  SCORE: {self.score}/{self.num_of_questions}\n"
        sep = "-" * len(status_header) + "\n"
        status_header += sep

        return status_header

    def show_report(self):
        pass
