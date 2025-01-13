import os
import re


def get_confirmation() -> bool:
    user_in = input("Are you sure? (Yes/No):\n").strip().upper()
    options = ("YES","Y")

    return user_in in options

def wait():
    input("PRESS ENTER TO CONTINUE...")
    
def clear_screen():
    # For Unix/Linux
    if os.name == 'posix':
        os.system('clear')
    # For Windows
    elif os.name == 'nt':
        os.system('cls')

def check_input(pattern, prompt,reject_prompt):
    no_match = True
    inp = ""
    while(no_match):
        inp = input(prompt).upper().lstrip(" ")
        no_match = not re.search(pattern, inp)
        
        if(no_match):
            clear_screen()
            input(f"{reject_prompt}\nPress ENTER to continue.\n")
            clear_screen()
    return inp


# def get_userin(pattern:str, prompt:str, rejection:str) -> str:
#     no_match = True
#     while(no_match):
#         no_match = validate_input(pattern)

#         if()


def validate_input(pattern):
    user_in = input().upper().strip()
    return re.search(pattern, user_in)


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
            f"^[1-{length}{letters}]$" ,
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