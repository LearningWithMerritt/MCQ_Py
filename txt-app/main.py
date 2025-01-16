'''
TODO:
Check File Integrity, and fix

Menu Choices
Decrypt File, Delete, and then display


'''

import time
import sys
import importlib

# from quiz.mcq import MCQ
from quiz.quiz import Quiz
from utils.utils import *
from utils.config import * 
from utils.file_hander import * 
from utils.crypt import dexor


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
        # "Continue Last Quiz" : continue_last,
        "Take A Quiz" : take_quiz,
        "Restart A Quiz" : restart_quiz,
        "Display Score Report" : score_report,
    }

    create_menu(prompt, options,back=False)
         
def take_quiz():
    prompt = "Please pick a chapter:\n\n"

    options = {}

    for chapter in modules.keys():
        sections = modules[chapter].get_sections()
        sub_options = {}
        for name, section in sections.items():
            sub_options[name] = lambda section=section : load_section(section)

        options[chapter] = lambda sub_options=sub_options: create_menu(
            "Please pick a section:\n\n",
            sub_options,
        )

    create_menu(prompt,options)

def restart_quiz():
    pass

def score_report():
    pass

def load_section(section):
    dexor(
        q_setpath / f"{section.filename}.enc",
        q_setpath / f"{section.filename}.py",
        q_setpath / f"{section.filename}.key"
    )

    module = importlib.import_module(f"quiz.q_sets.{section.filename}")

    try:
        basic = getattr(module, "basic")
        advanced = getattr(module, "advanced")

    except AttributeError as e:
        print("MISSING AN ATTRIBUTE", e)

    else:
        delete_fromdir(q_setpath,".py")
        Quiz(section.name, basic, 20).start()

    finally:
        delete_fromdir(q_setpath,".py")
        
       

if __name__ == "__main__":

    main()