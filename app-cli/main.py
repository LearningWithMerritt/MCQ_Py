'''
TODO:
Check File Integrity, and fix

Encrypt/Decrypt save file when working with it

Context class for globals

Utils

UI, Menu Submenu Input Validate

Quiz
Question Type
MCQ


File Handling
json

Encryption
'''

# import time
# import sys
# import importlib

# # from quiz.mcq import MCQ
# from quiz.quiz import Quiz
# from utils.utils import *
# from utils.config import * 
# from utils.file_hander import * 
# from utils.json_handler import *
# from utils.crypt import dexor


# def main():
#     try:
#         main_menu()

#     except KeyboardInterrupt as e :
#         clear_screen()
#         print(f"GOODBYE! : {version}\n\n")
#         sys.exit()

# def main_menu():
#     prompt = (
#         f"Welcome to {version}\n\n"
#         "What would you like to do?\n\n"
#     )

#     options = {
#         # "Continue Last Quiz" : continue_last,
#         "Take A Quiz" : take_quiz,
#         "Display Score Report" : score_report,
#     }

#     create_menu(prompt, options,back=False)
         
# def take_quiz():
#     prompt = "Please pick a chapter:\n\n"

#     options = {}

#     for chapter in modules.keys():
#         sections = modules[chapter].get_sections()
#         sub_options = {}
#         for name, section in sections.items():
#             sub_options[name] = lambda section=section : load_section(section)

#         options[chapter] = lambda sub_options=sub_options: create_menu(
#             "Please pick a section:\n\n",
#             sub_options,
#         )

#     create_menu(prompt,options)


# def load_section(section):
#     dexor(
#         q_setpath / f"{section.filename}.enc",
#         q_setpath / f"{section.filename}.py",
#         q_setpath / f"{section.filename}.key"
#     )

#     module = importlib.import_module(f"quiz.q_sets.{section.filename}")

#     try:
#         basic = getattr(module, "basic")
#         advanced = getattr(module, "advanced")

#     except AttributeError as e:
#         print("MISSING AN ATTRIBUTE", e)

#     else:
#         delete_fromdir(q_setpath,".py")
#         Quiz(section.name, basic, 20).start()

#     finally:
#         delete_fromdir(q_setpath,".py")
        
# def score_report():
#     '''TODO:
#     Read from save.json
#     print a Report for all chapters 

#     Chapter
#         Section | Name | Passed? | Score | Percent
#         Section | Name | Passed? | Score | Percent
    
#     Chapter 
#         Section | Name | Passed? | Score | Percent
#         Section | Name | Passed? | Score | Percent
#     '''

#     report = Save(Path(__file__).parent/"quiz"/"save.json")

#     save_data = report.read()



#     if save_data:
#         clear_screen()
#         print(f"{version} SCORE REPORT:\n" + "-"*50)
#         for section, s in save_data.items():
#             if(s["passed"]):
#                 passed = "\u2705 Passed!"
#             else:
#                 passed = "\u274C Not Yet Passed"
#             print(f'{section} | {s["username"] } | {passed} | SCORE: {s["score"]}/{s["num_of_questions"]} | PRECENT: {s["percent"]}%')


#         print("\n" + "-"*50 + f"\n{version} SCORE REPORT: (Scroll Up for full report.)")
#         input("\nPRESS ENTER TO CONTINUE")


#     else:
#         clear_screen()
#         print("No current save data. Please complete a quiz.")
#         input("PRESS ENTER TO CONTINUE")
         

if __name__ == "__main__":
    from quiz.quiz import Quiz
    quiz = Quiz("DEFAULT")
    quiz.set_uname()