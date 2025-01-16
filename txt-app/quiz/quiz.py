'''TODO:
Create a report using data from the save file

Change restart into a loop, instead of a recursion


'''

import time
import random
import os
from pathlib import Path

from quiz.mcq import MCQ
from utils.utils import * 
# from utils.file_hander import write_json,read_json
from utils.json_handler import Save

class Quiz():

    def __init__(self,title:str="QUIZ",questions:list=[], num_of_questions:int=0):
        self.username = ""
        self.title = title
        self.num_of_questions:int = num_of_questions
        self.question_number:int = 0
        self.score:int = 0
        self.percent:float = 0

        self.passing_score = 75
        self.passed = False
        
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
        footer = "\nR). Restart  Q). Quit\n"
        question.make_prompt(header, self.question_number, footer)


        answer = question.get_choice()
        if(answer == "Q"):
            if(get_confirmation()):
                self.end()
                self.stop_switch = True
                return
        elif(answer == "R"):
            if(get_confirmation()):
                self.restart()
                self.stop_switch = True
                return

        elif(question.check_answer(answer)):
            self.score +=1

        self.used.append(question.question)
        time.sleep(1)
    
    def start(self) -> None:
        try:
            self.stop_switch = False
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
                    return
                self.question_number += 1
                self.__question_loop()
                if self.stop_switch:
                    return

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
        self.percent:float = round(self.score / self.num_of_questions * 100)
        if self.percent > self.passing_score:
            self.passed = True

    def save(self):
        data = {
            self.title : {
                "passed" : self.passed,
                "username" : self.username,
                "num_of_questions" : self.num_of_questions,
                "question_number" : self.question_number-1 if self.question_number < self.num_of_questions else self.question_number,
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

            self.calc_score()

            if self.question_number < 0:
                self.question_number = 0

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
        if(self.passed):
            passed = "\u2705 Passed!"
        else:
            passed = "\u274C Not Yet Passed"
        clear_screen()
        print(f"Name: {self.username} | Quiz: {self.title} | Score: {self.score}/{self.num_of_questions} | Percent: {self.percent} | Passed? : {passed}")
        input("PRESS ENTER TO CONTINUE")

        user_in = check_input(
            r"^[YN]$",
            "Would you like to take the quiz again?(y/n)\n",
            "Please type a valid input 'y' or 'n'."
        )

        if user_in == "Y":
            self.restart()

    def restart(self):
        data = self.save_file.load()
        if self.title in data.keys():
            del data[self.title]

        self.username = ""
        self.question_number = 0
        self.score = 0
        self.used = []
        self.previous_time = 0
        

        self.save_file.write(data)
        self.start()