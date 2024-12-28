'''Python Operators'''

concatenation_and_duplication = [

["What is the primary function of the '+' operator when used with strings in Python?","Combine strings","Duplicate strings","Divide strings","Subtract strings","Perform modulo operation"],
["What does the '*' operator do when applied to strings in Python?","Duplicate the string","Concatenate the string",
"Divide the string","Subtract one string from another","Find the remainder of division"],
["Literals in python are?"," actual values"," variables"," statements"," functions"," operators"],
[
"""What output will be printed by the following code snippet?

a = 'Hello'
b = 'World'

print(a + b)""","HelloWorld","Hello World","Hello + World","Error","None of these"
],

["What does the expression 'a' * 3 evaluate to in Python?","'aaa'","'aaa...'", "'a3'", "Error", "None of these"],

]



casting = [

["What does the 'str()' function do in Python?","Converts to string","Converts to integer","Converts to floating-point number","Returns the data type","None of these"],
["Which function is used to convert a number or string to an integer in Python?","int()","str()","float()","type()","None of these"],
["What does the 'float(),' function do in Python?","Converts to floating-point number","Converts to string","Converts to integer","Returns the data type","None of these"],
["What is the purpose of the 'type(),' function in Python?","Returns the data type","Converts to string","Converts to integer","Converts to floating-point number","None of these"],
["What is the general order of operations for arithmetic, relational, and logical operators in Python?","Arithmetic -> Relational -> Logical",
"Relational -> Arithmetic -> Logical","Logical -> Relational -> Arithmetic","Arithmetic -> Logical -> Relational","Relational -> Logical -> Arithmetic"],

]



arithmetic_operators = [

["What does the '*' operator represent in Python?","Multiplication","Division","Modulo","Exponentiation","None of these"],
["Which operator is used for floor division (integer division) in Python?","//","%","+","**","None of these"],
["What is the result of the expression 5 + 2 in Python?","7","3","10","2.5","None of these"],
["What operation does the '/' operator perform in Python?","Division","Multiplication","Subtraction","Exponentiation","None of these"],
["What is the outcome of the expression 5 % 2 in Python?","1","3","10","2.5","None of these"],

]



comparison_operators = [

["What does the '>' operator signify in Python?","Greater than","Less than","Greater than or equal to","Less than or equal to","Equal to"],
[
'''What is the output of the expression 'x >= z' in Python?

x = 50; y = 45; z = 45

x >= z''',"True","False","Error","None of these","None"
],
[
'''What is the result of the expression x > y in Python?

x = 50; y = 45; z = 45

x > y''',"True","False","Error","None","None of these"
],
["What does the '>=' operator indicate in Python?","Greater than or equal to","Less than","Greater than","Less than or equal to","Equal to"],

[
"""What will be the output of the expression y != x in Python?

x = 50; y = 45; z = 45

y != x""","True","False","Error","None","None of these"
],
["What does the '<' operator signify in Python?","Less than","Greater than","Greater than or equal to","Less than or equal to","Equal to"],

[
"""What is the outcome of the expression 'x <= z' in Python?

x = 50; y = 45; z = 45

x <= z""","False","True","Error","None","None of these"
],
["What does the '<=' operator represent in Python?","Less than or equal to","Greater than","Less than","Greater than or equal to","Equal to"],
["Which Python operator checks if a value is greater than another?",">",">=", "<=", "==", "None of these"],
["Which Python operator checks if a value is less than another?","<",">=", ">=", "==", "None of these"],
["Which Python operator checks if a value is greater than or equal to another?",">=", "<", "<=", "==", "None of these"],
["Which Python operator checks if a value is less than or equal to another?","<=", ">", ">=", "==", "None of these"],

]





membership = [
["What does the 'in' operator do in Python?","Checks if an element is a part of a collection","Checks if two variables are identical",
"Checks if an element is not part of a collection","Checks if two variables are not identical","None of these"],
["What does the 'not in' operator do in Python?","Checks if an element is not part of a collection","Checks if an element is a part of a collection",
"Checks if two variables are not identical","Checks if two variables are identical","None of these"],
["Which Python operator checks if an element is part of a collection?","in","not in","is","is not","None of these"],
["Which Python operator checks if an element is not part of a collection?","not in","in","is","is not","None of these"],

]



identity = [

["""What will be the result of the expression 'y is z' in Python?

x = 50; y = 45; z = 45

y is z""","True","False","Error","None of these","None"
],
["What is the purpose of the 'is not' operator in Python?","Not identical to","Identical to","Greater than or equal to","Less than or equal to","Equal to"],
["Which operator is used to check if two variables are identical in Python?","is","==","!=","is not","None of these"],

[
"""What will be printed by the expression print( y is z ), in Python?

x = 50; y = 45; z = 45

print( y is z )""","True","False","Error","None","None of these"
],

["Which Python operator checks if two values are identical?","is", "is not", "in", "not in", "None of these"],
["Which Python operator checks if two values are not identical?","is not", "is", "in", "not in", "None of these"],

]




assignment_vs_equality = [
[
"""What is the result of the expression 'x == z' in Python?

x = 50; y = 45; z = 45

x == z""","False","True","Error","None","None of these"
],
[
"""What will be the output of the expression print( y != z ) in Python?

x = 50; y = 45; z = 45

print( y != z )""","False","True","Error","None","None of these"
],

["Which Python operator checks if two values are equal?","==", "!=", ">=", "<=", "None of these"],
["Which Python operator checks if two values are not equal?","!=", "==", ">=", "<=", "None of these"],
["Which of the following is the '!=' operator in Python?","Not equal to","Equal to","Greater than or equal to","Less than or equal to","Greater than"],
["What does the '=' operator signify in Python?","Assignment","Equality","Comparison","Increment","None of these"],
["What is the purpose of the '==' operator in Python?","Equality (Comparison)","Assignment","Increment","Decrement","None of these"],
["Which statement correctly describes the usage of the '=' operator in Python?","The equal sign must always be on the left side of the operation",
"The equal sign must always be on the right side of the operation","The equal sign can be placed on either side of the operation",
"The equal sign is not necessary in Python","None of these"],
["In Python, what does the expression 'a == 1' evaluate to if 'a' stores the value 1?","True","False","Error","None","None of these"],
["What is the difference between '=' and '==' operators in Python?","'=' is used for assignment, while '==' is used for comparison",
"'=' is used for comparison, while '==' is used for assignment","Both operators perform the same task","There is no difference between '=' and '==' in Python","None of these"],

]





compound = [
["Which operator is used for adding and assigning in Python?","+=","-=","*=","/=","None of these"],
["Which operator is used for multiplying and assigning in Python?","*=","+=","-=","/=","None of these"],
["Which operator is used for dividing and assigning in Python?","/=","+=","-=","*=","None of these"],
["Which operator is used for floor dividing and assigning in Python?","//=","%=","**=","*=","None of these"],
["Which operator is used for modulo (remainder) and assigning in Python?","%=","//=","**=","*=","None of these"],
["Which operator is used for exponentiation (power) and assigning in Python?","**=","+=","-=","*=","None of these"],
["Which operator is used for subtracting and assigning in Python?","-=","+=","*=","/=","None of these"],
["What does the '+= ' operator represent in Python?","Add and assign","Subtract and assign","Multiply and assign","Divide and assign","None of these"],
["What does the '-=' operator represent in Python?","Subtract and assign","Add and assign","Multiply and assign","Divide and assign","None of these"],
["What does the '*=' operator represent in Python?","Multiply and assign","Add and assign","Subtract and assign","Divide and assign","None of these"],
["What does the '/=' operator represent in Python?","Divide and assign","Add and assign","Subtract and assign","Multiply and assign","None of these"],
["What does the '//=' operator represent in Python?","Floor divide and assign","Modulo and assign","Exponentiation (power) and assign","Multiply and assign","None of these"],
["What does the '**=' operator represent in Python?","Exponentiation (power), and assign","Add and assign","Subtract and assign","Multiply and assign","None of these"],
["What is the equivalent shorthand operator for 'x = x + 1' in Python?","x+=1","x-=1","x*=1","x/=1","None of these"],
["Which shorthand operator corresponds to 'x = x - 1' in Python?","x-=1","x+=1","x*=1","x/=1","None of these"],
["What shorthand operator is equivalent to 'x = x * 1' in Python?","x*=1","x+=1","x-=1","x/=1","None of these"],
["Which shorthand operator represents 'x = x / 1' in Python?","x/=1","x+=1","x-=1","x*=1","None of these"],
["What shorthand operator is the equivalent of 'x = x // 1' in Python?","x//=1","x%=1","x**=1","x+=1","None of these"],
["Which shorthand operator is the same as 'x = x % 1' in Python?","x%=1","x//=1","x**=1","x+=1","None of these"],
["What is the shorthand operator corresponding to 'x = x ** 1' in Python?","x**=1","x+=1","x-=1","x*=1","None of these"]

]


logical = []


de_morgan = [
["According to De Morgan's Laws, what is the equivalent expression for 'not(a and b)' ?",
"(not a or not b)","(not a and not b)","(not a and b)","(a or b)","(a and b)","(not a or not b)"],
["According to De Morgan's Laws, what is the equivalent expression for 'not(a or b)'?",
"(not a and not b)","(not a or not b)","(not a and b)","(a or b)","(a and b)","(not a and not b)"],
[
"""The variables a and b have both been properly declared and initialized, what is the result of the following expression:

( not(a and b) == (not a or not b) )""","True", "False", "None", "Error", "None of these"
],
[
"""The variables a and b have both been properly declared and initialized, what is the result of the following expression:

( not(a or b)  == (not a and not b) )""","True", "False", "None", "Error", "None of these"
],
[
"""The variables a and b have both been properly declared and initialized, what is the result of the following expression:

( not(a and b) == (not a and not b) )""","False","True", "None", "Error", "None of these"
],
[
"""The variables a and b have both been properly declared and initialized, what is the result of the following expression:

( not(a or b)  == (not a or not b) )""","False","True","None", "Error", "None of these"
],

]


built_ins = []
bitwise = []



basic = concatenation_and_duplication + casting + arithmetic_operators + comparison_operators + membership + identity + assignment_vs_equality + compound + logical


advanced = de_morgan + built_ins + bitwise