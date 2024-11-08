



'Ternary Operators'
MCQ("What will the following code snippet output?\n\nx = 10\nresult = 'Interpreter' if x % 2 == 0 else 'Syntax'\nprint(result)", "Interpreter", "Syntax", "Module", "Framework", "Library", "Interpreter")
MCQ("What is the result of the following ternary expression?\n\nx = 7\ny = 10\nresult = 'True' if x > y else 'False'\nprint(result)", "False", "True", "Error", "Zero", "Negative", "False")
MCQ("What is the output of the following code snippet?\n\nnum = -5\nresult = 'Function' if num > 0 else 'Non-zero'\nprint(result)", "Non-zero", "Function", "Zero", "Negative", "Error", "Non-zero")
MCQ("What does the following ternary operation return?\n\nvalue = 20\nresult = 'Yes' if value >= 10 else 'No'\nprint(result)", "Yes", "No", "Error", "True", "False", "Yes")
MCQ("What will be the value of 'grade' after the ternary expression is evaluated?\n\nmarks = 85\ngrade = 'Boolean' if marks >= 60 else 'None'\nprint(grade)", "Boolean", "None", "Error", "High", "Low", "Boolean")
MCQ("What does the following ternary expression yield?\n\nx = 25\ny = 30\nz = 'Valid' if x < y else 'Invalid'\nprint(z)", "Valid", "Invalid", "Error", "True", "False", "Valid")
MCQ("What does the following ternary operation output?\n\nvalue = 0\nresult = 'Function' if value > 0 else ('Keyword' if value < 0 else 'Literal')\nprint(result)", "Literal", "Function", "Keyword", "Error", "True", "Literal")
MCQ("What is the result of the following ternary expression?\n\nx = 15\ny = 10\nz = 'Greater' if x > y else ('Lesser' if x < y else 'Equal')\nprint(z)", "Greater", "Lesser", "Equal", "Error", "True", "Greater")
MCQ("What does the following ternary operator evaluate to?\n\nvalue = 100\nresult = 'Pass' if value >= 70 else 'Fail'\nprint(result)", "Pass", "Fail", "Error", "High", "Low", "Pass")
MCQ("What will be the output of the following ternary expression?\n\nx = 12\ny = 18\nresult = 'True' if x != y else 'False'\nprint(result)", "True", "False", "Error", "Equal", "Unequal", "True")


'Basic Questions'


'If Statements'
MCQ("What is the purpose of the if statement in Python?", "To execute a block of code only if a specified condition is true", "To execute a block of code regardless of any condition", "To execute a block of code if a specified condition is false", "To check the syntax of a block of code", "None of these", "To execute a block of code only if a specified condition is true")
MCQ("What is the syntax for an if statement in Python?", "if condition:", "if then:", "if (condition){}", "if (condition) then:", "None of these", "if condition:")
MCQ("What will be the output of the following code?\nx = 10\nif x > 5:\n print('x is greater than 5')", "x is greater than 5", "x is less than 5", "x is equal to 5", "Syntax Error", "None of these", "x is greater than 5")
MCQ("What happens if the condition in an if statement evaluates to False?", "The code block associated with the if statement is not executed", "The code block associated with the if statement is executed", "The program terminates", "An error is raised", "None of these", "The code block associated with the if statement is not executed")
MCQ("Which symbol is used to denote the start of a block of code in Python?", ":", "{}", "()", "//", "None of these", ":")
MCQ("In Python, can an if statement contain multiple conditions?", "Yes", "No", "Sometimes", "Depends on the version of Python", "None of these", "Yes")
MCQ("What is the purpose of indentation in Python?", "To define blocks of code", "To make the code look neat", "To increase readability", "All of these", "None of these", "All of these")
MCQ("Which of the following is a valid way to write an if statement in Python?", "if x > 5:", "if (x > 5)", "if x > 5 then:", "if x > 5 then", "None of these", "if x > 5:")
MCQ("What will be the output of the following code?\nx = 3\nif x % 2 == 0:\n print('x is even')", "No output", "x is even", "x is odd", "Syntax Error", "None of these", "No output")
MCQ("What happens if the condition in an if statement is not met and there is no else statement?", "The program continues execution after the if block", "The program terminates", "An error is raised", "The program goes into an infinite loop", "None of these", "The program continues execution after the if block")

'Special Conditionals Notes'
MCQ("Any non-zero number (integer, float) is evaluated as:", "True", "False", "None", "Error", "None of these", "True") 
MCQ("Any non-empty string, list, tuple, set, or dictionary, is evaluated as:",  "True", "False", "None", "Error", "None of these", "True") 
MCQ("Any function, method, lambda or class is evaluated as:",  "True", "False", "None", "Error", "None of these", "True") 
MCQ("By default, objects are evaluated as:",  "True", "False", "None", "Error", "None of these", "True") 


'If-else Statments'
MCQ("What will be the output of the following Python code?\n \nx = 5\nif x > 3:\n print('x is greater than 3') \n\nelse:\n print('x is less than or equal to 3')\n", "x is greater than 3", "x is less than 3", "x is less than or equal to 3", "x is greater than or equal to 3", "x is less than 3", "x is greater than 3")
MCQ("What is the output of the following Python code?\n \nnum = 12\nif num % 2 == 0:\n print('Even number') \n\nelse:\n print('Odd number')\n", "Even number", "Odd number", "Not an even or odd number", "12 is divisible by 2", "Remainder number", "Even number")
MCQ("What does the following Python code do?\n \nage = 20\nif age >= 18:\n print('You are eligible to vote') \n\nelse:\n print('You are not eligible to vote')\n", "Checks if age is less than 18", "Checks if age is divisible by 18", "Checks if age is equal to 18", "Checks if age is greater than or equal to 18", "Checks if age is less than or equal to 18", "Checks if age is greater than or equal to 18")
MCQ("What will be printed by the following Python code snippet?\n \nscore = 75\nif score >= 60:\n print('You passed the exam!') \n\nelse:\n print('You failed the exam!')\n", "You passed the exam!", "You failed the exam!", "Your score is 60 or above", "Your score is below 60", "TypeError", "You passed the exam!")
MCQ("What is the output of the following code snippet?\n \nx = 10\nif x == 10:\n print('x is equal to 10') \n\nelse:\n print('x is not equal to 10')\n", "x is equal to 10", "x is not equal to 10", "x is equal to 5", "x is equal to 11", "x is not equal to 5", "x is equal to 10")
MCQ("What does the following Python code snippet do?\n \nage = 25\nif age < 18:\n print('You are a minor') \n\nelse:\n print('You are an adult')\n", "Checks if age is greater than or equal to 18", "Checks if age is less than 18", "Checks if age is less than or equal to 18", "Checks if age is greater than 18", "Checks if age is equal to 18", "Checks if age is less than 18")
MCQ("What will the following Python code output?\n \nnum = -5\nif num < 0:\n print('Negative number') \n\nelse:\n print('Positive number')\n", "Negative number", "Positive number", "Not a negative or positive number", "Not a number", "Number", "Negative number")
MCQ("What will be the result of the following Python code?\n \nx = 7\nif x % 2 == 0:\n print('Even') \n\nelse:\n print('Odd')\n", "Odd", "Even", "Divisible by 2", "Not divisible by 2", "Error", "Odd")
MCQ("What does the following Python code snippet do?\n \nx = 20\nif x >= 10:\n print('x is greater than 10') \n\nelse:\n print('x is less than or equal to 10')\n", "Checks if x is greater than 10", "Checks if x is less than 10", "Checks if x is equal to 10", "Checks if x is greater than or equal to 10", "Checks if x is less than 10", "Checks if x is greater than or equal to 10")
MCQ("What is the output of the following Python code snippet?\n \nnum = '0'\nif num == 0:\n print('Zero') \n\nelse:\n print('Non-zero')\n", "Zero", "Non-zero", "Positive", "Negative", "0", "Non-zero")

'Chained conditionals'
MCQ("What is the output of the following code snippet?\n\nx = 15\nif x < 10:\n print('apple') \n\nelif x > 10:\n print('banana') \n\nelse:\n print('orange')\n", "banana", "apple", "orange", "grape", "cherry", "banana")
MCQ("What is the output of the following code snippet?\n\nx = 5\nif x < 10:\n print('apple') \n\nelif x > 10:\n print('banana') \n\nelse:\n print('orange')\n", "apple", "banana", "orange", "grape", "cherry", "apple")
MCQ("What is printed by the following code snippet?\n\nx = 10\nif x < 5:\n print('mango') \n\nelif x > 10:\n print('kiwi') \n\nelse:\n print('pear')\n", "pear", "mango", "kiwi", "grape", "cherry", "pear")
MCQ("What will the following code snippet print?\n\nx = 8\nif x < 5:\n print('watermelon') \n\nelif x > 10:\n print('papaya') \n\nelse:\n print('blueberry')\n", "blueberry", "watermelon", "papaya", "grape", "cherry", "blueberry")
    
MCQ("What will be printed by the following code snippet?\n\nx = 7\nif x > 5 and x < 10:\n print('apple') \n\nelif x < 0 or x > 10:\n print('banana') \n\nelse:\n print('orange')\n", "apple", "banana", "orange", "grape", "cherry", "apple")
MCQ("What will be the output of the following code snippet?\n\nx = 12\nif x > 5 and x < 10:\n print('strawberry') \n\nelif x < 0 or x > 10:\n print('blueberry') \n\nelse:\n print('raspberry')\n", "blueberry", "strawberry", "raspberry", "blackberry", "cranberry", "blueberry")
MCQ("What is printed by the following code snippet?\n\nx = 15\nif x > 5 and x < 10:\n print('mango') \n\nelif x < 0 or x > 10:\n print('pineapple') \n\nelse:\n print('peach')\n", "pineapple", "mango", "peach", "pear", "plum", "pineapple")
MCQ("What will the following code snippet print?\n\nx = 3\nif x > 5 and x < 10:\n print('grape') \n\nelif x < 0 or x > 10:\n print('cherry') \n\nelse:\n print('plum')\n", "cherry", "grape", "plum", "pear", "apricot", "plum")
    
MCQ("What does the following Python code snippet output?\n\nname = 'alice'\nif 'a' in name:\n print('function') \n\nelif len(name) < 5:\n print('module') \n\nelse:\n print('variable')\n", "function", "module", "variable", "method", "class", "function")
MCQ("What does the following Python code snippet output?\n\nword = 'python'\nif 'p' not in word:\n print('snake') \n\nelif len(word) < 7:\n print('programming') \n\nelse:\n print('language')\n", "snake", "programming", "language", "insect", "reptile", "programming")
MCQ("What does the following Python code snippet output?\n\nnumber = 10\nif number > 0:\n print('positive') \n\nelif number < 0:\n print('negative') \n\nelse:\n print('zero')\n", "positive", "negative", "zero", "fraction", "integer", "positive")
MCQ("What does the following Python code snippet output?\n\nword = 'banana'\nif 'c' in word:\n print('fruit') \n\nelif len(word) < 5:\n print('apple') \n\nelse:\n print('orange')\n", "fruit", "apple", "orange", "vegetable", "dessert", "orange")
    
MCQ("What is the result of the following code snippet?\n\nage = 18\nif age >= 18 and age <= 65:\n print('Adult') \n\nelif age < 18:\n print('Child') \n\nelse:\n print('Senior')\n", "Adult", "Child", "Senior", "Both Adult and Child", "Error", "Adult")
MCQ("What is the output of the following code snippet?\n\nx = 15\nif x > 10 and x % 2 == 0:\n print('Function') \n\nelif x < 10 or x % 3 == 0:\n print('Module') \n\nelse:\n print('Variable')\n", "Function", "Module", "Variable", "Method", "Class", "Module")
MCQ("What will be printed by the following code snippet?\n\ny = 20\nif (y > 15 and y < 25) or (y % 4 == 0):\n print('Lambda') \n\nelif y < 20 and y % 3 == 0:\n print('Decorator') \n\nelse:\n print('Iterator')\n", "Lambda", "Decorator", "Iterator", "Generator", "Comprehension", "Lambda")
MCQ("What does the following Python code snippet output?\n\nz = 30\nif (z > 20 and z < 40) or (z % 5 == 0):\n print('Recursion') \n\nelif z > 25 and z % 6 == 0:\n print('Assertion') \n\nelse:\n print('Exception')\n", "Recursion", "Assertion", "Exception", "Module", "Namespace", "Recursion")    
MCQ("What will be the output of the following code snippet?\n\nnum = 5\nif num % 2 == 0:\n print('snake') \n\nelif num % 3 == 0:\n print('django') \n\nelse:\n print('flask')\n", "flask", "snake", "django", "neither snake nor django", "pandas", "flask")
MCQ("What will the following code snippet print?\n\nnum = 25\nif num > 20 and num % 5 == 0:\n print('Polymorphism') \n\nelif num < 20 or num % 3 == 0:\n print('Abstraction') \n\nelse:\n print('Inheritance')\n", "Polymorphism", "Abstraction", "Inheritance", "Encapsulation", "Aggregation", "Polymorphism")
MCQ("What output is produced by the following code snippet?\n\nvalue = 35\nif (value > 30 and value < 40) or value % 7 == 0:\n print('Interface') \n\nelif value > 25 and value % 8 == 0:\n print('Module') \n\nelse:\n print('Library')\n", "Interface", "Module", "Library", "Package", "Framework", "Interface")
MCQ("What does the following Python code snippet print?\n\nnumber = 28\nif (number > 25 and number < 30) and (number % 4 == 1):\n print('Class') \n\nelif number > 20 and number % 6 == 0:\n print('Object') \n\nelse:\n print('Instance')\n", "Class", "Object", "Instance", "Attribute", "Method", "Instance")


'Nested Conditionals'
MCQ("What will the following code snippet output?\n\nx = 10\nif x > 5:\n if x < 10:\n  print('Pythonic') \n\n else:\n  print('Module') \n\nelse:\n print('Interpreter')", "Pythonic", "Module", "Interpreter", "Library", "Framework", "Module")
MCQ("What is the result of executing the code below?\n\nnum = 20\nif num < 25:\n if num > 15:\n print('Algorithm') \n\nelse:\n print('Scripting')", "Algorithm", "Scripting", "Framework", "Runtime", "Debugger", "Algorithm")
MCQ("What does the following Python snippet print?\n\nx = 30\nif x > 25:\n if x % 7 == 0:\n  print('Recursion') \n\nelse:\n print('Syntax')", "Recursion", "Syntax", "Debugging", "Nothing is printed", "Module", "Nothing is printed")
MCQ("What will be the output of the modified code snippet?\n\nnum = 18\nif num < 15:\n if num < 20:\n  print('Decorator') \n\n else:\n  print('Parameter') \n\nelse:\n print('Polymorphism')", "Decorator", "Parameter", "Polymorphism", "Inheritance", "Nothing is printed", "Polymorphism")
MCQ("What is printed by the following Python script?\n\nx = 5\nif x > 3:\n if x < 7:\n  print('Syntax') \n\n else:\n  print('List') \n\nelse:\n print('Tuple')", "Syntax", "List", "Tuple", "Dictionary", "Set", "Syntax")

