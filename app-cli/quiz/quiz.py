from utils.utils import *
from quiz.mcq import MCQ


class Quiz:

    def __init__(self,
        title:str,
        questions:list=[],
        totalquestions:int=0,
        pass_score:int=75
    ):
        self.title = title
        self.totalquestions:int=totalquestions
        self.pass_score:int = pass_score
        self.savefile = None #Save Object
        self.questions:list = self.load_questions(questions)
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

        self.switch:bool = False
    
    def load_questions(self, questions:list) -> None:
        for q in questions:
            self.questions.append(MCQ(*q))

    def begin(self) -> None:
        pass

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
        self.percent = round(self.score /self.totalquestions * 100)
        if self.percent > self.pass_score:
            self.passing = True

    def save(self) -> None:
        pass
    
    def load(self) -> None:
        pass

    def report(self) -> None:
        pass

    def restart(self) -> None:
        pass