'''
TODO:
Check File Integrity, and fix

Menu Choices
Decrypt File, Delete, and then display


'''





import time
import sys

# from quiz.mcq import MCQ
from quiz.quiz import Quiz
from utils.utils import *
from utils.config import * 


def main():
    try:
        main_menu()

    except KeyboardInterrupt as e :
        clear_screen()
        print(f"{version}")
        sys.exit()



def main_menu():
    prompt = (
        f"Welcome to {version}\n\n"
        "What would you like to do?\n\n"
    )

    options = {
        "Take A Quiz" : take_quiz,
        "Restart A Quiz" : restart_quiz,
        "Display Score Report" : score_report,
    }

    create_menu(prompt, options,back=False)


    


def create_menu(prompt:str, options:dict[str:object], back:bool=True):
    run = True
    letters = "Qq"
    length = len(options)
    option_list = tuple(options.keys())

    i = 1
    for option in options.keys():
        prompt += f"{i}.) {option}\n"
        i+=1

    prompt += "\n"

    if back:
        letters += "Bb"
        prompt += "B.) BACK "
    
    prompt += "Q.) QUIT\n"

    while run:
        clear_screen()
        user_in = check_input(
            f"[1-{length}{letters}]" + r"{1}",
            prompt,
            f"Please input a valid response (1-{length} OR {letters}.)\n",
        )

        if user_in == "B":
            run = False
            return
        elif user_in == "Q":
            run = False
            raise KeyboardInterrupt
        else:
            function = options[option_list[int(user_in)-1]]
            function()
            


def take_quiz():
    prompt = "Please pick a chapter:\n\n"

    options = {}

    for chapter in quiz_modules.keys():
        section_names = quiz_modules[chapter].keys()
        sections = {}
        for name in section_names:
            section_data = quiz_modules[chapter][name]
            sections[name] = lambda c=chapter,n=name : get_section(c,n)

        options[chapter] = lambda sections=sections: create_menu(
            "Please pick a section:\n\n",
            sections,
        )

    create_menu(prompt,options)

def restart_quiz():
    pass

def score_report():
    pass

def get_section(chapter, name):
    print(f"{name} : {quiz_modules[chapter][name]['file']}")
    time.sleep(2)



    


main()