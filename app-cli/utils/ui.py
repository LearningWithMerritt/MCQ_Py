import os,sys
import time
import shutil



class Menu():
    ''' Handles User Interface elements '''

    def __init__(self,
        pattern = None,
        header="",
        sepchar="=",
        sepmaxlen=1000,
        prompt="",
        options=None,
        cli_prompt = "$> " 
    ):
        self.header = header
        self.prompt = prompt
        self.sepmaxlen = sepmaxlen
        self.sepchar = sepchar
        if options is None:
            self.options = {}
        else:
            self.options = options
        
        self.flow_options = {
            "Q": Menu_Option("Quit", self.exit, True),
        }

        self.all_options = self.options | self.flow_options

        self.cli_prompt = cli_prompt

        self.output = None
        self.switch = True

    def run(self):
        try:
            self.switch = True
            while(self.switch):
                self.clear()
                self.set_seperator(self.sepchar,len(self.header))
                if(self.header):
                    print(self.header)
                    print(self.sep +"\n")

                print(self.prompt,"\n")
                if(0 < len(self.sep)):
                    print(self.sep +"\n")

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
                            else:
                                return


                    elif(self.confirm()):
                        if(self.switch):
                            self.output = pick
                            if(pick.do is not None):
                                pick.do()
                            else:
                                return
    
                else:
                    print("PLEASE SELECT A VALID OPTION.\n")
                    input("press [ENTER] to continue...")
        except KeyboardInterrupt as e:
            print("GOODBYE...\n")
            sys.exit()

    def stop(self):
        self.switch = False

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
        self.clear()
        print("GOODBYE!...\n")
        sys.exit()
    
    def in_options(self, pick) -> bool:
        return pick in self.all_options.keys()
    
    def set_seperator(self,char,length,maxlen=None):
        if maxlen is None:
            maxlen = self.sepmaxlen

        if(length < maxlen):
            width = shutil.get_terminal_size().columns
            if(length < width):
                self.sep = char * length
            else:
                self.sep = char * width
        else:
            self.sep = char * maxlen
        
    def set_flow(self,options):
        for choice in options.keys():
            self.flow_options[choice] = options[choice]

            self.all_options = self.options | self.flow_options

    def add_option(self, key, val):
        self.options[key] = val

        self.all_options = self.options | self.flow_options





class Menu_Option:

    def __init__(self, text, do=None, confirm=False):
        self.text = text
        self.do = do
        self.confirm = confirm








