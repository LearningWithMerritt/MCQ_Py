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