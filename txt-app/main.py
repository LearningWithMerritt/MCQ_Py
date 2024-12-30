import time

# from quiz.mcq import MCQ
from quiz.quiz import Quiz
from utils.utils import *


from quiz.q_sets_plain.q_set15 import basic,advanced

try:
    # for q in basic:
    #     clear_screen()
    #     print(MCQ(*q).check_answer())
    #     time.sleep(1)

    Quiz("EXAMPLE",basic,20).start()
        
        
except KeyboardInterrupt:
    clear_screen()
    print("GOODBYE...")


