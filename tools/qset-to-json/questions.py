'''Place preformmated questions and answers in the dictionary "questions" below.'''

setname = "test"

# {question : [answer, *options]}
questions = {
'''
What is the output of the following Python code snippet?

color = input()

if("green" == color):
    print("GO")
elif("yellow" == color):
    print("CAUTION")
else:
    print("STOP")

''' : ["The output varies depending on user input.","GO","CAUTION","STOP","Error"],
'''
What is the output of the following Python code snippet?

x = 10
y = 5

if x > y:
    print("X is greater")
elif x < y:
    print("Y is greater")
else:
    print("Both are equal")

''' : ["X is greater", "Y is greater", "Both are equal", "Error"],

'''
What is the result of this code?

a = [1, 2, 3]
b = a
b.append(4)

print(a)

''' : ["[1, 2, 3, 4]", "[1, 2, 3]", "Error", "None"],

'''
What is the output of this Python code?

def add(a, b=5):
    return a + b

print(add(3))

''' : ["8", "5", "Error", "3"],

'''
What is the output of the following Python code snippet?

x = "Python"
y = x[::-1]
print(y)

''' : ["nohtyP", "Python", "Error", "None"],

'''
What is the output of this Python code snippet?

x = [1, 2, 3, 4]
print(x[-2])

''' : ["3", "4", "2", "Error"],

'''
What does the following Python code output?

try:
    print(1 / 0)
except ZeroDivisionError:
    print("Error")
finally:
    print("Done")

''' : ["Error\nDone", "Done", "Error", "None"],

'''
What will this code snippet output?

for i in range(3):
    print(i, end=" ")

''' : ["0 1 2 ", "0 1 2", "012", "Error"],

'''
What is the type of the variable `x` in the following Python code?

x = (1, 2, 3)

''' : ["tuple", "list", "dictionary", "set"],

'''
What will the following Python code output?

x = {1, 2, 3, 3}
print(len(x))

''' : ["3", "4", "2", "Error"],

'''
What will this Python code produce?

def greet():
    return "Hello, World!"

print(greet())

''' : ["Hello, World!", "Error", "None", "greet()"], 


}