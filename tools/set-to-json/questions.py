'''Place preformmated questions and answers in the dictionary "questions" below.'''

setname = "set12"


questions = {}

'''General Syntax'''
s1 = {
"Which of the following best defines 'syntax'?": [
    "Rules for writing a language",
    "A type of programming language",
    "A debugging technique",
    "A compiler feature"
],
"How is source code executed in Python?": [
    "Top to bottom, left to right, line by line",
    "Bottom to top, right to left",
    "Randomly based on function calls",
    "Only after compilation"
],
"What is required in Python syntax to define blocks of code?": [
    "Indentation",
    "Braces `{}`",
    "Semicolons `;`",
    "Parentheses `()`"
],
"What happens when indentation is incorrect in Python?": [
    "It results in an error",
    "It is ignored",
    "It is automatically fixed",
    "It only affects performance"
],
"Which symbol is primarily used for indentation in Python?": [
    "Spaces or tabs",
    "Semicolons `;`",
    "Brackets `[]`",
    "Curly braces `{}`"
],
"What type of error is caused by incorrect indentation in Python?": [
    "IndentationError",
    "SyntaxError",
    "RuntimeError",
    "LogicError"
],
'''Review the code snippet below, which print statement will be executed first?

print("a"); print("b")
print("c")

print("d")
''':[
    "a",
    "b",
    "c",
    "d"  
]

}

'''Every Opening Needs a Closing'''

s2 ={
"Which of the following symbols in Python must always have a closing counterpart?": [
    "(), [], {}",
    "`@`, `#`, `!`",
    "`?`, `:`",
    "`%`, `&`"
],
"Which of the following is an example of correctly paired symbols in Python?": [
    "'Hello' or (1, 2, 3)",
    "'Hello or (1, 2, 3'",
    "'[1, 2, 3'",
    "'{key: value'"
],
"What will happen if an opening parenthesis `(` is not closed properly?": [
    "SyntaxError",
    "The code will run normally",
    "Python will automatically close it",
    "It will be ignored"
],

'''The following code snippet results in an error, which of the following correctly identifies the issue?

print("Hello World"
''': [
    "A missing ')'",
    "A missing '\"'",
    "A missing '('",
    "A missing '}'"
],
'''The following code snippet results in an error, which of the following correctly identifies the issue?

numbers = [1, 2, 3, 4{
''': [
    "A missing ']'",
    "A missing '['",
    "A missing '{'",
    "A missing '('"
],
'''The following code snippet results in an error, which of the following correctly identifies the issue?

data = 'key': 'value' }
''': [
    "A missing '{'",
    "A missing '}')",
    "A missing '}'",
    "A missing '['"
],
'''The following code snippet results in an error, which of the following correctly identifies the issue?

if (x > 0: 
    print('Positive')
''': [
    "A missing ')'",
    "A missing ':')",
    "A missing '('",
    "A missing 'if'"
],
'''The following code snippet results in an error, which of the following correctly identifies the issue?

def my_function(param: 
    return param * 2
''': [
    "A missing ')'",
    "A missing ':'",
    "A missing '('",
    "A missing 'def'"
],
'''The following code snippet results in an error, which of the following correctly identifies the issue?

    if x == 10 :
print("Ten")
''': [
    "IndentationError: unexpected indent",
    "A missing ':'",
    "A missing 'if'",
    "IndentationError: expected an indented block"
],
'''The following code snippet results in an error, which of the following correctly identifies the issue?

print("Hello World"
''': [
    "A missing ')'",
    "A missing '('",
    "A missing '{'",
    "A missing '\"'"
],
'''The following code snippet results in an error, which of the following correctly identifies the issue?

numbers = [1, 2, 3, 4)
''': [
    "Replace ')' with ']'",
    "Replace '[' with '('",
    "Replace ')' with '{'",
    "Replace '(' with '['"
],
'''The following code snippet results in an error, which of the following correctly identifies the issue?

def test_function():
print('Testing')
''': [
    "IndentationError: expected an indented block",
    "A missing ':'",
    "A missing 'def'",
    "A missing '()'"
],
'''The following code snippet results in an error, which of the following correctly identifies the issue?

if (x > 0: 
    print("Positive")
''': [
    "A missing ')'",
    "A missing '('",
    "A missing ':'",
    "IndentationError: expected an indented block"
]
}

s3 = {
'''Is the line 'elif x == 2:' inside or outside the 'if x == 1:' code block?

if x == 1:
    print("x is 1")
elif x == 2:
    print("x is 2")
''' : [
    "Outside",
    "Inside",
    "Unclear",
    "Not part of any block"
],

'''Is the line 'else:' inside or outside the 'if x == 1:' code block?

if x == 1:
    print("x is 1")
else:
    print("x is neither 1 nor 2")
''' : [
    "Outside"
    "Inside",
    "Unclear",
    "Not part of any block"
],

'''Is the line 'while x < 5:' inside or outside the 'if x == 1:' code block?

if x == 1:
    print("x is 1")
while x < 5:
    print(x)
    x += 1
''' : [
    "Outside",
    "Inside",
    "Unclear",
    "Not part of any block"
],

'''Is the line 'for i in range(3):' inside or outside the 'while x < 5:' code block?

while x < 5:
    print(x)
    for i in range(3):
        print(i)
    x += 1
''' : [
    "Inside",
    "Outside",
    "Unclear",
    "Not part of any block"
],

'''Is the line 'def greet(name):' inside or outside the 'for i in range(3):' code block?

for i in range(3):
    print(i)
def greet(name):
    print(f"Hello, {name}!")
''' : [
    "Outside",
    "Inside",
    "Unclear",
    "Not part of any block"
],

'''Is the line 'class Dog:' inside or outside the 'def greet(name):' code block?

def greet(name):
    print(f"Hello, {name}!")
class Dog:
    def __init__(self, name):
        self.name = name
''' : [
    "Outside",
    "Inside",
    "Unclear",
    "Not part of any block"
],

'''Is the line '    def __init__(self, name):' inside or outside the 'class Dog:' code block?

class Dog:
    def __init__(self, name):
        self.name = name
''' : [
    "Inside",
    "Outside",
    "Unclear",
    "Not part of any block"
],

'''Is the line '    print("Hello, World!")' inside or outside the 'while x < 5:' code block?

while x < 5:
    print(x)
    print("Hello, World!")
    x += 1
''' : [
    "Inside",
    "Outside",
    "Unclear",
    "Not part of any block"
],

'''Is the line '    print(i)' inside or outside the 'for i in range(3):' code block?

for i in range(3):
    print(i)
print("Loop ended")
''' : [
    "Inside",
    "Outside",
    "Unclear",
    "Not part of any block"
],

'''Is the line '    print(x)' inside or outside the 'else:' code block?

if x == 1:
    print("x is 1")
else:
    print(x)
''' : [
    "Inside",
    "Outside",
    "Unclear",
    "Not part of any block"
],

'''Is the line '    print("Done")' inside or outside the 'while x < 5:' code block?

while x < 5:
    print(x)
print("Done")
''' : [
    "Outside",
    "Inside",
    "Unclear",
    "Not part of any block"
],

'''Is the line 'def greet(name):' inside or outside the 'class Dog:' code block?

class Dog:
    def __init__(self, name):
        self.name = name
def greet(name):
    print(f"Hello, {name}!")
''' : [
    "Outside",
    "Inside",
    "Unclear",
    "Not part of any block"
],

'''Is the line '    print(f"Hello, {name}!")' inside or outside the 'def greet(name):' code block?

def greet(name):
    print(f"Hello, {name}!")
print("Function defined")
''' : [
    "Inside",
    "Outside",
    "Unclear",
    "Not part of any block"
],

'''Is the line 'while x < 5:' inside or outside the 'if x == 1:' code block?

if x == 1:
    print("x is 1")
while x < 5:
    print(x)
    x += 1
''' : [
    "Outside",
    "Inside",
    "Unclear",
    "Not part of any block"
],

'''Is the line 'elif x == 2:' inside or outside the 'if x == 1:' code block?

if x == 1:
    print("x is 1")
elif x == 2:
    print("x is 2")
''' : [
    "Outside",
    "Inside",
    "Unclear",
    "Not part of any block"
],

'''Is the line 'for i in range(5):' inside or outside the 'else:' code block?

if x == 1:
    print("x is 1")
else:
    for i in range(5):
        print(i)
''' : [
    "Inside",
    "Outside",
    "Unclear",
    "Not part of any block"
],

'''Is the line '    print(i)' inside or outside the 'for i in range(5):' code block?

for i in range(5):
    print(i)
''' : [
    "Inside",
    "Outside",
    "Unclear",
    "Not part of any block"
],

'''Is the line 'def greet(name):' inside or outside the 'class Dog:' code block?

class Dog:
    def greet(self, name):
        print(f"Hello, {name}!")
def greet(name):
    print(f"Goodbye, {name}!")
''' : [
    "Outside",
    "Inside",
    "Unclear",
    "Not part of any block"
],

'''Is the line '    print(f"Hello, {name}!")' inside or outside the 'def greet(self, name):' code block?

class Dog:
    def greet(self, name):
        print(f"Hello, {name}!")
''' : [
    "Inside",
    "Outside",
    "Unclear",
    "Not part of any block"
]
}

s3 = {
'''What is the preferred indentation style in Python according to PEP 8?
''' : [
    "4-space indentation",
    "2-space indentation",
    "Tab indentation",
    "No indentation"
],

'''What is the maximum line length recommended in PEP 8?
''' : [
    "79 characters",
    "80 characters",
    "100 characters",
    "120 characters"
],

'''How should functions and classes be separated according to PEP 8?
''' : [
    "Use blank lines",
    "No blank lines",
    "Use tabs",
    "Indent functions and classes equally"
],

'''Where should comments be placed in Python code according to PEP 8?
''' : [
    "On their own line",
    "At the end of a line of code",
    "Inside parentheses",
    "Within the function signature"
],

'''What should be used to document functions and classes according to PEP 8?
''' : [
    "Docstrings",
    "Single-line comments",
    "Inline comments",
    "Type annotations"
],

'''Which of the following is the correct way to name functions in Python according to PEP 8?
''' : [
    "lower_snake_case",
    "UpperCamelCase",
    "camelCase",
    "PascalCase"
],

'''Which of the following is the correct way to name classes in Python according to PEP 8?
''' : [
    "UpperCamelCase",
    "lower_snake_case",
    "camelCase",
    "PascalCase"
],

'''What should be used around operators in Python according to PEP 8?
''' : [
    "Spaces around operators",
    "No spaces around operators",
    "Tabs around operators",
    "Underscores around operators"
],

'''How should commas be spaced according to PEP 8?
''' : [
    "Space after commas",
    "No space after commas",
    "Tabs after commas",
    "Underscores after commas"
],

'''What should be used inside bracketing constructs according to PEP 8?
''' : [
    "No spaces inside brackets",
    "Spaces inside brackets",
    "Tabs inside brackets",
    "Underscores inside brackets"
],

'''What is the correct way to write method arguments according to PEP 8?
''' : [
    "Use self as the first argument in methods",
    "Use 'this' as the first argument in methods",
    "Use 'args' as the first argument in methods",
    "Use 'self' for static methods"
],
'''How should the body of a function or class be indented according to PEP 8?
''' : [
    "4 spaces",
    "2 spaces",
    "1 tab",
    "No indentation"
],

'''What is the recommended way to separate larger blocks of code inside functions according to PEP 8?
''' : [
    "Use blank lines",
    "Use comments",
    "Use tabs",
    "No separation"
],

'''Which of the following is the correct way to use docstrings in Python according to PEP 8?
''' : [
    "Use triple quotes for docstrings",
    "Use single quotes for docstrings",
    "Use comments for docstrings",
    "No docstrings"
],
'''The following code violates PEP 8. What is the issue?

def MyFunction():
    pass
''' : [
    "Function name should be in lower_snake_case",
    "Function name should be in UpperCamelCase",
    "Indentation is incorrect",
    "Missing docstring"
],

'''The following code violates PEP 8. What is the issue?

if x== 1:
    print(x)
''' : [
    "Missing spaces around the operator",
    "Too many spaces around the operator",
    "Incorrect indentation",
    "No blank line after 'if' statement"
],

'''The following code violates PEP 8. What is the issue?

x=2+3
''' : [
    "Missing spaces around the operator",
    "Too many spaces around the operator",
    "Incorrect indentation",
    "No need to use spaces"
],

'''The following code violates PEP 8. What is the issue?

def exampleFunction():
    pass # this is a comment
''' : [
    "Comment should be on a new line",
    "Function name should be in lower_snake_case",
    "Missing spaces after function name",
    "Indentation is incorrect"
],

'''The following code violates PEP 8. What is the issue?

a=1
b = 2
''' : [
    "No spaces around the = operator",
    "Inconsistent indentation around the assignment operator",
    "Too many spaces around the assignment operator",
    "Spacing is correct"
],

'''The following code violates PEP 8. What is the issue?

def my_function(a,b):
    return a + b
''' : [
    "No spaces after commas",
    "Spaces should be around the operator",
    "Function name should be UpperCamelCase",
    "No docstring for the function"
],

'''The following code violates PEP 8. What is the issue?

x = [1,2,3,4]
''' : [
    "No spaces after commas",
    "Too many spaces after commas",
    "Spaces should be inside brackets",
    "Spacing is correct"
],

'''The following code violates PEP 8. What is the issue?

class myclass:
    pass
''' : [
    "Class name should be UpperCamelCase",
    "Class name should be lower_snake_case",
    "Class name should be PascalCase",
    "Missing docstring"
],

'''The following code violates PEP 8. What is the issue?

def my_function(  a , b ):
    return a+b
''' : [
    "Spaces directly inside of bracketing constructs",
    "Spaces should be removed after commas",
    "Spacing is correct",
    "No spaces around operators"
],

'''The following code violates PEP 8. What is the issue?

def example(x,y):
    return x + y
''' : [
    "No space after the comma",
    "Extra spaces around the parentheses",
    "Function name should be in UpperCamelCase",
    "Missing docstring"
],

'''The following code violates PEP 8. What is the issue?

def example_function():
    pass
print("Hello")
''' : [
    "No blank line between code blocks",
    "Extra indentation for print statement",
    "Missing docstring",
    "The function body is not indented"
]
}

s4 = {
'''Which of the following is a universal truth about programming?
''' : [
    "Syntax must be perfectly written",
    "Syntax can be written loosely",
    "Syntax is never important",
    "Syntax doesn't matter"
],

'''What is the key takeaway from the universal programming truth about software?
''' : [
    "All software is broken",
    "Software is always bug-free",
    "Software should never be tested",
    "Software is perfect at all times"
],

'''What happens if the syntax of a program is wrong?
''' : [
    "The program will not run",
    "The program will run with warnings",
    "The program will automatically fix the syntax",
    "The program will ignore the error"
]
}




# {question : [answer, *options]}
questions.update(s1)
questions.update(s2)
questions.update(s3)
questions.update(s4)
# questions.update(s5)
# questions.update(s6)
# questions.update(s7)
# questions.update(s8)
# questions.update(s9)
# questions.update(s10)







if __name__ == "__main__":
    print(len(questions))

    # for question, options in questions.items():
    #     print(question, *options, sep="\n")
    #     input()