'''Place preformmated questions and answers in the dictionary "questions" below.'''

setname = "set14"


questions = {}

'Defining a Variable'
s1 = {
    """Which of the following best describes a variable in programming?""": [
    "A pointer that references a location in memory where data is stored",
    "A fixed value used in code",
    "A function that changes data types",
    "An operator used for comparison"
],

"""Which of the following is a beginner-friendly way to think about variables?""": [
    "A container that stores literal data",
    "A list of immutable values",
    "A complex mathematical formula",
    "A debugging tool"
],

"""True or False: The data that a variable points to can be changed.""": [
    "True",
    "False"
],

"""Why is it important to understand the specific definition of a variable as a memory reference?""": [
    "Because the container analogy doesn’t always apply in more advanced use cases",
    "Because containers can’t store multiple values",
    "To use the print function correctly",
    "To write shorter code"
],
}

'Creating a Variable'
s2={
    """Which of the following is the correct syntax to create a variable in Python?""": [
    "variable = value",
    "value = variable",
    "variable == value",
    "def variable = value"
],

"""What does the single equals sign (=) do in Python?""": [
    "It assigns a value to a variable",
    "It checks if two values are equal",
    "It compares data types",
    "It multiplies two numbers"
],

"""Why should variable names be representative of the data that they reference?""": [
    "To improve source code readability",
    "To make the code run faster",
    "Because Python requires it",
    "To reduce memory usage"
],

"""Which of the following is a valid variable name for tracking a user's name?""": [
    "user_name",
    "123name",
    "user-name",
    "@username"
],

"""What value will the variable `b` hold after this code is run?\nb = 5""": [
    "5",
    "'b'",
    "True",
    "None"
],

"""True or False: Variable names should represent the data they reference.""": [
    "True",
    "False"
],

"""Which of the following variable assignments is correct in Python?""": [
    'name = "Jose"',
    '"Jose" = name',
    'name == "Jose"',
    'name : "Jose"'
],

"""Which of the following is an example of good variable naming practice?""": [
    "percent = 95.61",
    "p = 95.61",
    "x = 95.61",
    "pi-val = 95.61"
],

"""What is the purpose of the following line of code?

bad_passwords = ["password", "123456", "12345678"]
""": [
    "To create a variable that stores a list of strings",
    "To compare password strings",
    "To create a dictionary of passwords",
    "To assign one string to the variable"
],

}

'Assigning Multiple Variables'
s3 = {
    """What does the following line of code do?

apples = bananas = oranges = 42

""": [
    "Assigns the value 42 to all three variables: apples, bananas, and oranges",
    "Creates a list containing the numbers apples, bananas, and oranges",
    "Compares apples, bananas, and oranges to the number 42",
    "Declares a function named apples, bananas, and oranges"
],

"""What is the value of bananas after this code runs?

apples = bananas = oranges = 42

""": [
    "42",
    "apples",
    "oranges",
    "None"
],

"""True or False: The following line makes apples, bananas, and oranges aliases of the same data.

apples = bananas = oranges = 42

""": [
    "True",
    "False"
],

"""Which of the following correctly assigns the same value to multiple variables in Python?""": [
    "x = y = z = 99",
    "x == y == z == 99",
    "x = y : z = 99",
    "x, y, z = 99"
],

"""In the code below, what does it mean that apples, bananas, and oranges are aliases?

apples = bananas = oranges = 42

""": [
    "They all reference the same data in memory",
    "They are all the same type of variable",
    "They all store different values",
    "They are private variables"
],


"""What is the value of fruit2 after this line executes?

fruit1, fruit2, fruit3 = "green", "yellow", "red"

""": [
    "'yellow'",
    "'green'",
    "'red'",
    "None"
],

"""Which of the following correctly assigns multiple variables to different values on the same line?""": [
    "apple, banana, cherry = 'red', 'yellow', 'green'",
    "apple = banana = cherry = 'red', 'yellow', 'green'",
    "apple == banana == cherry == 'red'",
    "apple banana cherry = 'red' 'yellow' 'green'"
],

"""True or False: The following line of code is valid in Python.

car = 'blue'; bike = 'black'; bus = 'yellow'

""": [
    "True",
    "False"
],

"""Which of the following best describes the code below?

fruit1, fruit2, fruit3 = 'green', 'yellow', 'red'

""": [
    "Assigns 'green' to fruit1, 'yellow' to fruit2, and 'red' to fruit3 in one line",
    "Compares fruit1, fruit2, and fruit3 to the values 'green', 'yellow', and 'red'",
    "Creates a list with elements 'green', 'yellow', and 'red'",
    "Assigns the same value to fruit1, fruit2, and fruit3"
],
"""What does the following code do?

apple = "red"
apple = "green"
print(apple)

""": [
    "Reassigns the value of `apple` from 'red' to 'green' and prints 'green'",
    "Prints 'red' without changing the value of `apple`",
    "Declares a function named `apple`",
    "Compares the value of `apple` to 'green' and prints the result"
],

"""What will the following code output?

apple = "red"
apple = "green"
print(apple)

""": [
    "'green'",
    "'red'",
    "None",
    "Error"
],

"""Which of the following best describes reassigning a variable in Python?""": [
    "Changing the value a variable points to in memory",
    "Changing the variable name without altering its value",
    "Assigning a variable to another variable",
    "Creating a new variable from an existing one"
],

"""True or False: Reassigning a variable replaces its original value with the new value.

fruit = "banana"
fruit = "mango"

""": [
    "True",
    "False"
],

"""Which of the following is the correct syntax to reassign a variable in Python?""": [
    "fruit = 'mango'",
    "fruit == 'mango'",
    "fruit : 'mango'",
    "'mango' = fruit"
]
}

'Rules for Naming Variables'
s4 ={
"""Which of the following is a valid variable name in Python?""": [
    "my_variable_1",
    "1_variable",
    "my variable",
    "my-variable"
],

"""True or False: Variable names in Python can contain spaces.

""": [
    "False",
    "True"
],

"""Which of the following is NOT true when naming a variable in Python?""": [
    "Variable names can start with a number",
    "Variable names can only contain letters, numbers, and underscores",
    "Variable names are case sensitive",
    "Variable names cannot contain spaces"
],

"""Which of the following variable names is valid in Python?""": [
    "apple_1",
    "1_apple",
    "apple 1",
    "apple-1"
],

"""Which of the following is a good practice when naming variables in Python?""": [
    "Variables should be named after what they store or reference",
    "Variables should always be named using only numbers",
    "Variables should never be descriptive",
    "Variable names should be the same as Python keywords"
],
"""Which of the following variable names is valid in Python?""": [
    "name_123",
    "123_name",
    "name 123",
    "name-123"
],

"""Which of the following variable names is valid in Python?""": [
    "_underscore",
    "1underscore",
    "underscore space",
    "underscore-"
],

"""Which of the following variable names is valid in Python?""": [
    "myvariable",
    "my-variable",
    "my variable",
    "my@variable"
],

"""Which of the following variable names is valid in Python?""": [
    "count1",
    "1count",
    "count 1",
    "count-1"
],

"""Which of the following variable names is valid in Python?""": [
    "_total_amount",
    "(totalamount)",
    "total amount",
    "total@amount"
],

"""Which of the following variable names is valid in Python?""": [
    "value_1",
    "1value",
    "value 1",
    "value@1"
],

"""Which of the following variable names is valid in Python?""": [
    "data_value",
    "!datavalue"
    "data value",
    "data@value"
],

"""Which of the following variable names is valid in Python?""": [
    "firstName",
    "first name",
    "first-name",
    "first@name"
],

"""Which of the following variable names is valid in Python?""": [
    "myValue",
    "my-Value",
    "my value",
    "@myvalue"
],

"""Which of the following variable names is valid in Python?""": [
    "price1",
    "1price",
    "price 1",
    "price@1"
],
}

'Varaibles are references to locations in memory'
s5 = {
    """What happens when you assign a value to a variable in Python?""": [
    "Python creates an object in memory and assigns the variable a reference to its memory location",
    "Python creates a new function and assigns the variable to it",
    "Python directly stores the variable's value in a table",
    "Python creates a copy of the data and stores it in a new location"
],

"""Which of the following will return the memory location of the variable?""": [
    "id(variable)",
    "location(variable)",
    "address(variable)",
    "pointer(variable)"
],

"""Which of the following is true about the `id()` function in Python?""": [
    "It returns the memory location where the variable's data is stored",
    "It returns the value of the variable",
    "It returns the name of the variable",
    "It returns the data type of the variable"
],

"""True or False: If a variable has not been assigned a value, accessing it will raise a NameError.

""": [
    "True",
    "False"
],

"""What will happen if you try to access a variable that has not been assigned a value in Python?""": [
    "A NameError will be raised",
    "The variable will be initialized to None",
    "The program will continue without any issue",
    "A SyntaxError will be raised"
],
}

'Variable Aliasing'
s6 = {
    """Which of the following best describes aliasing in Python?""": [
    "Assigning one variable to reference the same data as another variable",
    "Creating two variables with different names pointing to different data",
    "Changing the data type of a variable",
    "Assigning a function to a variable"
],

"""What happens when you assign a variable to another in Python?""": [
    "Both variables point to the same memory location",
    "The second variable gets a copy of the first variable's data",
    "The second variable references the data from the first variable temporarily",
    "The second variable creates a new object"
],

"""What will happen if you modify a mutable object through one alias?""": [
    "The changes will reflect in all aliases pointing to the same object",
    "Only the alias through which the object is modified will be affected",
    "All aliases will point to a new memory location",
    "Only the original object will be affected"
],

"""Which of the following is true when aliasing immutable types?""": [
    "Changing the reference of one variable does not affect the others",
    "All variables will update to the new reference automatically",
    "All variables point to the new value after changing one reference",
    "Aliasing does not work with immutable types"
],

"""Which of the following will result in variables pointing to different memory locations?""": [
    "Reassigning one of the variables to a new value",
    "Changing the value of a mutable object",
    "Reassigning all variables to the same value",
    "Assigning variables of different data types"
],

"""True or False: In Python, all aliasing applies the same rules to mutable and immutable data types.

""": [
    "False",
    "True"
],

"""Which of the following code snippets will create aliases for a mutable object?""": [
    "a = [1, 2, 3]; b = a; c = b",
    "a = 10; b = a; c = b",
    "a = 'Hello'; b = a",
    "a = (1, 2, 3); b = a"
],

"""What happens when you modify a mutable object that has been aliased?""": [
    "All aliases will reflect the changes made to the object",
    "Only the object referenced by the last alias will be modified",
    "The changes will only be seen in the first alias",
    "The memory address will change for all aliases"
],

"""What is true about the behavior of immutable data types when aliased?""": [
    "Each alias maintains its own reference to the data, and changing one does not affect the others",
    "All aliases will reflect changes made to the data",
    "Modifying one alias will change all others to the new value",
    "None of the aliases will work after reassignment"
],

"""Which of the following is an example of aliasing an immutable object in Python?""": [
    "a = 'Hello'; b = a; c = b",
    "a = [1, 2, 3]; b = a; c = b",
    "a = 10; b = 10; c = b",
    "a = (1, 2, 3); b = a"
],
"""What will be the output of the following code?

a = "Hello"
b = a
b = "World"

print(a)
print(b)
""": [
    "Hello", 
    "World",
    "Both will print 'World'",
    "Both will print 'Hello'"
],

"""What will the ouput of the following code snippet?

a = [1, 2, 3]
b = a
b[0] = 99

print(a)
""": [
    "[99, 2, 3]",
    "[1, 2, 3]",
    "b",
    "99"
],

"""What will the following code print?

x = 10
y = x
x = 20

print(x, y)
""": [
    "20 10",
    "20 20",
    "10 10",
    "10 20"
],
}

'Type Annotation: Declaring Variable Type'
s7 = {
    """What is the purpose of Type Annotation in Python?""": [
    "To declare the type of data a variable is expected to reference",
    "To ensure that variables hold only a specific type of data",
    "To optimize the execution speed of the program",
    "To create more complex variables"
],

"""Which of the following is the correct syntax for Type Annotation in Python?""": [
    "variable: type = value",
    "variable = type(value)",
    "type(variable) = value",
    "type: variable = value"
],

"""What will the following code output?

num: int = 10
num = 20
print(num)
""": [
    "20",
    "10",
    "Error: Type mismatch",
    "None"
],

"""What is the type of the following variable?

text: str = 'Hello, World!'
""": [
    "str",
    "int",
    "list",
    "bool"
],

"""What will the following code output?

flo: float = 3.14
flo = 2.718
print(flo)
""": [
    "2.718",
    "3.14",
    "Error: Type mismatch",
    "None"
],

"""Which of the following correctly annotates a variable holding a list of integers?""": [
    "numbers: list = [1, 2, 3]",
    "numbers: int = [1, 2, 3]",
    "numbers: dict[int] = [1, 2, 3]",
    "list: numbers = [1, 2, 3]"
],
"""Which of the following types is used for an annotation that represents characters?""": [
    "str",
    "complex",
    "int",
    "float"
],

"""What does the following annotation represent?

imaginary: complex = 1j
""": [
    "A complex number",
    "A string",
    "An integer",
    "A floating-point number"
],

"""Is the following code correct in Python?

dictionary: dict = {"a": 1, "b": 2}
""": [
    "Yes, it is a valid type annotation for a dictionary",
    "No, the correct syntax should be 'dict: dictionary = {...}'",
    "No, type annotation cannot be used with dictionaries",
    "Yes, but it will raise a runtime error"
],
}

'Variable Scope and Context'
s8 = {
    """What does the term 'Scope' in programming refer to?""": [
    "The area within code in which a variable can be accessed and used",
    "The time it takes for a program to execute",
    "The type of variable a program can reference",
    "The style of code used in a program"
],

"""Which of the following is true about 'global' variables in Python?""": [
    "Global variables are accessible anywhere in the program after they are defined",
    "Global variables can only be accessed inside functions",
    "Global variables are used to store temporary data",
    "Global variables are automatically deleted after use"
],

"""What does the 'nonlocal' keyword do in Python?""": [
    "It allows access to variables in the nearest enclosing scope",
    "It makes a variable global to the entire program",
    "It restricts a variable to be used only inside a function",
    "It initializes variables in all scopes"
],


"""What is the scope of a variable declared inside a function?""": [
    "Local to the function",
    "Global to the program",
    "Global to the function",
    "Nonlocal to the program"
],

"""What is the difference between global and local scope?""": [
    "Global variables can be accessed anywhere in the program, while local variables are restricted to the function or block in which they are defined",
    "Global variables are more secure, while local variables can be accessed anywhere",
    "Local variables can only be accessed by the user, while global variables cannot",
    "There is no difference"
],

"""Which of the following will allow modification of a global variable inside a function?""": [
    "Using the global keyword",
    "Using the nonlocal keyword",
    "Declaring the variable inside the function",
    "Global variables cannot be modified inside functions"
],

"""What is the purpose of namespaces in Python?""": [
    "They map variable names to objects, allowing proper access and management of variables",
    "They make variables unique to each function",
    "They are used to define variable types",
    "They handle memory allocation for variables"
],

"""Which keyword should be used to access and modify a global variable within a function?""": [
    "global",
    "local",
    "nonlocal",
    "namespace"
],
"""How does Python search for variables in terms of scope?""": [
    "From the most local scope to the least local scope",
    "From the least local scope to the most local scope",
    "It searches globally first, then locally",
    "It looks in a random order"
],

"""Which of the following best describes the way Python handles variable lookup?""": [
    "It starts with the local scope and works outward to the global scope",
    "It starts with the global scope and works inward to the local scope",
    "It looks for the variable in the order it was declared",
    "It searches the entire code without any specific order"
],

"""What happens when a variable is not found in the local scope in Python?""": [
    "Python looks for the variable in the enclosing scope or global scope",
    "Python raises an error immediately",
    "Python uses a default value for the variable",
    "Python stops searching and returns None"
],
"""What does the dir() function return in Python?""": [
    "A list of names in the current local namespace",
    "A list of built-in functions in Python",
    "A dictionary of global variables",
    "The location of all imported modules"
],

"""What will the following code output?

namespace = dir()
print(namespace)""": [
    "A list of names in the current local namespace",
    "The built-in functions of Python",
    "A list of all modules imported in the current script",
    "The location of the current script in memory"
],

"""What does the __builtins__ argument in dir() function provide?""": [
    "It shows the built-in namespace with all the default built-in names",
    "It shows the location of the built-in files in Python",
    "It shows the list of global variables",
    "It shows the local functions defined in the current script"
],

"""How can you view the built-in namespace in Python?""": [
    "Use dir() with the __builtins__ argument",
    "Use the built-in function list()",
    "Use the print() function directly",
    "Use the globals() function"
],
"""Which of the following best describes a local variable in Python?""": [
    "A variable that is accessible only inside the scope in which it is defined",
    "A variable that is accessible anywhere in the program",
    "A variable that can be accessed only within a class",
    "A variable that can only be modified within a function"
],

"""What does it mean for a variable to be global in Python?""": [
    "It is accessible anywhere in the program outside of functions or classes",
    "It can only be accessed inside the function where it is defined",
    "It is only accessible within a method or class",
    "It is accessible only within the specific function where it is initialized"
],

"""Where can you access a local variable in Python?""": [
    "Only within the function, method, or block of code where it is defined",
    "Anywhere in the entire program",
    "Inside other functions or methods",
    "Only within classes and modules"
],

"""Which keyword is used in Python to declare a variable as global inside a function?""": [
    "global",
    "local",
    "nonlocal",
    "public"
],

"""Which of the following is true about global variables?""": [
    "They can be accessed and modified from anywhere in the program outside of functions or classes",
    "They are defined only inside functions",
    "They are only accessible inside the class where they are defined",
    "They are not accessible inside functions unless declared as nonlocal"
],
"""Which of the following best describes a namespace in Python?""": [
    "A mapping of names (variables) to objects",
    "A storage area for all functions in a program",
    "A type of data structure used only for global variables",
    "A keyword used to define variables in different scopes"
],
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
# questions.update(s9)
# questions.update(s10)







if __name__ == "__main__":
    print(len(questions))

    # for question, options in questions.items():
    #     print(question, *options, sep="\n")
    #     input()