import json

question = '''
What will be the output of the following Python code snippet?

class Example():
    def __init__(self):
        self.name = "name"

    def method(self):
        print(self.name)
'''

answer = "HelloWorld"
options = [
    "Hello World",
    "Hello + World",
    "Error",
    "None of these"
]

options.insert(0,answer)

question = repr(question.lstrip("\n"))

if question.startswith('"') and question.endswith('"'):
    question = question[1:-1]
if question.startswith("'") and question.endswith("'"):
    question = question[1:-1]


data = {
    question : options
}

with open("temp.json", "w") as file:
    json.dump(data,file,indent=4)


with open("temp.json", "r") as file:
    data = json.load(file)

print(data)

for key,val in data.items():
    print(key.encode('utf-8').decode('unicode_escape'))
    for v in val:
        print(v)







