'> For Loop Syntax'
MCQ("What symbol marks the beginning of a for loop in Python?","for","while","do","foreach","loop","for")
MCQ("In a for loop syntax, what comes after the 'for' keyword?","variable","condition","iteration","increment","statement","variable")
MCQ("What symbol does a for loop header end with?",":",";","{","}","#",":")
MCQ("What do you use to iterate over a sequence of numbers in a for loop?","range()","if-else","while","break","continue","range()")
MCQ("Which of the following statements is true regarding the loop variable in a Python for loop?","The loop variable retains its value after the loop completes","The loop variable is only accessible within the loop","The loop variable can be reassigned within the loop","The loop variable cannot be used as a list index","All of these","All of these")
MCQ("In Python, why is proper indentation important in for loops?","It defines the block of code to be executed within the loop","It determines the number of iterations in the loop","It specifies the loop variable","It controls the termination condition of the loop","None of these","It defines the block of code to be executed within the loop")
MCQ("Which of the following lines contains an indentation error in this Python for loop?\n\nfor i in range(5):\nprint(i)\n    print('Loop iteration:', i)","for i in range(5):","print(i)","print('Loop iteration:', i)","None of these","All of these","print(i)")
MCQ("What will happen if the colon (:) is missing in the following Python for loop declaration?\nfor i in range(5)\n    print(i)","The loop will execute without any errors","The loop will raise a SyntaxError","The loop will only execute once","The loop will run indefinitely","None of these","The loop will raise a SyntaxError")
MCQ("How many times will the block of code within the following Python for loop execute?\n\nfor i in range(3):\n    print('Iteration', i)\n","1 time","2 times","3 times","4 times","None of these","3 times")
MCQ("How many times will the block of code within the following Python for loop execute?\n\nfor i in range(5):\n    print('Number:', i)\n","5 times","4 times","6 times","0 times","None of these","5 times")
MCQ("How many times will the block of code within the following Python for loop execute?\n\nfor i in range(0):\n    print('Count:', i)\n","0 times","1 time","Infinite times","Depends on the range function","None of these","0 times")
MCQ("How many times will the block of code within the following Python for loop execute?\n\nfor i in range(2, 5):\n    print('Value:', i)\n","3 times","2 times","4 times","5 times","None of these","3 times")
MCQ("How many times will the block of code within the following Python for loop execute?\n\nfor i in range(1, 10, 2):\n    print('Number:', i)\n","5 times","4 times","3 times","6 times","None of these","5 times")
MCQ("How many times will the block of code within the following Python for loop execute?\n\nfor i in range(10, 5, -1):\n    print('Countdown:', i)\n","5 times","4 times","3 times","6 times","None of these","5 times")


'> the range constructor'
MCQ("In Python, what is the purpose of the 'range()' function often used with for loops?","To generate a sequence of numbers","To specify the end point of a loop","To check the validity of loop conditions","To iterate over a list","None of these","To generate a sequence of numbers")
MCQ("What is the output of the following code:\n\nfor x in range(5):\n    print(x, end = ' ')", "1 2 3 4 5", "0 1 2 3 4", "SyntaxError", "5 4 3 2 1", "4 3 2 1 0","0 1 2 3 4")
MCQ("What is the purpose of the 'range()' constructor in Python?","To generate a sequence of numbers","To create a list of elements","To define the range of a loop","To specify the number of iterations in a loop","None of these","To generate a sequence of numbers")
MCQ("Which of the following statements is true about the 'range()' constructor in Python?","It can take up to three arguments: start, stop, and step","It can only take one argument: the stop value","It alway generates a sequence starting from 0","It generates a sequence of even numbers only","None of these","It can take up to three arguments: start, stop, and step")
MCQ("What will be the output of the following code snippet?\n\nfor i in range(3):\n print(i, end = ' ')\n","0 1 2","1 2 3","0 1 2 3","1 2 3 4","None of these","0 1 2")
MCQ("In the 'range()' constructor, what happens if you leave out the start argument? Example: range(4)","It defaults to 0","It defaults to 1","It defaults to -1","It raises an error","None of these","It defaults to 0")
MCQ("Which of the following is a valid way to iterate backwards using the 'range()' constructor?","range(-10, 0, -1)","range(0, 10, -1)","range(10, -1, -1)","range(0, -10, -1)","None of these","range(10, -1, -1)")
MCQ("What is the default start value of the 'range()' constructor in Python if not specified?","0","1","-1","None (start value must be specified)","None of these","0")
MCQ("What is the default step value of the 'range()' constructor in Python if not specified?","1","0","-1","None (step value must be specified)","None of these","1")
MCQ("When using the 'range()' constructor in Python, is the start value included in the generated sequence by default?","No, the start value is excluded by default","Yes, the start value is included by default","It depends on the Python version","There is no start value", " None of these","Yes, the start value is included by default")
MCQ("In Python's 'range()' constructor, is the stop value included in the generated sequence?","No, the stop value is excluded","Yes, the stop value is included","It depends on the step value","It depends on the start value"," None of these","No, the stop value is excluded")

'> Counting Up by 1 and by multiples'
'0 to Positive by 1s'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(6):\n    print(i, end = ' ')\n","0 1 2 3 4 5","1 2 3 4 5 6","0 1 2 3 4 5 6","1 2 3 4 5"," None of these","0 1 2 3 4 5")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(0, 6, 1):\n print(i, end=' ')\n", "0 1 2 3 4 5", "1 2 3 4 5 6", "0 1 2 3 4", "0 1 2 3 4 5 6", " None of these", "0 1 2 3 4 5")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(11):\n print(i, end=' ')\n", "0 1 2 3 4 5 6 7 8 9 10", "1 2 3 4 5 6 7 8 9 10 11", "0 1 2 3 4 5 6 7 8 9", "0 1 2 3 4 5 6 7 8 9 10 11", " None of these", "0 1 2 3 4 5 6 7 8 9 10")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(0, 21):\n print(i, end=' ')\n", "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20", "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21", "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19", "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21", " None of these", "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20")

'0 to Positive by Multiples'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(0, 10, 2):\n    print(i, end=' ')\n", "0 2 4 6 8", "2 4 6 8 10", "0 2 4 6 8 10", "0 2 4 6", " None of these", "0 2 4 6 8")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(0, 20, 5):\n    print(i, end=' ')\n", "0 5 10 15", "5 10 15 20", "0 5 10 15 20", "0 5 10 15 20 25", " None of these", "0 5 10 15")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(0, 30, 3):\n    print(i, end=' ')\n", "0 3 6 9 12 15 18 21 24 27", "3 6 9 12 15 18 21 24 27 30", "0 3 6 9 12 15 18 21 24 27 30", "0 3 6 9 12 15 18 21", " None of these", "0 3 6 9 12 15 18 21 24 27")

'From 1 to Positive by 1s'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(1, 6):\n    print(i)\n","1 2 3 4 5","2 3 4 5 6","0 1 2 3 4","1 3 5 7 9"," None of these","1 2 3 4 5")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(1, 8, 1):\n    print(i, end=' ')\n", "1 2 3 4 5 6 7", "0 1 2 3 4 5 6", "2 3 4 5 6 7 8", "1 2 3 4 5 6", " None of these", "1 2 3 4 5 6 7")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(1, 16):\n    print(i, end=' ')\n", "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", "0 1 2 3 4 5 6 7 8 9 10 11 12 13", "2 3 4 5 6 7 8 9 10 11 12 13 14 15 16", "1 2 3 4 5 6 7 8 9 10 11 12 13 14", " None of these", "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(1, 26, 1):\n    print(i, end=' ')\n", "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25", "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24", "2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26", "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24", " None of these", "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25")
        
'From 1 to Postive by Multiples'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(1, 21, 2):\n    print(i, end=' ')\n", "1 3 5 7 9 11 13 15 17 19", "2 4 6 8 10 12 14 16 18 20", "1 3 5 7 9 11 13 15 17 19 21", "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20", " None of these", "1 3 5 7 9 11 13 15 17 19")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(1, 31, 3):\n    print(i, end=' ')\n", "1 4 7 10 13 16 19 22 25 28", "3 6 9 12 15 18 21 24 27 30", "1 3 5 7 9 11 13 15 17 19 21 23 25 27 29", "1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31", " None of these", "1 4 7 10 13 16 19 22 25 28")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(1, 41, 4):\n    print(i, end=' ')\n", "1 5 9 13 17 21 25 29 33 37", "2 6 10 14 18 22 26 30 34 38", "1 4 7 10 13 16 19 22 25 28 31 34 37 40", "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20", " None of these", "1 5 9 13 17 21 25 29 33 37")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(1, 51, 5):\n    print(i, end=' ')\n", "1 6 11 16 21 26 31 36 41 46", "5 10 15 20 25 30 35 40 45 50", "1 5 9 13 17 21 25 29 33 37 41 45 49", "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20", " None of these", "1 6 11 16 21 26 31 36 41 46")

'From Positive to Positive by 1s'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(3, 8, 1):\n    print(i, end=' ')\n", "3 4 5 6 7", "4 5 6 7 8", "3 4 5 6", "4 5 6", " None of these", "3 4 5 6 7")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(5, 15):\n    print(i, end=' ')\n", "5 6 7 8 9 10 11 12 13 14", "4 5 6 7 8 9 10 11 12 13 14", "5 6 7 8 9 10 11 12 13", "4 5 6 7 8 9 10 11 12 13", " None of these", "5 6 7 8 9 10 11 12 13 14")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(20, 30, 1):\n    print(i, end=' ')\n", "20 21 22 23 24 25 26 27 28 29", "21 22 23 24 25 26 27 28 29 30", "20 21 22 23 24 25 26 27 28 29 30", "19 20 21 22 23 24 25 26 27 28 29 30", " None of these", "20 21 22 23 24 25 26 27 28 29")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(15, 25):\n    print(i, end=' ')\n", "15 16 17 18 19 20 21 22 23 24", "14 15 16 17 18 19 20 21 22 23 24", "15 16 17 18 19 20 21 22 23 24 25", "14 15 16 17 18 19 20 21 22 23", " None of these", "15 16 17 18 19 20 21 22 23 24")

'From Positive to Positive by Multiples'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(3, 31, 3):\n    print(i, end=' ')\n", "3 6 9 12 15 18 21 24 27 30", "2 4 6 8 10 12 14 16 18 20 22 24 26 28 30", "3 6 9 12 15 18 21 24 27", "3 6 9 12 15 18 21 24", " None of these", "3 6 9 12 15 18 21 24 27 30")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(5, 51, 5):\n    print(i, end=' ')\n", "5 10 15 20 25 30 35 40 45 50", "5 10 15 20 25 30 35 40 45 50 55", "10 15 20 25 30 35 40 45 50 55", "5 10 15 20 25 30 35 40 45 50 55 60", " None of these", "5 10 15 20 25 30 35 40 45 50")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(4, 41, 4):\n    print(i, end=' ')\n", "4 8 12 16 20 24 28 32 36 40", "4 8 12 16 20 24 28 32 36 40 44", "8 12 16 20 24 28 32 36 40 44", "4 8 12 16 20 24 28 32 36", " None of these", "4 8 12 16 20 24 28 32 36 40")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(6, 61, 6):\n    print(i, end=' ')\n", "6 12 18 24 30 36 42 48 54 60", "6 12 18 24 30 36 42 48 54 60 66", "12 18 24 30 36 42 48 54 60 66", "6 12 18 24 30 36 42 48 54", " None of these", "6 12 18 24 30 36 42 48 54 60")

'From Negative to Negative by 1s'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-5, -15, -1):\n    print(i, end=' ')\n", "-5 -6 -7 -8 -9 -10 -11 -12 -13 -14", "-4 -5 -6 -7 -8 -9 -10 -11 -12 -13", "-5 -6 -7 -8 -9 -10 -11 -12 -13", "-4 -5 -6 -7 -8 -9 -10 -11 -12", " None of these", "-5 -6 -7 -8 -9 -10 -11 -12 -13 -14")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-10, -20, -1):\n    print(i, end=' ')\n", "-10 -11 -12 -13 -14 -15 -16 -17 -18 -19", "-11 -12 -13 -14 -15 -16 -17 -18 -19 -20", "-10 -11 -12 -13 -14 -15 -16 -17 -18", "-11 -12 -13 -14 -15 -16 -17 -18 -19", " None of these", "-10 -11 -12 -13 -14 -15 -16 -17 -18 -19")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-15, -25, -1):\n    print(i, end=' ')\n", "-15 -16 -17 -18 -19 -20 -21 -22 -23 -24", "-14 -15 -16 -17 -18 -19 -20 -21 -22 -23", "-15 -16 -17 -18 -19 -20 -21 -22 -23", "-14 -15 -16 -17 -18 -19 -20 -21 -22", " None of these", "-15 -16 -17 -18 -19 -20 -21 -22 -23 -24")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-20, -30, -1):\n    print(i, end=' ')\n", "-20 -21 -22 -23 -24 -25 -26 -27 -28 -29", "-19 -20 -21 -22 -23 -24 -25 -26 -27 -28", "-20 -21 -22 -23 -24 -25 -26 -27 -28", "-19 -20 -21 -22 -23 -24 -25 -26 -27", " None of these", "-20 -21 -22 -23 -24 -25 -26 -27 -28 -29")

'From Negative to Negative by Multiples'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-3, -16, -3):\n    print(i, end=' ')\n", "-3 -6 -9 -12 -15", "-3 -6 -9 -12", "-3 -6 -9 -12 -15 -18", "-4 -7 -10 -13 -16", " None of these", "-3 -6 -9 -12 -15")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-5, -26, -5):\n    print(i, end=' ')\n", "-5 -10 -15 -20 -25", "-5 -10 -15 -20", "-5 -10 -15 -20 -25 -30", "-4 -9 -14 -19 -24", " None of these", "-5 -10 -15 -20 -25")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-4, -25, -4):\n    print(i, end=' ')\n", "-4 -8 -12 -16 -20 -24", "-4 -8 -12 -16 -20", "-4 -8 -12 -16 -20 -24 -28", "-5 -9 -13 -17 -21 -25", " None of these", "-4 -8 -12 -16 -20 -24")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-6, -31, -6):\n    print(i, end=' ')\n", "-6 -12 -18 -24 -30", "-6 -12 -18 -24", "-6 -12 -18 -24 -30 -36", "-5 -11 -17 -23 -29", " None of these", "-6 -12 -18 -24 -30")

'From Negative to Positive by 1s'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-5, 6):\n    print(i, end=' ')\n", "-5 -4 -3 -2 -1 0 1 2 3 4 5", "-4 -3 -2 -1 0 1 2 3 4 5 6", "-5 -4 -3 -2 -1 0 1 2 3 4 5 6", "-6 -5 -4 -3 -2 -1 0 1 2 3 4 5", " None of these", "-5 -4 -3 -2 -1 0 1 2 3 4 5")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-2, 3):\n    print(i, end=' ')\n", "-2 -1 0 1 2", "-1 0 1 2 3", "-2 -1 0 1 2 3", "-3 -2 -1 0 1 2", " None of these", "-2 -1 0 1 2")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-3, 4):\n    print(i, end=' ')\n", "-3 -2 -1 0 1 2 3", "-2 -1 0 1 2 3 4", "-3 -2 -1 0 1 2 3 4", "-4 -3 -2 -1 0 1 2 3", " None of these", "-3 -2 -1 0 1 2 3")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-4, 5):\n    print(i, end=' ')\n", "-4 -3 -2 -1 0 1 2 3 4", "-3 -2 -1 0 1 2 3 4 5", "-4 -3 -2 -1 0 1 2 3 4 5", "-5 -4 -3 -2 -1 0 1 2 3 4", " None of these", "-4 -3 -2 -1 0 1 2 3 4")

'From Negative to Positive by Multiples'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-10, 21, 5):\n    print(i, end=' ')\n", "-10 -5 0 5 10 15 20", "-10 -5 0 5 10 15 20 25", "-10 -5 0 5 10 15 20 25 30", "-9 -4 1 6 11 16 21 26", " None of these", "-10 -5 0 5 10 15 20")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-15, 36, 6):\n    print(i, end=' ')\n", "-15 -9 -3 3 9 15 21 27 33", "-15 -9 -3 3 9 15 21 27 33 39", "-15 -9 -3 3 9 15 21 27 33 39 45", "-14 -8 -2 4 10 16 22 28 34 40", " None of these", "-15 -9 -3 3 9 15 21 27 33")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-7, 46, 7):\n    print(i, end=' ')\n", "-7 0 7 14 21 28 35 42", "-7 0 7 14 21 28 35 42 49", "-7 0 7 14 21 28 35 42 49 56", "-6 1 8 15 22 29 36 43", " None of these", "-7 0 7 14 21 28 35 42")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-8, 61, 8):\n    print(i, end=' ')\n", "-8 0 8 16 24 32 40 48 56", "-8 0 8 16 24 32 40 48 56 64", "-8 0 8 16 24 32 40 48 56 64 72", "-7 1 9 17 25 33 41 49 57 65", " None of these", "-8 0 8 16 24 32 40 48 56")



'Counting Down by 1 and by multiples'


'From Positive to 0 by 1s'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(5, -1, -1):\n    print(i, end=' ')\n", "5 4 3 2 1 0", "4 3 2 1 0", "5 4 3 2 1", "4 3 2 1", " None of these", "5 4 3 2 1 0")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(10, -1, -1):\n    print(i, end=' ')\n", "10 9 8 7 6 5 4 3 2 1 0", "9 8 7 6 5 4 3 2 1 0", "10 9 8 7 6 5 4 3 2 1", "9 8 7 6 5 4 3 2 1", " None of these", "10 9 8 7 6 5 4 3 2 1 0")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(15, -1, -1):\n    print(i, end=' ')\n", "15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0", "14 13 12 11 10 9 8 7 6 5 4 3 2 1 0", "15 14 13 12 11 10 9 8 7 6 5 4 3 2 1", "14 13 12 11 10 9 8 7 6 5 4 3 2 1", " None of these", "15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(20, -1, -1):\n    print(i, end=' ')\n", "20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0", "19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0", "20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1", "19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1", " None of these", "20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0")

'From Positive to 0 by Multiples'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(10, -1, -2):\n    print(i, end=' ')\n", "10 8 6 4 2 0", "9 7 5 3 1", "10 8 6 4 2", "9 7 5 3", " None of these", "10 8 6 4 2 0")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(20, -1, -4):\n    print(i, end=' ')\n", "20 16 12 8 4 0", "19 15 11 7 3", "20 16 12 8 4", "19 15 11 7", " None of these", "20 16 12 8 4 0")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(30, -1, -5):\n    print(i, end=' ')\n", "30 25 20 15 10 5 0", "29 24 19 14 9 4", "30 25 20 15 10 5", "29 24 19 14 9", " None of these", "30 25 20 15 10 5 0")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(40, -1, -10):\n    print(i, end=' ')\n", "40 30 20 10 0", "39 29 19 9", "40 30 20 10", "39 29 19", " None of these", "40 30 20 10 0")

'From Positive to Positive by 1s'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(10, 0, -1):\n    print(i, end=' ')\n", "10 9 8 7 6 5 4 3 2 1", "9 8 7 6 5 4 3 2 1", "10 9 8 7 6 5 4 3 2", "9 8 7 6 5 4 3 2", " None of these", "10 9 8 7 6 5 4 3 2 1")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(20, 10, -1):\n    print(i, end=' ')\n", "20 19 18 17 16 15 14 13 12 11", "19 18 17 16 15 14 13 12 11", "20 19 18 17 16 15 14 13 12", "19 18 17 16 15 14 13 12", " None of these", "20 19 18 17 16 15 14 13 12 11")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(30, 20, -1):\n    print(i, end=' ')\n", "30 29 28 27 26 25 24 23 22 21", "29 28 27 26 25 24 23 22 21", "30 29 28 27 26 25 24 23 22", "29 28 27 26 25 24 23 22", " None of these", "30 29 28 27 26 25 24 23 22 21")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(40, 30, -1):\n    print(i, end=' ')\n", "40 39 38 37 36 35 34 33 32 31", "39 38 37 36 35 34 33 32 31", "40 39 38 37 36 35 34 33 32", "39 38 37 36 35 34 33 32", " None of these", "40 39 38 37 36 35 34 33 32 31")

'From Positive to Positive by Multiples'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(10, 0, -2):\n    print(i, end=' ')\n", "10 8 6 4 2", "10 8 6 4 2 0", "10 8 6 4 2 0 -2", "10 8 6 4 2 -2", " None of these", "10 8 6 4 2")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(20, 14, -2):\n    print(i, end=' ')\n", "20 18 16", "19 17 15", "20 18 16 14", "19 17 15 13", " None of these", "20 18 16")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(30, 11, -3):\n    print(i, end=' ')\n", "30 27 24 21 18 15 12", "29 26 23 20 17 14 11", "30 27 24 21 18 15 12 9", "29 26 23 20 17 14 11 8", " None of these", "30 27 24 21 18 15 12")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(40, 26, -4):\n    print(i, end=' ')\n", "40 36 32 28", "39 35 31 27", "40 36 32 28 24", "39 35 31 27 23", " None of these", "40 36 32 28")

'From 0 to Negative by 1s'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(0, -6, -1):\n    print(i, end=' ')\n", "0 -1 -2 -3 -4 -5", "0 -1 -2 -3 -4", "0 -1 -2 -3", "0 -1 -2", " None of these", "0 -1 -2 -3 -4 -5")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(0, -11, -1):\n    print(i, end=' ')\n", "0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10", "0 -1 -2 -3 -4 -5 -6 -7 -8 -9", "0 -1 -2 -3 -4 -5 -6 -7 -8", "0 -1 -2 -3 -4 -5 -6 -7", " None of these", "0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(0, -16, -1):\n    print(i, end=' ')\n", "0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15", "0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14", "0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13", "0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12", " None of these", "0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(0, -21, -1):\n    print(i, end=' ')\n", "0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15 -16 -17 -18 -19 -20", "0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15 -16 -17 -18 -19", "0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15 -16 -17 -18 -19 -20", "0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15 -16 -17 -18 -19", " None of these", "0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15 -16 -17 -18 -19 -20")

'From 0 to Negative by Multiples'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(0, -11, -2):\n    print(i, end=' ')\n", "0 -2 -4 -6 -8 -10", "0 -2 -4 -6 -8", "0 -2 -4 -6", "0 -2 -4", " None of these", "0 -2 -4 -6 -8 -10")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(0, -16, -3):\n    print(i, end=' ')\n", "0 -3 -6 -9 -12 -15", "0 -3 -6 -9 -12", "0 -3 -6 -9", "0 -3 -6", " None of these", "0 -3 -6 -9 -12 -15")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(0, -21, -4):\n    print(i, end=' ')\n", "0 -4 -8 -12 -16 -20", "0 -4 -8 -12 -16", "0 -4 -8 -12", "0 -4 -8", " None of these", "0 -4 -8 -12 -16 -20")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(0, -26, -5):\n    print(i, end=' ')\n", "0 -5 -10 -15 -20 -25", "0 -5 -10 -15 -20", "0 -5 -10 -15", "0 -5 -10", " None of these", "0 -5 -10 -15 -20 -25")

'From Positive to Negative by 1s'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(5, -6, -1):\n    print(i, end=' ')\n", "5 4 3 2 1 0 -1 -2 -3 -4 -5", "4 3 2 1 0 -1 -2 -3 -4 -5", "5 4 3 2 1 0 -1 -2 -3 -4", "4 3 2 1 0 -1 -2 -3 -4", " None of these", "5 4 3 2 1 0 -1 -2 -3 -4 -5")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(10, -7, -1):\n    print(i, end=' ')\n", "10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6", "9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6", "10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5", "9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5", " None of these", "10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(15, -11, -1):\n    print(i, end=' ')\n", "15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10", "14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10", "15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9", "14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9", " None of these", "15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(20, -4, -1):\n    print(i, end=' ')\n", "20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3", "19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3", "20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 -1 -2", "19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 -1 -2", " None of these", "20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3")


'From Positive to Negative by Multiples'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(10, -11, -2):\n    print(i, end=' ')\n", "10 8 6 4 2 0 -2 -4 -6 -8 -10", "9 7 5 3 1 -1 -3 -5 -7 -9", "10 8 6 4 2 0 -2 -4 -6 -8", "9 7 5 3 1 -1 -3 -5 -7 -9 -11", " None of these", "10 8 6 4 2 0 -2 -4 -6 -8 -10")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(20, -21, -3):\n    print(i, end=' ')\n", "20 17 14 11 8 5 2 -1 -4 -7 -10 -13 -16 -19", "19 16 13 10 7 4 1 -2 -5 -8 -11 -14 -17 -20", "20 17 14 11 8 5 2 -1 -4 -7 -10 -13 -16 -19 -22", "19 16 13 10 7 4 1 -2 -5 -8 -11 -14 -17 -20 -23", " None of these", "20 17 14 11 8 5 2 -1 -4 -7 -10 -13 -16 -19")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(15, -16, -4):\n    print(i, end=' ')\n", "15 11 7 3 -1 -5 -9 -13", "14 10 6 2 -2 -6 -10 -14", "15 11 7 3 -1 -5 -9 -13 -17", "14 10 6 2 -2 -6 -10 -14 -18", " None of these", "15 11 7 3 -1 -5 -9 -13")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(25, -26, -5):\n    print(i, end=' ')\n", "25 20 15 10 5 0 -5 -10 -15 -20 -25", "20 15 10 5 0 -5 -10 -15 -20 -25", "25 20 15 10 5 0 -5 -10 -15 -20", "20 15 10 5 0 -5 -10 -15 -20 -25 -30", " None of these", "25 20 15 10 5 0 -5 -10 -15 -20 -25")

'From Negative to Negative 1s'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-5, -10, -1):\n    print(i, end=' ')\n", "-5 -6 -7 -8 -9", "-6 -7 -8 -9 -10", "-5 -6 -7 -8 -9 -10", "-6 -7 -8 -9", " None of these", "-5 -6 -7 -8 -9")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-10, -15, -1):\n    print(i, end=' ')\n", "-10 -11 -12 -13 -14", "-11 -12 -13 -14 -15", "-10 -11 -12 -13 -14 -15", "-11 -12 -13 -14", " None of these", "-10 -11 -12 -13 -14")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-15, -20, -1):\n    print(i, end=' ')\n", "-15 -16 -17 -18 -19", "-16 -17 -18 -19 -20", "-15 -16 -17 -18 -19 -20", "-16 -17 -18 -19", " None of these", "-15 -16 -17 -18 -19")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-20, -25, -1):\n    print(i, end=' ')\n", "-20 -21 -22 -23 -24", "-21 -22 -23 -24 -25", "-20 -21 -22 -23 -24 -25", "-21 -22 -23 -24", " None of these", "-20 -21 -22 -23 -24")

'From Negative to Negative Mutliples'
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-10, -21, -2):\n    print(i, end=' ')\n", "-10 -12 -14 -16 -18 -20", "-11 -13 -15 -17 -19 -21", "-10 -12 -14 -16 -18 -20 -22", "-11 -13 -15 -17 -19", " None of these", "-10 -12 -14 -16 -18 -20")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-20, -31, -3):\n    print(i, end=' ')\n", "-20 -23 -26 -29", "-21 -24 -27 -30", "-20 -23 -26 -29 -32", "-21 -24 -27", " None of these", "-20 -23 -26 -29")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-30, -41, -4):\n    print(i, end=' ')\n", "-30 -34 -38", "-31 -35 -39", "-30 -34 -38 -42", "-31 -35 -39 -43", " None of these", "-30 -34 -38")
MCQ("What will be the output of the following Python code snippet?\n\nfor i in range(-40, -51, -5):\n    print(i, end=' ')\n", "-40 -45 -50", "-41 -46 -51", "-40 -45 -50 -55", "-41 -46 -51 -56", " None of these", "-40 -45 -50")

'> Off by 1 Errors'

'The For Each Loop'
MCQ("What will be the output of the following Python code snippet?\n\nnumbers = [1, 2, 3, 4, 5]\nfor num in numbers:\n    print(num, end=' ')\n", "1 2 3 4 5", "2 3 4 5 6", "0 1 2 3 4", "1 2 3 4", " None of these", "1 2 3 4 5")
MCQ("What does the following Python code snippet do?\n\nfruits = ['apple', 'banana', 'cherry', 'date']\nfor fruit in fruits:\n    print(fruit)\n", "Prints each element of the list 'fruits' on a separate line", "Prints the length of each fruit in the list 'fruits'", "Prints the list 'fruits'", "Prints the elements of the list 'fruits' separated by spaces", " None of these", "Prints each element of the list 'fruits' on a separate line")
MCQ("What will be the output of the following Python code snippet?\n\nlanguages = ['Python', 'Java', 'C++', 'JavaScript']\nfor lang in languages:\n    print(lang, end=', ')\n", "Python, Java, C++, JavaScript, ", "PythonJavaC++JavaScript", "Python Java C++ JavaScript", "Python, Java, C++, JavaScript", " None of these", "Python, Java, C++, JavaScript, ")
MCQ("What will be the output of the following Python code snippet?\n\nsentence = 'Hello, world!'\nfor char in sentence:\n    print(char, end='')\n", "Hello, world!", "H e l l o , w o r l d !", "Helloworld!", "Hello,world!", " None of these", "Hello, world!")

'> Throw away variable _ '
MCQ("What does the following Python code snippet do?\n\npython\nfor _ in range(5):\n    print('Hello')\n", "Prints 'Hello' five times", "Prints the numbers from 1 to 5", "Prints nothing", "Throws an error", " None of these", "Prints 'Hello' five times")
MCQ("What will be the output of the following Python code snippet?\n\npython\nfor _ in range(3):\n    print(_, end=' ')\n", "0 1 2", "1 2 3", "2 3 4", "3 4 5", " None of these", "0 1 2")
