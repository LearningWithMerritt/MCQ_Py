import os,sys
import time


class Menu():
    ''' Handles User Interface elements '''

    def __init__(self,
        pattern = None,
        header="",
        sep="=",
        sepmaxlen=75,
        prompt="",
        options={},
        cli_prompt = "|MCQ_Py|> "
    ):
        self.header = header
        self.prompt = prompt
        self.set_seperator(sep,len(header), sepmaxlen)
        self.options = options
        
        self.flow_options = {
            "Q": Menu_Option("Quit", self.exit, True),
        }

        self.all_options = self.options | self.flow_options

        self.cli_prompt = cli_prompt

        self.output = None
        self.switch = True

    def run(self):
        self.switch = True
        while(self.switch):
            self.clear()
            if(self.header):
                print(self.header)
                print(self.sep)

            print(self.prompt,"\n")
            if(0 < len(self.sep)):
                print(self.sep)

            for key, option in self.options.items():
                print(f"[{key}]. {option.text}")
            print()

            for key,option in reversed(self.flow_options.items()):
                print(f"[{key}]: {option.text}",end="  ")
            print()

            user_in = input(self.cli_prompt).strip().upper()


            if(self.in_options(user_in)):
                pick = self.all_options[user_in]
                if(not pick.confirm):
                    if(self.switch):
                        self.output = pick
                        if(pick.do is not None):
                            pick.do()


                elif(self.confirm()):
                    if(self.switch):
                        self.output = pick
                        if(pick.do is not None):
                            pick.do()
  
            else:
                print("PLEASE SELECT A VALID OPTION.\n")
                input("press [ENTER] to continue...")
 
    def confirm(self):
        affirm = ["YES","Y"]
        user_in = input(f"Are you sure? (y/n)\n{self.cli_prompt}").strip().upper()
        return user_in in affirm
            
    def clear(self):
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")
        else:
            print(f"Unknown OS '{os.name}' : Cannot Clear Screen")

    def wait(self, seconds=0):
        time.sleep(seconds)
        input("press [ENTER] to continue...")

    def exit(self):
        print("GOODBYE!.")
        sys.exit()

    def set_seperator(self,char,length,maxlen):
        if(length < maxlen):
            self.sep = char * length
        else:
            self.sep = char * maxlen
        
    def control(self, user_in):
        keys = self.flow_options.keys()
        if user_in in keys:
            pick = self.flow_options[user_in]

            if 2 < len(pick):
                confirm = pick[2]

                if(not confirm()):
                    return None

            function = pick[1]
            function()

    def in_options(self, pick) -> bool:
        return pick in self.all_options.keys()

    def set_flow(self,options):
        for choice in options.keys():
            self.flow_options[choice] = options[choice]

            self.all_options = self.options | self.flow_options

    def stop(self):
        self.switch = False

class Menu_Option:

    def __init__(self, text, do=None, confirm=False):
        self.text = text
        self.do = do
        self.confirm = confirm



if __name__ == "__main__":

    def load_section(section):
        print(section)
        input()





    sec_menu = Menu(
        prompt = "Pick a section:",
        options = {
            "1" : Menu_Option("Section 1",lambda s="Section 1": load_section(s),True)
        }
    )
    sec_menu.set_flow({
        "B" : Menu_Option("Back", sec_menu.stop),
    })

    ch_menu = Menu(
        prompt = "Pick a chapter.",
        options = {
            "1" : Menu_Option("Chapter 1",sec_menu.run),
            "2" : Menu_Option("Chapter 2"),
            "3" : Menu_Option("Chapter 3")
        }
    )
    ch_menu.set_flow({
        "B" : Menu_Option("Back", ch_menu.stop),
    })


    main_menu = Menu(
        prompt = "What would you like to do?",
        options = {
            "1" : Menu_Option("Take A Quiz", ch_menu.run),

        },
    )


    main_menu.run()
    print(sec_menu.output.text)
 





