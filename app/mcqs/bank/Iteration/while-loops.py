
'> Special to Python: While-Else'
MCQ("In Python, what happens if the condition of a while loop becomes False, and the loop has an else block?",
"The else block is executed",
"The loop terminates and the else block is skipped",
"The loop restarts from the beginning",
"The code raises an error",
"The loop continues indefinitely",
"The else block is executed")

MCQ("What is the purpose of the else block in a while loop?",
"To execute code when the loop condition becomes False",
"To execute code before each iteration of the loop",
"To skip the loop entirely",
"To handle exceptions within the loop",
"To break out of the loop",
"To execute code when the loop condition becomes False")

MCQ("Which of the following scenarios is an appropriate use case for a while-else statement?",
"When you want to execute some code if the loop completes without encountering a break statement",
"When you want to execute code only if the loop condition is False at the start",
"When you want to execute code only if the loop condition is True at the start",
"When you want to execute code inside the loop before each iteration",
"When you want to execute code only if the loop encounters a break statement",
"When you want to execute some code if the loop completes without encountering a break statement")

MCQ("In a while-else statement, when does the else block get executed?",
"When the while loop completes without encountering a break statement",
"When the while loop starts",
"When the while loop condition becomes True",
"When the while loop condition becomes False",
"When the while loop is terminated using the continue statement",
"When the while loop completes without encountering a break statement")

MCQ("What happens if the while loop is terminated by a break statement before the loop condition becomes False in a while-else statement?",
"The else block is skipped",
"The else block is still executed",
"The loop starts over from the beginning",
"The code raises an error",
"The loop enters an infinite loop",
"The else block is skipped")


MCQ("What will be the output of the following code snippet?\n\npython\nx = 5\nwhile x > 0:\n print(x, end=' ')\n x -= 1\nelse:\n print('Loop completed!')\n\n","5 4 3 2 1 Loop completed!","Loop completed! 5 4 3 2 1","5 4 3 2 1","Loop completed! 5 4 3 2 1 ","5 4 3 2 1 ","Loop completed! 5 4 3 2 1")
MCQ("What will be the output of the following code snippet?\n\npython\nx = 0\nwhile x < 5:\n print(x, end=' ')\n x += 1\nelse:\n print('Loop completed!')\n\n","0 1 2 3 4 Loop completed!","Loop completed! 0 1 2 3 4","0 1 2 3 4","Loop completed! 0 1 2 3 4 ","0 1 2 3 4 ","Loop completed! 0 1 2 3 4")


'> Nested While Loops'
MCQ("What will be the output of the following nested while loop?\n\npython\nx = 1\nwhile x <= 3:\n y = 1\n while y <= 2:\n  print(x, y, end = ' ')\n  y += 1\n x += 1\n\n",
"1 1 1 2 2 1 2 2 3 1 3 2",
"1 1 2 1 2 2 3 1 3 2",
"1 1 1 2 2 2 3 1 3 2",
"1 2 1 3 2 1 2 2 3 1 3 2 ",
"1 1 2 1 2 2 3 1 3 2 ",
"1 1 1 2 2 1 2 2 3 1 3 2")

MCQ("What will be the output of the following nested while loop?\n\npython\nx = 3\nwhile x > 0:\n y = 3\n while y > 0:\n  print(x, y ,end = ' ')\n  y -= 1\n x -= 1\n\n",
"3 3 2 3 1 3 2 2 1 2 1 1",
"3 3 3 2 3 1 2 3 2 2 2 1 1 3 1 2 1 1 ",
"3 3 2 2 2 1 1 1",
"3 3 2 2 1 1",
"3 3 2 3 1 2 1 1",
"3 3 3 2 3 1 2 3 2 2 2 1 1 3 1 2 1 1 ")

MCQ("What will be the output of the following nested while loop?\n\npython\nx = 1\nwhile x <= 2:\n y = 1\n while y <= 3:\n  print(x + y, end = ' ')\n  y += 1\n x += 1\n\n",
"2 3 4 3 4 5",
"2 3 4 1 2 3",
"1 2 3 4 5 6",
"1 2 3 2 3 4",
"1 2 3 4 1 2",
"2 3 4 3 4 5")

MCQ("What will be the output of the following nested while loop?\n\nx = 2\nwhile x >= 0:\n y = 0\n while y <= 2:\n  print(x - y, end = ' ')\n  y += 1\n x -= 1\n\n",
"2 1 0 1 0 -1 0 -1 -2",
"2 1 0 1 0 -1 2 1 0",
"0 1 2 -1 0 1 -2 -1 0",
"0 1 2 1 0 -1 2 1 0",
"2 1 0 -1 0 1 -2 -1 0",
"2 1 0 1 0 -1 0 -1 -2")

'> Break and Continue'
MCQ("What will the following code snippet output?\n\nx = 0\nwhile x < 5:\n if x == 3:\n  break\n  print(x)\n x += 1\n", "0, 1, 2, 3", "0, 1, 2", "0, 1, 2, 3, 4", "0, 1, 2, 3, 4, 5", "None of these", "0, 1, 2")
MCQ("Consider the code snippet below:\n\nx = 10\nwhile x > 0:\n if x == 7:\n  break\n  print(x)\n x -= 1\nWhat will be the output of the code?", "10, 9, 8", "10, 9, 8, 7", "10, 9, 8, 7, 6", "10, 9, 8, 7, 6, 5", "None of these", "10, 9, 8")
MCQ("What happens when a break statement is encountered within a nested loop?", "The break statement only exits the inner loop", "The break statement only exits the outer loop", "The break statement exits both the inner and outer loops", "The break statement is ignored", "None of these", "The break statement only exits the inner loop")
MCQ("In a while loop, where should a break statement typically be placed?", "Within an if statement to check a condition", "At the beginning of the loop", "At the end of the loop", "Before the loop starts", "None of these", "Within an if statement to check a condition")
MCQ("What is the primary purpose of using a break statement in a loop?", "To prematurely terminate the loop", "To skip a specific iteration of the loop", "To increment the loop counter", "To pause the execution of the loop", "None of these", "To prematurely terminate the loop")
MCQ("What will the following code snippet output?\n\nx = 0\nwhile x < 5:\n x += 1\n if x == 3:\n  continue\n  print(x)\n", "1, 2, 4, 5", "1, 2, 3, 4, 5", "1, 2, 3, 4", "1, 2, 3, 4, 5, 6", "None of these", "1, 2, 4, 5")
MCQ("Consider the code snippet below:\n\nx = 10\nwhile x > 0:\n x -= 1\n if x == 7:\n  continue\n  print(x)\nWhat will be the output of the code?", "9, 8, 6, 5, 4, 3, 2, 1, 0", "10, 9, 8, 6, 5, 4, 3, 2, 1, 0", "9, 8, 7, 6, 5, 4, 3, 2, 1, 0", "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0", "None of these", "9, 8, 6, 5, 4, 3, 2, 1, 0")
MCQ("What does a continue statement do in a loop?", "Skips the remaining code in the loop and continues with the next iteration", "Exits the loop completely", "Restarts the loop from the beginning", "Halts the execution of the loop", "None of these", "Skips the remaining code in the loop and continues with the next iteration")
MCQ("In a while loop, where should a continue statement typically be placed?", "Within an if statement to check a condition", "At the beginning of the loop", "At the end of the loop", "Before the loop starts", "None of these", "Within an if statement to check a condition")
MCQ("What is the primary purpose of using a continue statement in a loop?", "To skip certain iterations of the loop based on a condition", "To prematurely terminate the loop", "To increment the loop counter", "To pause the execution of the loop", "None of these", "To skip certain iterations of the loop based on a condition")



'Basic Questions'

'Vocabulary'
MCQ("What is the definition of 'iterate' in programming?", "A statement that evaluates True/False to determine if a code block is run.", "The rules for writing a programming language.", "Repetition of a process or function.", "A type of variable in programming.", "A method for debugging code.", "Repetition of a process or function.")
MCQ("Which term refers to a statement that evaluates True/False to determine if a code block is run?", "Iterate", "Condition", "Syntax", "Variable", "Debugging", "Condition")
MCQ("What does 'Syntax' refer to in programming?", "Repetition of a process or function.", "A statement that evaluates True/False to determine if a code block is run.", "The rules for writing a programming language.", "A type of loop in programming.", "A method for code optimization.", "The rules for writing a programming language.")

'> While Loop Syntax'
MCQ("Which keyword is used to initiate a while loop in Python?", "for", "do", "while", "if", "loop", "while")
MCQ("What comes after the condition in a while loop?", "A colon ( : )", "An equal sign ( = )", "A semicolon ( ; )", "A comma ( , )", "A period ( . )", "A colon ( : )")
MCQ("What is the purpose of the condition in a while loop?", "To initialize variables", "To execute code once", "To determine when the loop should stop", "To print output", "To define functions", "To determine when the loop should stop")
MCQ("What is the significance of indentation in Python?", "It doesn't matter in Python", "It indicates the end of a loop", "It defines a code block", "It terminates the program", "It is used for commenting", "It defines a code block")
MCQ("What does the code block inside a while loop consist of?", "A single line of code", "A series of numbers", "Multiple function calls", "Statements to be executed repeatedly", "Variable declarations", "Statements to be executed repeatedly")
MCQ("In Python, how is the end of the code block inside a while loop indicated?", "Using a semicolon ( ; )", "Using an equal sign ( = )", "By unindenting", "Using parentheses ( )", "Using square brackets ( [ ] )", "By unindenting")
MCQ("How is the condition of a while loop typically defined?", "Using a variable name", "Using a function call", "Using a string value", "Using a sequence of numbers", "Using a logical expression", "Using a logical expression")
MCQ("What happens if the condition of a while loop evaluates to False initially?", "The loop will execute indefinitely", "The loop will exit immediately without executing the code block", "The loop will skip the code block and move to the next iteration", "The loop will raise an error","The loop will execute the code block once and then move the next line","The loop will exit immediately without executing the code block")
MCQ("What is the role of the colon ( : ) in while loop syntax?", "To terminate the loop", "To separate the condition from the code block", "To indicate the end of the code block", "To define the condition", "To indicate the start of the loop", "To separate the condition from the code block")
MCQ("Which of the following statements accurately describes the execution flow of a while loop?", "The loop will execute the code block once", "The loop will execute the code block repeatedly until the condition becomes False", "The loop will execute the code block based on the condition's value", "The loop will execute the code block based on a predefined number of iterations", "The loop will execute the code block repeatedly until it reaches a specified limit", "The loop will execute the code block repeatedly until the condition becomes False")

'> The Control Variable'
MCQ("Which of the following best describes a control variable in a while loop?", "A variable used to manage the flow of the loop", "A variable that remains constant throughout the loop", "A variable that changes unpredictably within the loop", "A variable declared outside the loop", "A variable that controls the termination condition of the loop", "A variable that controls the termination condition of the loop")
MCQ("In Python, how is a control variable typically used in a while loop?", "To determine the loop's termination condition", "To store the loop's result", "To control the loop's iteration count", "To define the loop's starting point", "To print the loop's output", "To determine the loop's termination condition")
MCQ("What will be the output of the following code snippet?\n\nx = 0\nwhile x < 5:\n print(x)\n x += 1\n\n", "0 1 2 3 4", "1 2 3 4 5", "0 1 2 3 4 5", "5 4 3 2 1 0", "0 1 2 3", "0 1 2 3 4")
MCQ("What is the role of the control variable 'x' in the following code snippet?\n\nx = 0\nwhile x < 5:\n print(x)\n x += 1\n", "To control the termination condition of the while loop", "To initialize the loop counter", "To print the loop output", "To define the loop's starting point", "To check if the loop condition is met", "To control the termination condition of the while loop")
MCQ("What is the role of the control variable 'x' in the following code snippet?\n \n\nx = 0\nwhile x < 5:\n print(x)\n x += 1\n\n", "To control the termination condition of the while loop", "To initialize the loop counter", "To print the loop output", "To define the loop's starting point", "To check if the loop condition is met", "To control the termination condition of the while loop")
MCQ("In the code snippet provided, how many times will the print statement execute?\n \n\nx = 0\nwhile x < 5:\n print(x)\n x += 1\n\n", "5 times", "6 times", "4 times", "Infinite times", "3 times", "5 times")
MCQ("What will happen if the initial value of 'x' is set to 5 in the given code snippet?\n \n\nx = 0\nwhile x < 5:\n print(x)\n x += 1\n\n", "The loop body will not execute at all", "The loop will execute indefinitely", "The loop will terminate immediately", "The loop will print '5' once and then terminate", "The loop will print '0' to '4' as before", "The loop body will not execute at all")
MCQ("Which part of the code snippet is responsible for ensuring that the loop will eventually terminate?\n \n\nx = 0\nwhile x < 5:\n print(x)\n x += 1\n\n", "x += 1", "while x < 5:", "print(x)", "x = 0", "The absence of an increment statement", "while x < 5:")
MCQ("What would happen if the condition in the while loop were changed to 'x <= 5'?\n \n\nx = 0\nwhile x > 10:\n print(x)\n x += 1\n\n", "The loop would print an additional '5'", "The loop would not execute at all", "The loop would execute indefinitely", "The loop would print '0' to '5'", "The loop would print '1' to '5'", "The loop would print '0' to '5'")
MCQ("In the code snippet provided, how many times will the print statement execute?\n \n\nx = 0\nwhile x < 10:\n print(x)\n x += 2\n\n", "5 times", "6 times", "4 times", "Infinite times", "3 times", "5 times")
MCQ("In the given code snippet, how many times will the print statement execute?\n \n\nx = 0\nwhile x < 3:\n print(x)\n x -= 1\n\n", "3 times", "2 times", "1 time", "Infinite times", "0 times", "Infinite times")
MCQ("Considering the provided code snippet, how many times will the print statement be executed?\n \n\nx = 10\nwhile x > 5:\n print(x)\n x -= 3\n\n", "2 times", "3 times", "4 times", "Infinite times", "5 times", "2 times")
MCQ("Which statement best explains the role of a control variable in a while loop?", "It allows the loop to repeat until a certain condition is met", "It keeps track of the loop's current iteration", "It prevents the loop from executing indefinitely", "It defines the loop's starting point", "It ensures the loop's termination", "It ensures the loop's termination")
MCQ("In the context of while loops, what is the significance of updating the control variable?", "It prevents infinite looping", "It ensures the loop's starting point", "It defines the loop's termination condition", "It controls the loop's output", "It determines the loop's iteration count", "It prevents infinite looping")
MCQ("What is the primary purpose of a control variable in a while loop?", "To control the loop's execution based on certain conditions", "To define the loop's structure", "To store the loop's output", "To initialize the loop", "To print the loop's result", "To control the loop's execution based on certain conditions")
MCQ("Which of the following statements accurately describes the role of a control variable in a while loop?", "It determines when the loop stops executing", "It controls the loop's starting value", "It defines the loop's structure", "It stores the loop's output", "It ensures the loop's starting point", "It determines when the loop stops executing")
MCQ("What happens if the control variable in a while loop is not updated within the loop body?", "The loop may execute indefinitely, causing a program to hang", "The loop terminates immediately", "The loop skips the next iteration", "The loop throws an error", "The loop restarts from the beginning", "The loop may execute indefinitely, causing a program to hang")
MCQ("Which of the following examples demonstrates the correct usage of a control variable in a while loop?", "\nx = 0\nwhile x < 10:\n print(x)\n x += 1\n", " \nwhile True:\n print('Infinite loop!') \n", " \nx = 5\nwhile x >= 0:\n print(x)\n x -= 1 \n", " \nwhile condition:\n print('Looping...') \n", " \nx = 0\nwhile x != 10:\n print(x) \n", " \nx = 5\nwhile x >= 0:\n print(x)\n x -= 1 \n")

'Counting With While loops'
MCQ("What is the purpose of the following code snippet?\n \n\ncount = start\nwhile(count < stop): \n count = count + step \n \n count += step \n\n", "To iterate from 'start' to 'stop' with a certain 'step' size", "To define a function named 'count'", "To check if 'count' is equal to 'stop'", "To initialize 'count' to zero", "To print the value of 'count'", "To iterate from 'start' to 'stop' with a certain 'step' size")
MCQ("Which of the following statements is true regarding the while loop condition in the provided code snippet?\n \n\ncount = start\nwhile(count < stop): \n count = count + step \n \n count += step \n\n", "The loop will continue as long as 'count' is less than 'stop'", "The loop will continue as long as 'count' is greater than 'stop'", "The loop will only run once", "The loop will never run", "The loop will run indefinitely", "The loop will continue as long as 'count' is less than 'stop'")
MCQ("What does 'count += step' achieve in the provided code snippet?\n \n\ncount = start\nwhile(count < stop): \n count = count + step \n \n count += step \n\n", "It increments the value of 'count' by 'step'", "It decrements the value of 'count' by 'step'", "It resets the value of 'count' to 'step'", "It multiplies the value of 'count' by 'step'", "It divides the value of 'count' by 'step'", "It increments the value of 'count' by 'step'")
MCQ("Which of the following correctly describes the purpose of the 'step' variable in the provided code snippet?\n \n\ncount = start\nwhile(count < stop): \n count = count + step \n \n count += step \n\n", "It determines the increment or decrement value for 'count'", "It sets the starting value of 'count'", "It defines the stopping condition for the loop", "It checks if 'count' has reached 'stop'", "It initializes the loop counter", "It determines the increment or decrement value for 'count'")
MCQ("What happens if the condition 'count < stop' evaluates to False initially?\n \n\ncount = start\nwhile(count < stop): \n count = count + step \n \n count += step \n\n", "The loop body will not execute at all", "The loop will execute indefinitely", "The loop will terminate immediately", "The loop will print 'count'", "The loop will reset 'count' to zero", "The loop body will not execute at all")
MCQ("What is the primary role of the 'step' variable in the while loop?\n \n\ncount = start\nwhile(count < stop): \n count = count + step \n \n count += step \n\n", "To control the increment or decrement of 'count'", "To set the initial value of 'count'", "To define the loop's termination condition", "To check if 'count' has reached 'stop'", "To print the value of 'count'", "To control the increment or decrement of 'count'")
MCQ("What is the effect of changing 'count += step' to 'count -= step' in the provided code snippet?\n \n\ncount = start\nwhile(count < stop): \n count = count + step \n \n count += step \n\n", "It decrements the value of 'count' by 'step' instead of incrementing it", "It resets the value of 'count' to 'step'", "It multiplies the value of 'count' by 'step'", "It divides the value of 'count' by 'step'", "It increments the value of 'count' by 'step' instead of decrementing it", "It decrements the value of 'count' by 'step' instead of incrementing it")
MCQ("What would be the effect if the condition in the while loop were changed to 'count <= stop'?\n \n\ncount = start\nwhile(count < stop): \n count = count + step \n \n count += step \n\n", "The loop would print an additional value of 'count'", "The loop would not execute at all", "The loop would execute indefinitely", "The loop would print values of 'count' in reverse order", "The loop would print values of 'count' in ascending order", "The loop would print an additional value of 'count'")
MCQ("What would happen if the condition in the while loop were changed to 'count == stop'?\n \n\ncount = start\nwhile(count < stop): \n count = count + step \n \n count += step \n\n", "The loop may not execute at all depending on the initial values of 'count' and 'stop'", "The loop would print an additional value of 'count'", "The loop would execute indefinitely", "The loop would print values of 'count' in reverse order", "The loop would print values of 'count' in ascending order", "The loop may not execute at all depending on the initial values of 'count' and 'stop'")

'COUNTING UP++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
'0 to Positive By 1s'
MCQ("Consider the code snippet below:\n\nx = 0\nwhile x <= 5:\n print(x)\n x += 1\nWhat will be the output of the code?", "0, 1, 2, 3, 4, 5", "5, 4, 3, 2, 1, 0", "0, 2, 4", "0, 1, 2, 3, 4", "0, 5", "0, 1, 2, 3, 4, 5")
MCQ("Consider the code snippet below:\n\nx = 0\nwhile x < 8:\n print(x end = ' ')\n x += 1\nWhat will be the output of the code?", "0 1 2 3 4 5 6 7", "7 6 5 4 3 2 1 0", "0 1 2 3 4 5 6 7 8", "8 7 6 5 4 3 2 1", "1 2 3 4 5 6 7 8", "0 1 2 3 4 5 6 7")

'0 to Positive By Multiples'
MCQ("Consider the code snippet below:\n\nx = 0\nwhile x < 10:\n print(x)\n x += 3\nWhat will be the output of the code?","0, 3, 6, 9","10, 7, 4, 1","0, 1, 2, 3, 4, 5, 6, 7, 8, 9","9, 6, 3, 0","10, 8, 6, 4, 2","0, 3, 6, 9")
MCQ("Consider the code snippet below:\n\nx = 0\nwhile x < 100:\n print(x)\n x += 25\nWhat will be the output of the code?","0, 25, 50, 75","100, 75, 50, 25, 0","0, 1, 2, 3, ..., 99","99, 74, 49, 24","100, 75, 50, 25","0, 25, 50, 75")

'From 1 to Positive by 1s'
MCQ("Consider the code snippet below:\n\nx = 1\nwhile x <= 10:\n print(x)\n x += 1\nWhat will be the output of the code?","1, 2, 3, 4, 5, 6, 7, 8, 9, 10","10, 9, 8, 7, 6, 5, 4, 3, 2, 1","1, 3, 5, 7, 9","1, 2, 3, 4, 5, 6, 7, 8, 9","1, 1, 1, 1, 1, 1, 1, 1, 1, 1","1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
MCQ("Consider the code snippet below:\n\nx = 1\nwhile x < 7:\n print(x)\n x += 1\nWhat will be the output of the code?","1, 2, 3, 4, 5, 6","6, 5, 4, 3, 2, 1","1, 3, 5","1, 2, 3, 4, 5, 6, 7","1, 1, 1, 1, 1, 1","1, 2, 3, 4, 5, 6")


'From 1 to Positive by Multiples'
MCQ("What will be the output of the following code snippet?\n\nx = 1\nwhile x <= 10:\n print(x)\n x += 2", "1, 3, 5, 7, 9", "2, 4, 6, 8, 10", "1, 2, 3, 4, 5", "2, 3, 5, 7, 11", "1, 3, 5, 7, 11", "1, 3, 5, 7, 9")
MCQ("Consider the code snippet below:\n\nx = 10\nwhile x % 3 != 0:\n print(x)\n x += 1\nWhat will be the output of the code?", "10", "10, 11", "10, 11, 12", "10, 12, 14", "10, 13, 16", "10, 11, 12")

'From Positive to Positive by 1s'
MCQ("What will be the output of the following code snippet?\n\nx = 3\nwhile x <= 8:\n print(x)\n x += 1", "3, 4, 5, 6, 7, 8", "8, 7, 6, 5, 4, 3", "3, 5, 7, 9, 11, 13", "4, 6, 8, 10, 12, 14", "2, 4, 6, 8, 10, 12", "3, 4, 5, 6, 7, 8")
MCQ("What will be the output of the following code snippet?\n\nx = 50\nwhile x <= 57:\n print(x)\n x += 1", "50, 51, 52, 53, 54, 55, 56, 57", "57, 56, 55, 54, 53, 52, 51, 50", "50, 52, 54, 56, 58, 60, 62, 64", "51, 53, 55, 57, 59, 61, 63, 65", "49, 50, 51, 52, 53, 54, 55, 56, 57", "50, 51, 52, 53, 54, 55, 56, 57")

'From Positive to Positive by Mutliples'
MCQ("What will be the output of the following code snippet?\n\nx = 100\nwhile x <= 130:\n print(x)\n x += 5", "100, 105, 110, 115, 120, 125, 130", "130, 125, 120, 115, 110, 105, 100", "100, 95, 90, 85, 80, 75", "105, 110, 115, 120, 125, 130, 135", "99, 104, 109, 114, 119, 124, 129", "100, 105, 110, 115, 120, 125, 130")
MCQ("What will be the output of the following code snippet?\n\nx = 10\nwhile x <= 25:\n print(x)\n x += 3", "10, 13, 16, 19, 22, 25", "25, 22, 19, 16, 13, 10", "10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25", "13, 16, 19, 22, 25, 28", "9, 12, 15, 18, 21, 24", "10, 13, 16, 19, 22, 25")


'From Negative to 0 by 1s'
MCQ("What will be the output of the following code snippet?\n\nx = -3\nwhile x <= 0:\n print(x)\n x += 1", "-3, -2, -1, 0", "0, -1, -2, -3", "-3, -4, -5, -6", "1, 2, 3, 4", "-3, -1, 1", "-3, -2, -1, 0")
MCQ("Consider the code snippet below:\n\nx = -10\nwhile x <= 0:\n print(x)\n x += 1\nWhat will be the output of the code?", "-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0", "0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10", "-10, -8, -6, -4, -2, 0", "-9, -7, -5, -3, -1", "-3, -2, -1, 0", "-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0")


'From Negative to 0 by Multiples'
MCQ("What will be the output of the following code snippet?\n\nx = -4\nwhile x <= 0:\n print(x)\n x += 2", "-4, -2, 0", "0, -2, -4", "-4, -6, -8, -10, -12, -14, -16, -18, -20", "-3, -1, 1", "-4, -2", "-4, -2, 0")
MCQ("Given the code snippet below:\n\nx = -15\nwhile x <= 0:\n print(x)\n x += 3\nWhat will be the output of the code?", "-15, -12, -9, -6, -3, 0", "0, -3, -6, -9, -12, -15", "-15, -18, -21, -24, -27, -30", "-14, -11, -8, -5, -2", "-15, -12, -9, -6, -3", "-15, -12, -9, -6, -3, 0")
MCQ("Given the code snippet below:\n\nx = -8\nwhile x <= -3:\n print(x)\n x += 1\nWhat will be the output of the code?","-8, -7, -6, -5, -4, -3","-3, -4, -5, -6, -7, -8","-8, -6, -4","-3, -2, -1","-8, -9, -10","-8, -6, -4")

'From Negative to Negative by 1s'
MCQ("Given the code snippet below:\n\nx = -20\nwhile x <= -15:\n print(x)\n x += 1\nWhat will be the output of the code?", "-20, -19, -18, -17, -16, -15", "-20, -19, -18, -17, -16", "-20, -18, -16, -14, -12, -10", "-21, -20, -19, -18, -17, -16", "-20, -21, -22, -23, -24, -25", "-20, -19, -18, -17, -16, -15")
MCQ("Given the code snippet below:\n\nx = -8\nwhile x <= -3:\n print(x)\n x += 1\nWhat will be the output of the code?", "-8, -6, -4, -2", "-3, -5, -7", "-8, -10, -12, -14", "-8, -7, -6, -5, -4, -3", "-8, -5, -2", "-8, -7, -6, -5, -4, -3")

'From Negative to Negative by Multiples'
MCQ("Consider the code snippet below:\n\nx = -20\nwhile x <= -7:\n print(x)\n x += 4\nWhat will be the output of the code?", "-20, -16, -12, -8", "-7, -11, -15, -19", "-20, -16, -12, -8, -4, 0", "-20, -16, -12, -8, -4", "-20, -16, -12, -7", "-20, -16, -12, -8")
MCQ("Given the code snippet below:\n\nx = -25\nwhile x <= -15:\n print(x)\n x += 3\nWhat will be the output of the code?", "-25, -22, -19, -16, -12, -8", "-15, -18, -21, -24", "-25, -22, -19, -16, -13, -10", "-25, -22, -19, -16", "-25, -22, -19, -16, -13, -10, -7", "-25, -22, -19, -16")

'From Negative to Positive by 1s'
MCQ("Given the code snippet below:\n\nx = -5\nwhile x < 5:\n print(x)\n x += 1\nWhat will be the output of the code?", "-5, -4, -3, -2, -1, 0, 1, 2, 3, 4", "5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5", "-5, -3, -1, 1, 3, 5", "-5, -4, -3, -2, -1", "-5, -1, 3", "-5, -4, -3, -2, -1, 0, 1, 2, 3, 4")
MCQ("Consider the code snippet below:\n\nx = -10\nwhile x <= 10:\n print(x)\n x += 1\nWhat will be the output of the code?", "-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10", "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10", "-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10", "-10, -9, -8, -7, -6, -5, -4, -3, -2, -1", "-10, -1, 8", "-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")


'From Negative to Positive by Multiples'
MCQ("Given the code snippet below:\n\nx = -10\nwhile x <= 10:\n print(x)\n x += 3\nWhat will be the output of the code?", "-10, -7, -4, -1, 2, 5, 8", "10, 7, 4, 1, -2, -5, -8", "-10, -13, -16, -19", "'-10, -7, -4, -1, 1, 4, 7, 10'", "-10, -7, -4, -1, 2, 5, 8, 11", "-10, -7, -4, -1, 2, 5, 8")
MCQ("Consider the code snippet below:\n\nx = -15\nwhile x <= 15:\n print(x)\n x += 4\nWhat will be the output of the code?", "-15, -11, -7, -3, 1, 5, 9, 13", "15, 11, 7, 3, -1, -5, -9, -13", "-15, -19, -23", "-15, -11, -7, -3, 0, 4, 8, 12, 16", "-15, -11, -7, -3, 1, 5, 9, 13, 17", "-15, -11, -7, -3, 1, 5, 9, 13")

'COUNTING DOWN++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
'From Positive to 0 by 1s'
MCQ("Given the code snippet below:\n\nx = 5\nwhile x >= 0:\n print(x)\n x -= 1\nWhat will be the output of the code?", "5, 4, 3, 2, 1, 0", "0, 1, 2, 3, 4, 5", "5, 3, 1", "5, 4, 3, 2, 1", "5, 2", "5, 4, 3, 2, 1, 0")
MCQ("Consider the code snippet below:\n\nx = 10\nwhile x >= 0:\n print(x)\n x -= 1\nWhat will be the output of the code?", "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0", "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10", "10, 8, 6, 4, 2, 0", "10, 9, 8, 7, 6, 5, 4, 3, 2, 1", "10, 7, 4, 1", "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0")

'From Positive to 0 by Multiples'
MCQ("Given the code snippet below:\n\nx = 10\nwhile x >= 0:\n print(x)\n x -= 3\nWhat will be the output of the code?", "10, 7, 4, 1, 0", "0, 3, 6, 9, 12", "10, 8, 6, 4, 2, 0", "10, 7, 4, 1", "10, 6, 2", "10, 7, 4, 1")
MCQ("Consider the code snippet below:\n\nx = 15\nwhile x >= 0:\n print(x)\n x -= 4\nWhat will be the output of the code?", "15, 11, 7, 3, 0", "0, 4, 8, 12, 16", "15, 12, 9, 6, 3, 0", "15, 11, 7, 3", "15, 10, 5, 0", "15, 11, 7, 3")

'From Positive to Positive by 1s'
MCQ("Given the code snippet below:\n\nx = 65\nwhile x >= 53:\n print(x)\n x -= 1\nWhat will be the output of the code?", "65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53", "53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65", "65, 63, 61, 59, 57, 55, 53", "65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54", "65, 53", "65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53")
MCQ("Consider the code snippet below:\n\nx = 100\nwhile x > 91:\n print(x)\n x -= 1\nWhat will be the output of the code?", "100, 99, 98, 97, 96, 95, 94, 93, 92, 91", "91, 92, 93, 94, 95, 96, 97, 98, 99, 100", "100, 98, 96, 94, 92", "100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90", "100, 99, 98, 97, 96, 95, 94, 93, 92", "100, 99, 98, 97, 96, 95, 94, 93, 92")

'From Positive to Positive by Multiples'
MCQ("Given the code snippet below:\n\nx = 10\nwhile x >= 3:\n print(x)\n x -= 3\nWhat will be the output of the code?", "10, 7, 4", "3, 6, 9", "10, 7, 4, 1", "10, 9, 8, 7, 6, 5, 4, 3", "10, 4", "10, 7, 4")
MCQ("Consider the code snippet below:\n\nx = 20\nwhile x >= 4:\n print(x)\n x -= 4\nWhat will be the output of the code?", "20, 16, 12, 8, 4", "4, 8, 12, 16, 20", "20, 16, 12, 8, 4, 0", "20, 15, 10, 5", "20, 16, 12, 8", "20, 16, 12, 8, 4")

'From Positive to Negative by 1s'
MCQ("Given the code snippet below:\n\nx = 10\nwhile x > -5:\n print(x)\n x -= 1\nWhat will be the output of the code?", "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5", "-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10", "10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10", "10, 9, 8, 7, 6, 5, 4, 3, 2, 1", "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4", "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4")
MCQ("Consider the code snippet below:\n\nx = 5\nwhile x >= -10:\n print(x)\n x -= 1\nWhat will be the output of the code?","5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10","5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9","-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5","-10, -9, -8, -7, -6, -5, -4, -3, -2, -1","-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5","5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10")

'From Positive to Negative by Multiples'
MCQ("Given the code snippet below:\n\nx = 10\nwhile x >= -5:\n print(x)\n x -= 2\nWhat will be the output of the code?", "10, 8, 6, 4, 2, 0, -2, -4, -6", "10, 8, 6, 4, 2, 0, -2, -4", "10, 8, 6, 4, 2, 0, -2, -4, -6, -8", "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5", "10, 8, 6, 4, 2, 0, -3, -5", "10, 8, 6, 4, 2, 0, -2, -4")
MCQ("Consider the code snippet below:\n\nx = 20\nwhile x >= -10:\n print(x)\n x -= 3\nWhat will be the output of the code?", "20, 17, 14, 11, 8, 5, 2, -1, -4, -7, -10", "-10, -7, -4, -1, 2, 5, 8, 11, 14, 17, 20", "20, 17, 14, 11, 8, 5, 2, -1, -4, -7", "20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10", "20, 17, 14, 11, 8, 5, 2, -1, -4, -7, -10, -13", "20, 17, 14, 11, 8, 5, 2, -1, -4, -7, -10")

'From 0 to Negative by 1s'
MCQ("Given the code snippet below:\n\nx = 0\nwhile x >= -5:\n print(x)\n x -= 1\nWhat will be the output of the code?", "0, -1, -2, -3, -4, -5", "-5, -4, -3, -2, -1, 0", "0, -2, -4", "0, -1, -2, -3, -4", "0, -3", "0, -1, -2, -3, -4, -5")
MCQ("Consider the code snippet below:\n\nx = 0\nwhile x >= -10:\n print(x)\n x -= 1\nWhat will be the output of the code?", "0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10", "-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0", "0, -2, -4, -6, -8, -10", "0, -1, -2, -3, -4, -5, -6, -7, -8, -9", "0, -5, -10", "0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10")

'From 0 to Negative by Multiples'
MCQ("Given the code snippet below:\n\nx = 0\nwhile x >= -10:\n print(x)\n x -= 3\nWhat will be the output of the code?", "0, -3, -6, -9", "-10, -7, -4, -1", "0, -2, -4, -6, -8, -10", "0, -3, -6", "0, -10", "0, -3, -6, -9")
MCQ("Consider the code snippet below:\n\nx = 0\nwhile x > -7:\n print(x)\n x -= 2\nWhat will be the output of the code?", "0, -2, -4, -6", "-7, -5, -3, -1", "0, -1, -2, -3, -4, -5, -6, -7", "0, -2, -4", "0, -7", "0, -2, -4, -6")

'From Negative to Negative by 1s'
MCQ("What will be the output of the following code snippet?\n\nx = -3\nwhile x >= -7:\n print(x)\n x -= 1", "-3, -4, -5, -6, -7", "-7, -6, -5, -4, -3", "-3, -2, -1, 0, 1", "-4, -3, -2, -1, 0", "-3, -2, -1", "-3, -4, -5, -6, -7")
MCQ("Given the code snippet below:\n\nx = -10\nwhile x >= -15:\n print(x)\n x -= 1\nWhat will be the output of the code?", "-10, -11, -12, -13, -14, -15", "-15, -14, -13, -12, -11, -10", "-10, -12, -14, -16, -18, -20", "-11, -12, -13, -14, -15", "-10, -11, -12, -13, -14", "-10, -11, -12, -13, -14, -15")
MCQ("Given the code snippet below:\n\nx = -5\nwhile x > -10:\n print(x)\n x -= 1\nWhat will be the output of the code?", "-5, -6, -7, -8, -9, -10", "-10, -9, -8, -7, -6, -5", "-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5", "-5, -6, -7, -8, -9", "-5, -10", "-5, -6, -7, -8, -9")
MCQ("Consider the code snippet below:\n\nx = -3\nwhile x > -7:\n print(x)\n x -= 1\nWhat will be the output of the code?", "-3, -4, -5, -6, -7", "-7, -6, -5, -4, -3", "-3, -2, -1, 0, 1, 2, 3, 4, 5", "-3, -4, -5, -6", "-3, -7", "-3, -4, -5, -6")

'From Negative to Negative by Multiples'
MCQ("Given the code snippet below:\n\nx = -3\nwhile x >= -10:\n print(x)\n x -= 3\nWhat will be the output of the code?", "-3, -6, -9", "-10, -7, -4, -1", "-3, -5, -7, -9", "-3, -6", "-3, -10", "-3, -6, -9")
MCQ("Consider the code snippet below:\n\nx = -2\nwhile x > -8:\n print(x)\n x -= 2\nWhat will be the output of the code?", "-2, -4, -6, -8", "-8, -6, -4, -2", "-2, -3, -4, -5, -6, -7, -8", "-2, -4, -6", "-2, -8", "-2, -4, -6")


'> Infinite Loops and Off by 1 Errors'
MCQ("Which of the following best defines an infinite loop in programming?", "A loop that continues indefinitely because its exit condition is never met", "A loop that terminates after a fixed number of iterations", "A loop that contains only one iteration", "A loop that executes a block of code exactly once", "A loop that executes until a specific condition is met", "A loop that continues indefinitely because its exit condition is never met")
MCQ("In a while loop, what causes an infinite loop?", "An exit condition that is never met", "An exit condition that is always met", "A condition that changes after each iteration", "A condition that is randomly generated", "A condition that relies on user input", "An exit condition that is never met")
MCQ("What is the most likely outcome of running code containing an infinite loop?", "The program will hang or freeze", "The program will terminate normally", "The program will display an error message", "The program will execute only once", "The program will execute as expected without any issues", "The program will hang or freeze")
MCQ("How can you identify an infinite loop in your code?", "By analyzing the loop's step variable", "By running the code and observing if it gets stuck in the loop indefinitely", "By counting the number of iterations in the loop", "By checking if the loop contains any errors", "By looking for keywords such as 'infinite' or 'loop'", "By running the code and observing if it gets stuck in the loop indefinitely")
MCQ("What is a potential consequence of inadvertently creating an infinite loop in your code?", "Consumption of excessive system resources leading to program malfunction or system crash", "Improved program performance", "Enhanced code readability", "Increased code efficiency", "Reduced likelihood of bugs", "Consumption of excessive system resources leading to program malfunction or system crash")

MCQ("What will happen if the following code snippet is executed?\n\nwhile True:\n print('Looping...')\n\n",
"The code will print 'Looping...' repeatedly until interrupted",
"The code will print 'Looping...' once and then stop",
"The code will raise a syntax error",
"The code will print nothing",
"The code will cause the system to crash",
"The code will print 'Looping...' repeatedly until interrupted")  

MCQ("What modification would fix the infinite loop in the following code snippet?\n\nwhile True:\n print('Infinite loop!')\n\n",
"Add a conditional statement to break out of the loop when a specific condition is met",
"Replace 'True' with a condition that evaluates to False to terminate the loop",
"Remove the 'print' statement to prevent the loop from executing infinitely",
"Increase the loop counter to limit the number of iterations",
"Use the 'continue' statement to skip the current iteration and proceed to the next one",
"Add a conditional statement to break out of the loop when a specific condition is met")


