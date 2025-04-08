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
import sys

from utils.context import *
from utils.utils import *
from utils.file_hander import *
from utils.ui import *
from quiz.quiz import Quiz

def main():
    try: 
        chmenu = Menu(
            prompt = f"Pick a Chapter:"
        )
        chmenu.set_flow({
            "B" : Menu_Option("Back", chmenu.stop)
        })

        chnum = 1
        for chapter, ch in modules.items():
            secmenu = Menu(
                prompt = f"{chapter}\nPick a section:"
            )
            secmenu.set_flow({
                "B" : Menu_Option("Back", secmenu.stop)
            })

            secnum = 1
            for section in ch.sections.keys():
                secmenu.add_option(str(secnum), Menu_Option(section, lambda c=ch,s=section : load_quiz(c.get_section(s))))
                secnum+=1

            chmenu.add_option(str(chnum), Menu_Option(chapter, secmenu.run))
            chnum +=1



  
        menu = Menu(
            prompt = f"Welcome to {version}\n\nWhat would you like to do?",
            options = {
                "1": Menu_Option("Take a Quiz",chmenu.run),
                # "2" : Menu_Option("Display Score Report", score_report),
                # "3" : Menu_Option("TESTING", lambda : load_quiz())
            }
        )

        menu.run()
               

    except KeyboardInterrupt as e:
        print(f"Goodbye... {version}")
        sys.exit()



def load_quiz(section=None):
    if section:
        path = q_setpath / section.filename
        qset = Save(path)
        try:
            data = qset.read()
        except FileNotFoundError as e:
            print("NOTICE: Quiz Not Available.")
            log(f"QUIZ-NOT-FOUND({section.name}) : {e}")
            wait()
            return
        Quiz(section.name,data,30).run()
    else:
        path = q_setpath / "test.json"
        qset = Save(path)
        data = qset.read()

        Quiz("TESTING",data,10).run()


def score_report():
    pass

if __name__ == "__main__":
    main()

