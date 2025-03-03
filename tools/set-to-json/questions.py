'''Place preformmated questions and answers in the dictionary "questions" below.'''

setname = "set11"


questions = {}

'''An Introduction to the Python Programming Language!'''
s1 = {
    "Who created the Python programming language?": [
        "Guido van Rossum", 
        "Dennis Ritchie", 
        "Bjarne Stroustrup", 
        "James Gosling"
    ],

    "In which year was Python first released?": [
        "1991", 
        "1994", 
        "2000", 
        "2008"
    ],

    "Which of the following is NOT a feature introduced in Python 2.0?": [
        "Improved Unicode support", 
        "List comprehensions", 
        "Garbage collection", 
        "Many usability improvements"
    ],

    "Which Python version introduced the print function with parentheses as mandatory syntax?": [
        "Python 3.0", 
        "Python 1.0", 
        "Python 2.0", 
        "Python 3.9"
    ],

    "When did official support for Python 2 end?": [
        "January 1, 2020", 
        "December 3, 2008", 
        "October 16, 2000", 
        "March 15, 2021"
    ],

    "Which of the following programming paradigms is NOT supported by Python?": [
        "Assembly programming", 
        "Procedural programming", 
        "Object-oriented programming", 
        "Functional programming"
    ],

    "What is the file extension for Python scripts?": [
        ".py", 
        ".pyt", 
        ".python", 
        ".exe"
    ],

    "What command is used to invoke the Python interpreter on Windows?": [
        "python", 
        "python3", 
        "py", 
        "py3"
    ],

    "What command is used to run a Python script named `script.py` on a UNIX-like system?": [
        "python3 script.py", 
        "python script.py", 
        "run script.py", 
        "exec script.py"
    ],

    "Which of the following statements about Python's syntax is TRUE?": [
        "Python uses significant whitespace to enhance readability", 
        "Python requires semicolons at the end of every statement", 
        "Python uses curly braces `{}` to define blocks of code", 
        "Python is case insensitive"
    ]
}


'''Single/Multi-Line Comments'''
s2 = {
    "What symbol is used to create a single-line comment in Python?": [
        "#", 
        "//", 
        "--", 
        "/*"
    ],

    "Which of the following is a valid multi-line comment in Python?": [
        "''' This is a multi-line comment '''", 
        "// This is a multi-line comment //", 
        "/* This is a multi-line comment */", 
        "-- This is a multi-line comment --"
    ],

    "What is another name for a multi-line comment in Python?": [
        "Docstring", 
        "Block comment", 
        "Inline comment", 
        "Metadata string"
    ],

    "Which of the following statements about comments in Python is TRUE?": [
        "Comments are ignored by the interpreter", 
        "Comments must always be at the beginning of a script", 
        "Python requires comments for every function", 
        "Comments are executed like normal code"
    ],

    "What is the main purpose of using comments in Python code?": [
        "To document and explain the code", 
        "To speed up code execution", 
        "To add debugging instructions", 
        "To prevent syntax errors"
    ],

    "Which shortcut can be used in VS Code to quickly comment or uncomment lines of code?": [
        "Ctrl + /", 
        "Alt + C", 
        "Shift + #", 
        "Ctrl + Shift + C"
    ],

    "Which of the following is NOT a correct way to write a comment in Python?": [
        "-- This is a comment", 
        "# This is a comment", 
        "''' This is a comment '''", 
        "\"\"\" This is a comment \"\"\""
    ],

    "How does the Python interpreter treat comments in a script?": [
        "It ignores them", 
        "It raises an error", 
        "It executes them as part of the code", 
        "It prints them as output"
    ],

    "Which of the following is a best practice when writing comments in Python?": [
        "Write clear and concise comments to improve readability", 
        "Write comments for every single line of code", 
        "Use comments to store unused code indefinitely", 
        "Avoid using comments to keep the code shorter"
    ],

    "What type of comments are typically used to provide documentation for functions in Python?": [
        "Docstrings", 
        "Single-line comments", 
        "XML comments", 
        "HTML comments"
    ]
}


'''First Program: Console Output'''
s3 = {
"Which function is used to display output in the Python console?": [
    "print()", 
    "display()", 
    "echo()", 
    "output()"
],

"What is the correct syntax to print 'Hello, World!' in Python?": [
    'print("Hello, World!")', 
    'echo("Hello, World!")', 
    'display("Hello, World!")', 
    'print Hello, World!'
],

"What type of data is 'Hello World' in the statement `print('Hello World')`?": [
    "String", 
    "Integer", 
    "Boolean", 
    "List"
],

'''What will be the output of the following Python code?

print(\"Hello\")
print(\"World\")

''': [
    "Hello\nWorld", 
    "Hello World", 
    "Hello, World!", 
    "HelloWorld"
],

"Which of the following statements about the `print()` function is TRUE?": [
    "It sends output to the standard output (stdout)", 
    "It can only print numbers", 
    "It requires a return statement", 
    "It is not a built-in function"
],

"What is the purpose of using quotes around 'Hello World' in the `print()` function?": [
    "To define it as a string", 
    "To mark it as a comment", 
    "To execute it as a command", 
    "To concatenate two values"
],

"What happens if you run `print(Hello World)` without quotes?": [
    "It results in a NameError", 
    "It prints 'Hello World' correctly", 
    "It prints 'Hello' and 'World' separately", 
    "It asks for user input"
],

"Which of the following is a correct way to print multiple items in one statement?": [
    'print("Hello", "World")', 
    'print("Hello" + "World")', 
    'print("Hello" "World")', 
    'print("Hello". "World")'
],

'''What will be the output of the following code?

print("Python", "is", "fun", sep="-") 

''': [
    "Python-is-fun", 
    "Python is fun", 
    "Python-is-fun-", 
    "Pythonisfun"
],

"What is the default separator between values when multiple arguments are passed to `print()`?": [
    "A space", 
    "A comma", 
    "A newline", 
    "No separator"
]
}

'''First Program: User Input'''
s4 = {
'''Which function is used to handle input from the user in Python?''': [
    "input()", 
    "read()", 
    "get_input()", 
    "scan()"
],

'''What happens when the input() function is called in a Python program?''': [
    "The program pauses and waits for user input", 
    "The program immediately proceeds", 
    "It raises an error", 
    "It executes other code in parallel"
],

'''What will the input() function return?''': [
    "The text entered by the user", 
    "An integer", 
    "A boolean value", 
    "A float"
],

'''What does placing a string inside the input() function do?''': [
    "It displays a prompt message to the user", 
    "It automatically validates the input", 
    "It stores the input in a variable", 
    "It converts the input into an integer"
],

'''What is the result when the following code is executed?

input("Type your input: ")
''': [
    "The program pauses and waits for user input", 
    "It prints 'Type your input:'", 
    "It automatically stores input in a variable", 
    "It throws an error"
],

'''What will be the output of the following code after user input is given?

print(input("Type your input: "))
''': [
    "The user input will be printed to the console", 
    "The program will stop", 
    "It will ask for input again", 
    "It will print the prompt message"
],
'''What is the correct way to print the user input after calling input()?''': [
    "print(input())", 
    "input(print())", 
    "output(input())", 
    "return(print())"
],

'''What does the term "stdin" refer to in Python?''': [
    "Standard Input", 
    "Standard Output", 
    "Standard Error", 
    "System Input"
],
'''What happens when the input() function is used without any arguments?''': [
    "The program waits for user input without displaying any prompt", 
    "It raises an error", 
    "It automatically fills in a default value", 
    "It exits the program"
],

'''Which of the following will correctly prompt a user to enter their age and store the input in a variable?''': [
    'age = input("Enter your age: ")', 
    'input = age("Enter your age")', 
    'input("Enter your age: ") = age', 
    'input("Enter your age: ").store(age)'
]
}

"""Executing a Python Program"""
s5 = {
'''What does source code refer to in Python?''': [
    "The human-readable set of instructions written by the programmer", 
    "The machine-readable bytecode", 
    "The executable file generated after compilation", 
    "The final output of a Python program"
],

'''Why is Python source code not immediately readable by the computer?''': [
    "Because it needs to be translated into machine code", 
    "Because it is stored in a .pyc file", 
    "Because it is automatically executed without translation", 
    "Because it contains errors"
],

'''What is the program used to translate Python source code into a form the computer can understand?''': [
    "The Python interpreter", 
    "The Python compiler", 
    "The Python Virtual Machine", 
    "The Python debugger"
],

'''Which program is used to execute Python code on Windows?''': [
    "python.exe", 
    "python3", 
    "python2", 
    "python-windows"
],

'''Which program is used to execute Python code on Mac/Linux?''': [
    "python3", 
    "python.exe", 
    "python2", 
    "python-mac"
],
'''What is the file extension used for storing Python source code?''': [
    ".py", 
    ".txt", 
    ".pyc", 
    ".exe"
],

'''What does the Python interpreter do with the source code when executed?''': [
    "Converts it into bytecode", 
    "Directly executes the source code", 
    "Translates it into machine code", 
    "Stores it in the pycache directory"
],

'''Where is the bytecode stored after the Python interpreter processes the source code?''': [
    "In a .pyc file inside the pycache directory", 
    "In a .txt file", 
    "In the Python source file", 
    "In the Python Virtual Machine"
],

'''Which component of the Python execution process translates bytecode into machine code?''': [
    "Python Virtual Machine (PVM)", 
    "Python interpreter", 
    "CPU", 
    "Python compiler"
],

'''What happens after the machine code is generated by the Python Virtual Machine?''': [
    "It is processed by the CPU to generate the output", 
    "It is stored in a .pyc file", 
    "It is executed by the Python interpreter", 
    "It is passed to the Python Virtual Machine"
],
'''What is the first step in executing a Python program?''': [
    "Invoke the interpreter through the command line and provide the filename as an argument", 
    "Write the program in a text editor", 
    "Run the Python interpreter without any arguments", 
    "Save the Python code in a .pyc file"
],

'''What is the correct syntax for running a Python program on Windows?''': [
    "python <filename>", 
    "python3 <filename>", 
    "py <filename>", 
    "py3 <filename>"
],

'''What is the correct syntax for running a Python program on Linux/MacOS?''': [
    "python3 <filename>", 
    "python <filename>", 
    "py <filename>", 
    "py3 <filename>"
]
}

'''Python Installation Path'''
s6 = {
'''Where is Python typically installed on Windows?''': [
    "C:\\Program Files\\Python3xx", 
    "C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python3xx", 
    "C:\\Python", 
    "C:\\Windows\\System32\\Python3xx"
],

'''Where is Python usually installed for a specific user on Windows?''': [
    "C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python3xx", 
    "C:\\Program Files\\Python3xx", 
    "C:\\Python\\Python3xx", 
    "C:\\Windows\\System32\\Python3xx"
],

'''How can you check the installed Python version on Windows?''': [
    "> python --version", 
    "$ python3 --version", 
    "> python version", 
    "$ python --version"
 ],

'''What is the default installation path for Python on Linux/MacOS?''': [
    "/usr/bin/python3", 
    "/usr/local/bin/python3", 
    "/bin/python", 
    "/home/user/python3"
],

'''How can you check the installed Python version on Linux/MacOS?''': [
    "python3 --version", 
    "python --version", 
    "version python3", 
    "python3 -v"
],

'''How can you execute a Python program on Linux/MacOS?''': [
    "python3 filename.py", 
    "python filename.py", 
    "python3 execute filename.py", 
    "run python3 filename.py"
]

}

'''You are experiencing an Error!'''
s7 = {
'''What type of error occurs when code violates the rules of the programming language's syntax?''': [
    "Syntax/Compile Time Errors", 
    "Runtime Errors", 
    "Logical Errors", 
    "ID 10 T Errors"
],

'''What type of error occurs after the program is successfully compiled but fails during execution due to an impossible operation?''': [
    "Runtime Errors", 
    "Syntax/Compile Time Errors", 
    "Logical Errors", 
    "PEBKAC Errors"
],

'''Which type of error happens when the program runs but produces incorrect results due to issues with the program's logic?''': [
    "Logical Errors", 
    "Syntax/Compile Time Errors", 
    "Runtime Errors", 
    "ID 10 T Errors"
],

'''What does PEBKAC stand for in the context of errors?''': [
    "Problem Exists Between the Keyboard and Chair", 
    "Program Execution Between Keyboard and Chair", 
    "Problematic Error Between Keyboard and Computer", 
    "Program Error Because of Keyboard and Computer"
],

'''What is an ID 10 T error caused by?''': [
    "User mistake", 
    "System malfunction", 
    "External factors", 
    "Syntax violation"
]

}

'''Syntax/Compile Time Errors'''
s8 = {
'''What is the first step in fixing a Syntax/Compile Time Error?''': [
    "Read the error output", 
    "Check for runtime errors", 
    "Rewrite the code from scratch", 
    "Ask for help from a friend"
],

'''In the following example, what is the issue with the code?

Traceback (most recent call last):
  File "<path to your .py file>", line 2, in <module>
    Print("Hello World")
    ^^^^^
NameError: name 'Print' is not defined. Did you mean: 'print'?

''': [
    "The function name is capitalized incorrectly", 
    "There is a missing parenthesis", 
    "The print statement is missing quotes", 
    "The program has no error"
],

'''What key information should you look for in error output when trying to fix a Syntax/Compile Time Error?''': [
    "Line number and specific error info", 
    "Program version and execution time", 
    "The number of characters in the code", 
    "The time it takes to compile the code"
],

'''What error is shown when there is a typo in a function name, such as using 'Print' instead of 'print'?''': [
    "NameError", 
    "SyntaxError", 
    "TypeError", 
    "RuntimeError"
],

'''In the example, what is the suggested fix for the error "NameError: name 'Print' is not defined. Did you mean: 'print'?"''': [
    "Use 'print' instead of 'Print'", 
    "Use a different function", 
    "Add an extra parenthesis", 
    "Remove the quotes"
]
}

'''Runtime Errors'''
s9 = {
'''What is a Runtime Error in Python?''': [
    "An error that occurs during execution due to an invalid operation", 
    "An error that occurs when there is a syntax mistake", 
    "An error caused by missing libraries", 
    "An error that prevents code from being compiled"
],

'''
What is the cause of the error in the following code?

print(5 / 0)


Traceback (most recent call last):
  File "<path to your .py file>", line 1, in <module>
    print(5 / 0)
           ~~^~~
ZeroDivisionError: division by zero

''' : [
    "The program attempted to divide by zero", 
    "The program attempted an invalid operation", 
    "There is a syntax error", 
    "There is an unexpected input"
],

'''In the following code, what is the issue?

my_list = ["a","b","c"]
print(my_list[3])


Traceback (most recent call last):
  File "<path to your .py file>", line 4, in <module>
    print(my_list[3])
          ~~~~~~~^^^
IndexError: list index out of range

''': [
    "The list index is out of range", 
    "The list is empty", 
    "The list contains invalid data", 
    "The print statement is missing parentheses"
],

'''What is the first step in fixing a Runtime Error?''': [
    "Read the error output", 
    "Check for syntax errors", 
    "Re-run the program multiple times", 
    "Use debugging tools"
],

'''In the given example, what specific error is reported when accessing an invalid index in the list?''': [
    "IndexError", 
    "TypeError", 
    "KeyError", 
    "FileNotFoundError"
]
}

'''Logical Errors'''
s10 = {
    '''What is a logical error in programming?''': [
    "When code runs without syntax or runtime errors but doesn't produce the expected output", 
    "When there is a syntax error", 
    "When an exception occurs during code execution", 
    "When a variable is not defined"
],

'''What is the first step to fixing logical errors in your code?''': [
    "Debugging", 
    "Rewriting the entire code", 
    "Using a new programming language", 
    "Ignoring the error"
],

'''What debugging method is commonly used by beginners to fix logical errors?''': [
    "Using print() statements", 
    "Using a debugger tool", 
    "Rewriting code with different logic", 
    "Reinstalling the IDE"
],

'''What can be difficult about fixing logical errors compared to other types of errors?''': [
    "The code runs without crashing, but the output is incorrect", 
    "The code always crashes", 
    "The syntax is incorrect", 
    "The program doesn't start at all"
],

'''Why might a beginner choose print() debugging when trying to fix a logical error?''': [
    "It is simple and doesn't require advanced tools", 
    "It automatically fixes the logical error", 
    "It helps to find syntax errors", 
    "It is faster than rewriting the code"
]

}



# {question : [answer, *options]}
questions.update(s1)
questions.update(s2)
questions.update(s3)
questions.update(s4)
questions.update(s5)
questions.update(s6)
questions.update(s7)
questions.update(s8)
questions.update(s9)
questions.update(s10)







if __name__ == "__main__":

    for question, options in questions.items():
        print(question, *options, sep="\n")
        input()