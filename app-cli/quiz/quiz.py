import random

from utils.utils import *
from utils.ui import * 
from utils.file_hander import * 
from quiz.mcq import MCQ


class Quiz:

    def __init__(self,
        title:str,
        question_data:dict[str:list],
        totalquestions:int=0,
        pass_score:int=75
    ):
        self.title = title
        self.totalquestions:int=totalquestions
        self.pass_score:int = pass_score
        self.savefile = Save(Path(__file__).parent/"save.json")
        self.question_data: dict[str:list] = question_data
        self.questions:list = []
        self.used:list = []
        self.directions = (
            "Answer the following questions to the best of your ability.\n"
            f"Quiz Info:[Total Questions : {self.totalquestions}][ Minimum Passing Score : {self.pass_score/100*self.totalquestions}/{self.totalquestions}]"
        )

        self.username:str = None
        self.number:int = 0
        self.score:int = 0
        self.percent:int = 0.0
        self.passing:int = False

        self.lastdelta:float=0.0
        self.t0:float = 0.0
        self.tf:float = 0.0
        self.tdelta:float = 0.0

        self.switch:bool = True


    
    def load_questions(self) -> None:
        for question, options in self.question_data.items():
            self.questions.append(MCQ(question,*options))

    def begin(self) -> None:
        
        while(self.number <= self.totalquestions and self.switch):
            if(len(self.questions) < 1):
                self.load_questions()

            self.calc_percent()

            question = self.questions.pop(random.randint(0,len(self.questions)-1))

            if(self.number < 1):
                self.number = 1

            menu = Menu(
                cli_prompt = "$>",
                header = f"[Quiz: {self.title}][Name: {self.username}][Score: {self.score}/{self.totalquestions}][Percent: {self.percent}%]",
                prompt = f"{self.number}). {question.question}",
                options = question.options
            )

            menu.set_flow({
                "R" : Menu_Option("Restart", self.restart,True)
            })

            menu.run()
            print(f"Your Answer: {menu.output.text}")
            
            if question.check_answer(menu.output.text):
                self.score += 1

            wait(2)
            self.number += 1

    def set_uname(self):
        self.username = validate_in(
            r"[A-Z]+\s[A-Z]+",
            "Enter your FIRST and LAST name with a single space in between",
            "names may only contain letters (A-Z) with a space to seperate FIRST and LAST."
        )

        if(30 < len(self.username)):
            self.username = self.username[:30]
            print("\nProvided name exceeds max length and has been truncated.")
            wait(2)

    def end(self) -> None:
        self.tf = time.time()
        self.tdelta = self.lastdelta + self.tf - self.t0
        self.calc_score()
        self.save()
        self.report()
        
    def calc_score(self) -> None:
        self.calc_percent()
        if self.percent > self.pass_score:
            self.passing = True

    def calc_percent(self) -> None:
        self.percent = round(self.score /self.totalquestions * 100)

    def save(self) -> None:
        pass
    
    def load(self) -> None:
        pass

    def report(self) -> None:
        pass

    def restart(self) -> None:
        print("RESTARTING")
        input()