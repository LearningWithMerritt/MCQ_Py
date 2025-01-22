import os
import re
import time


def wait(seconds):
    if(seconds):
        time.sleep(seconds)
    else:
        input("press [Enter] to continue...")
    
def clear_screen():
    # For Unix/Linux
    if os.name == 'posix':
        os.system('clear')
    # For Windows
    elif os.name == 'nt':
        os.system('cls')

def validate_in(pattern, prompt,error):
    match = False
    user_in = ""
    while(not match):
        clear_screen()
        print(prompt)
        user_in = input().strip().upper()
        match = re.search(pattern, user_in)
        
        if(not match):
            print(f"\nINVALID INPUT: {error}")
            wait()

    return user_in


