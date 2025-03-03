import json
import os
from pathlib import Path 
import time

from questions import *

path = Path(__file__).parent / "json-files" / f"{setname}.json"

def create():
    if not os.path.exists(Path(__file__).parent / "json-files"):
        os.mkdir(Path(__file__).parent / "json-files")
        
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write("{}")


def write(data):
    fdata = read()

    for k,val in data.items():
        if k not in fdata.keys():
            fdata[k] = val


    with open(path, "w") as file:
        json.dump(fdata, file,indent=4)    


def read():
    with open(path, "r") as file:
        data = json.load(file)
    
    return data


if __name__ ==  "__main__":
    create() 

    data = {}
    for question, options in questions.items():
        data[question.lstrip("\n")] = options
        
    
    write(data)
    print(f"JSON file successfully created:\n{path}")