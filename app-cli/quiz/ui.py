import re
from types import *

class Menu():
    ''' Handles User Interface elements '''

    def __init__(self):
        self.header = ""
        self.prompt = ""
        self.sep = "-"*len(self.prompt)
        self.choices = {} 
        self.footer = ""

        self.pattern = ""                    

        self.choice_label = "int" #("int","chr")


    def get_selection(self):
        switch = True
        while(switch):
            print(self.header,"\n")

            print(self.prompt,"\n")
            print(self.sep)

            for i,e in enumerate(self.choices):
                if "int" == self.choice_label:
                    pass
                elif "str" == self.choice_label:
                    pass

            
            print(self.footer,"\n")

            user_in = input().strip().lower()

            if(not re.search(pattern, user_in)):
                print(self.rejection)
                input("PRESS ENTER TO CONTINUE...")
                continue

            
            self.select_option(user_in)
            






{
    "Take a Quiz": Menu(
        "Pick a Chapter",chapter_map
    )
}





        if()



