'''Place preformmated questions and answers in the dictionary "questions" below.'''

setname = "set16"


questions = {}

'''Quick Start Guide To Functions'''
s1 = {
"""What is a function definition in programming?""": [
    "A block of code that specifies a sequence of statements to perform a specific task", 
    "A single line of code that performs an operation", 
    "A statement that defines variables", 
    "A command that runs the program"
], 
"""What are parameters in a function?""": [
    "Variables inside the parentheses used to pass information into functions", 
    "The actual values passed to the function", 
    "The name of the function", 
    "A block of executable code inside the function"
], 
"""What is the purpose of the return statement in a function?""": [
    "To return the result of a function to the caller", 
    "To call another function", 
    "To define the parameters of a function", 
    "To specify the function name"
], 
"""What does a function call do?""": [
    "Executes the function and returns the result", 
    "Defines the function", 
    "Specifies the function parameters", 
    "Passes the parameters to the function"
], 
"""What is an argument in a function call?""": [
    "The actual values or data passed to a function's parameters", 
    "The function name", 
    "The return value from the function", 
    "The code inside the function body"
], 
"""What happens when you call a function with the wrong number of arguments?""": [
    "An error occurs", 
    "The function will return None", 
    "The function will still execute with default values", 
    "The program will continue without any issues"
], 
"""Which of the following is NOT part of a function definition?""": [
    "The actual values passed when calling the function", 
    "The function's name", 
    "The parameters inside parentheses", 
    "The function body containing executable code"
], 
"""How are parameters passed into a function?""": [
    "Inside the parentheses when defining the function", 
    "Inside the function body as global variables", 
    "Through return statements", 
    "Through a print statement"
], 
"""What does the return statement allow a function to do?""": [
    "Return a result to the caller", 
    "Execute another function", 
    "Define the function's parameters", 
    "Return a value to the function's body"
], 
"""Can a function have no parameters?""": [
    "Yes, it can have no parameters", 
    "No, it must have at least one parameter", 
    "Yes, but only if there is a return statement", 
    "No, it must have parameters"
],
"""What is the name of the function in the following code?

def add(a, b):
    return a + b

""": [
    "add", 
    "a", 
    "b", 
    "return"
], 

"""What are the parameters of the function 'add'?

def add(a, b):
    return a + b

""": [
    "a and b", 
    "add and return", 
    "a, b, and return", 
    "2 and 4"
], 

"""In the function call `add(2, 2)`, what are the arguments?

add(2, 2)

""": [
    "2 and 2", 
    "a and b", 
    "add and 2", 
    "None"
], 

"""In the function definition

def add(a, b):
    return a + b

what does 'a' and 'b' represent?

""": [
    "Parameters", 
    "Arguments", 
    "Return values", 
    "Function name"
], 

"""What is returned when the function `add(5, 4)` is called?

add(5, 4)

""": [
    "9", 
    "4", 
    "12", 
    "None"
], 

"""What is the purpose of the 'return' keyword in the function definition?

def add(a, b):
    return a + b

""": [
    "To specify the result to be returned to the caller", 
    "To define parameters", 
    "To call the function", 
    "To print the result"
], 

"""In the statement

a = add(2, 2)

what is the result stored in variable 'a'?

""": [
    "4", 
    "2", 
    "None", 
    "a"
], 

"""What does the function call `add(2, 10)` return?

add(2, 10)

""": [
    "12", 
    "2", 
    "10", 
    "None"
], 

"""What does the print statement print when calling `add(5, 4)`?

print(add(5, 4))

""": [
    "9", 
    "4", 
    "12", 
    "None"
], 

"""What is the purpose of the parentheses in a function call, such as in `add(2, 2)`?

add(2, 2)

""": [
    "To pass arguments to the function", 
    "To define the function", 
    "To specify the return value", 
    "To store the result"
],
}

'''The print call'''
s2 = {
"""What is the purpose of the `print()` function in Python?""": [
    "To send data to standard output (stdout)", 
    "To store data in a file", 
    "To process data", 
    "To define a function"
],

"""Which of the following is the correct syntax for the `print()` function?""": [
    "print(*values, sep=' ', end='\\n', file=None, flush=False)", 
    "print(values, sep, end, file, flush)", 
    "print(*values, sep, file, flush)", 
    "print(values, file, flush)"
],

"""Which of the following is the default value for the `end` parameter in the `print()` function?""": [
    "\\n", 
    " ", 
    "", 
    "end"
],

"""What does the `sep` parameter in the `print()` function control?""": [
    "The separator between the printed values", 
    "The end character after the printed values", 
    "The file where the output is written", 
    "The flushing behavior of the output"
],

"""What happens if the `file` parameter is set to a file object in the `print()` function?""": [
    "The output is written to the specified file", 
    "The output is printed on the console", 
    "The output is ignored", 
    "An error is raised"
],

"""What does the `flush` parameter do in the `print()` function?""": [
    "Immediately flushes the output buffer", 
    "Delays the printing", 
    "Stops the program", 
    "Changes the separator"
],

"""What will be the output if `sep=" | "` is used in the `print()` function?""": [
    "It separates the printed values with a pipe (|)", 
    "It concatenates the values with a space", 
    "It concatenates the values with a comma", 
    "It prints the values in a list"
],

"""Which of the following is NOT an optional parameter in the `print()` function?""": [
    "values",
    "sep", 
    "end", 
    "file"
],

"""What is the default value of the `end` parameter in the `print()` function?""": [
    "\\n", 
    " ", 
    "end", 
    "None"
],

"""What does the `print()` function send its output to by default?""": [
    "Standard output (stdout)", 
    "A file", 
    "The internet", 
    "A database"
],
"""What is the default destination for output generated by a Python program?""": [
    "Standard output (stdout)", 
    "A file", 
    "A database", 
    "An external server"
],

"""Which of the following parameters in the `print()` function controls the separator between values?""": [
    "sep", 
    "end", 
    "file", 
    "flush"
],

"""What happens if the `end` parameter in the `print()` function is set to an empty string?""": [
    "The cursor stays on the same line", 
    "The output is flushed immediately", 
    "The separator between values is changed", 
    "The output is written to a file"
],

"""What is the default value for the `end` parameter in the `print()` function?""": [
    "\\n", 
    " ", 
    "", 
    "None"
],

"""Which of the following will change the separator between printed values to a pipe (|)?""": [
    "print('Hello', 'World', sep='|')", 
    "print('Hello', 'World', end='|')", 
    "print('Hello', 'World', file='output.txt')", 
    "print('Hello', 'World', flush=True)"
],

"""Which parameter in the `print()` function controls whether the output buffer is immediately flushed?""": [
    "flush", 
    "sep", 
    "end", 
    "file"
],

"""What is the effect of setting `flush=True` in the `print()` function?""": [
    "The output is printed immediately without buffering", 
    "The separator between values is changed", 
    "The output is written to a file", 
    "The cursor stays on the same line"
],

"""Which of the following is a correct use of the `file` parameter in the `print()` function?""": [
    "print('Hello World', file='output.txt')", 
    "print('Hello World', file='stdout')", 
    "print('Hello World', file=True)", 
    "print('Hello World', file=None)"
],

"""What is the output of the following code? `print("Hello", "World", sep="*")`""": [
    "Hello*World", 
    "Hello World", 
    "Hello|World", 
    "Hello:World"
],

"""In which situation would you use the `flush=True` argument in the `print()` function?""": [
    "When you want to see the output in real-time", 
    "When you need to save the output to a file", 
    "When you want to change the separator", 
    "When you want to add a newline after printing"
],
}

''' The input() function call'''
s3 = {
"""What does the `input()` function do in Python?""": [
    "Pauses the program and reads user input from standard input", 
    "Prints output to the console", 
    "Performs mathematical operations", 
    "Reads data from a file"
],

"""What is the default return type of the `input()` function?""": [
    "str", 
    "int", 
    "float", 
    "complex"
],

"""Which of the following parameters in the `input()` function specifies what is printed before accepting input?""": [
    "prompt", 
    "value", 
    "message", 
    "separator"
],

"""How can the prompt be provided in the `input()` function?""": [
    "By position or keyword", 
    "Only by keyword", 
    "Only by position", 
    "By default, it cannot be changed"
],

"""How can the user input be stored after being read by `input()`?""": [
    "In a variable", 
    "In a list", 
    "In a function", 
    "In a file"
],

"""Which constructor can be used to convert a string input to an integer in Python?""": [
    "int()", 
    "str()", 
    "float()", 
    "complex()"
],

"""Which constructor can be used to convert a string input to a floating-point number in Python?""": [
    "float()", 
    "int()", 
    "str()", 
    "complex()"
],

"""How can complex numbers be created from user input in Python?""": [
    "Using the `complex()` constructor with real and imaginary parts", 
    "Using the `float()` constructor with real and imaginary parts", 
    "Using the `int()` constructor with real and imaginary parts", 
    "Using the `str()` constructor with real and imaginary parts"
],

"""What will the following code output? 

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print(x + y)

""": [
    "The sum of the two numbers", 
    "The product of the two numbers", 
    "The difference of the two numbers", 
    "An error"
],

"""What is the purpose of using `int()`, `float()`, and `complex()` after calling `input()`?""": [
    "To convert the string input into a specific numeric type", 
    "To store the input as a string", 
    "To automatically perform calculations", 
    "To convert the input into a boolean value"
],
}

'''The len() function call'''
s4 = {
    """What does the `len()` function return when applied to a string?""": [
    "The number of characters in the string", 
    "The first character of the string", 
    "The index of the string", 
    "The ASCII value of the string"
],

"""What does `len()` return when applied to a list?""": [
    "The number of items in the list", 
    "The sum of the list", 
    "The type of the list", 
    "The first element in the list"
],

"""What will `len(["apple", "banana", "cherry"])` return?""": [
    "3", 
    "6", 
    "2", 
    "1"
],

"""How does `len()` behave when applied to a dictionary?""": [
    "It counts the number of key-value pairs", 
    "It counts the number of keys", 
    "It counts the number of values", 
    "It returns the total length of keys and values"
],

"""What will `len({"name": "Alice", "age": 30, "city": "New York"})` return?""": [
    "3", 
    "6", 
    "2", 
    "5"
],

"""How does `len()` work on nested data structures?""": [
    "It counts the top-level items", 
    "It counts all items, including nested items", 
    "It only counts the first item", 
    "It returns an error"
],

"""What will `len([["apple", "banana"], ["cherry", "date"], ["elderberry", "fig"]])` return?""": [
    "3", 
    "6", 
    "2", 
    "4"
],

"""What does `len()` return when applied to a tuple?""": [
    "The number of items in the tuple", 
    "The sum of the items in the tuple", 
    "The index of the tuple", 
    "The type of the tuple"
],

"""What will `len("Python")` return?""": [
    "6", 
    "5", 
    "7", 
    "4"
],

"""If `len()` is applied to a dictionary, which of the following is counted?""": [
    "Key-value pairs", 
    "Only keys", 
    "Only values", 
    "Nested dictionaries"
],
}

'''Type function call'''
s4 = {
"""What does the `type()` function return?""": [
    "The type of an object", 
    "The value of an object", 
    "The length of an object", 
    "The name of an object"
],

"""What will `type(5)` return?""": [
    "<class 'int'>", 
    "<class 'float'>", 
    "<class 'str'>", 
    "<class 'bool'>"
],

"""What is the result of `type(3.14)`?""": [
    "<class 'float'>", 
    "<class 'int'>", 
    "<class 'str'>", 
    "<class 'complex'>"
],

"""What does `type(True)` return?""": [
    "<class 'bool'>", 
    "<class 'int'>", 
    "<class 'str'>", 
    "<class 'float'>"
],

"""What will `type({"a","b","c"})` return?""": [
    "<class 'set'>", 
    "<class 'list'>", 
    "<class 'tuple'>", 
    "<class 'dict'>"
],

"""What does `type(type)` return?""": [
    "<class 'type'>", 
    "<class 'str'>", 
    "<class 'int'>", 
    "<class 'object'>"
],

"""What will `type(None)` return?""": [
    "<class 'NoneType'>", 
    "<class 'bool'>", 
    "<class 'int'>", 
    "<class 'str'>"
],

"""What does `type("Hello")` return?""": [
    "<class 'str'>", 
    "<class 'list'>", 
    "<class 'tuple'>", 
    "<class 'dict'>"
],

"""What will `type(len)` return?""": [
    "<class 'builtin_function_or_method'>", 
    "<class 'int'>", 
    "<class 'str'>", 
    "<class 'float'>"
],

"""What is the result of `type({"a":97,"b":98,"c":99})`?""": [
    "<class 'dict'>", 
    "<class 'list'>", 
    "<class 'tuple'>", 
    "<class 'set'>"
],
}

'''Nested Function Calls'''

s5 = {
    "What does nesting refer to in programming?": [
        "Placing one construct inside another", 
        "Repeating the same code", 
        "Combining multiple functions into one", 
        "Declaring variables within functions"
    ],
    "Which of the following constructs can be nested in Python?": [
        "All of the above", 
        "Loops", 
        "Functions", 
        "Conditionals"
    ],
    "In Python, which of the following is an example of a nested collection?": [
        "[[1, 2], [3, 4], [5, 6]]", 
        "[10, 20, 30]", 
        "{\"a\": 1, \"b\": 2}", 
        "\"hello world\""
    ],
    "Which of the following function calls occurs first in the statement `print(int(input(\"Enter a number: \")))`?": [
        "input()", 
        "int()", 
        "print()", 
        "None of the above"
    ],
    "Arrange the following nested function calls in the order they execute: `print(str(int(input(\"Enter a number: \"))))`": [
        "input() -> int() -> str() -> print()", 
        "str() -> input() -> int() -> print()", 
        "int() -> str() -> print() -> input()", 
        "print() -> input() -> str() -> int()"
    ],
    "In the nested function call `round(abs(float(input())))`, which function is executed first?": [
        "input()", 
        "float()", 
        "abs()", 
        "round()"
    ],
    "Which function call occurs second in the nested function call `sum(map(int, input().split()))`?": [
        "input()", 
        "map()", 
        "int()", 
        "sum()"
    ],
    "Which of the following is the correct order of execution for the nested function call `sorted(map(int, input().split()))`?": [
        "input() -> split() -> map() -> int() -> sorted()", 
        "input() -> split() -> int() -> map() -> sorted()", 
        "map() -> split() -> input() -> sorted()", 
        "sorted() -> map() -> input() -> split()"
    ],
    "In the function call `print(len(str(input())))`, which function executes last?": [
        "print()", 
        "str()", 
        "input()", 
        "len()"
    ],
    "Which of the following is the correct sequence of function calls for `abs(float(input()))`?": [
        "input() -> float() -> abs()", 
        "abs() -> input() -> float()", 
        "float() -> abs() -> input()", 
        "input() -> abs() -> float()"
    ],
    "In the nested call `list(map(int, input().split()))`, which function is executed last?": [
        "list()", 
        "map()", 
        "split()", 
        "input()"
    ],
    "Given the nested function call `str(int(input(\"Enter a number: \")))`, which call occurs first?": [
        "input()", 
        "int()", 
        "str()", 
        "None of the above"
    ],
    "In the statement `print(int(float(input())))`, which function is called last?": [
        "print()", 
        "int()", 
        "float()", 
        "input()"
    ]
}



# {question : [answer, *options]}
questions.update(s1)
questions.update(s2)
questions.update(s3)
questions.update(s4)
questions.update(s5)
# questions.update(s6)
# questions.update(s7)
# questions.update(s8)
# questions.update(s9)
# questions.update(s10)
# questions.update(s11)
# questions.update(s12)
# questions.update(s13)
# questions.update(s14)
# questions.update(s15)
# questions.update(s16)
# questions.update(s17)
# questions.update(s18)
# questions.update(s19)
# questions.update(s20)






if __name__ == "__main__":
    print(len(questions))

    # for question, options in questions.items():
    #     print(question, *options, sep="\n")
    #     input()