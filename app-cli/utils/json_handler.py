import json
import sys
import os
from pathlib import Path



class Json_Handler():

    def __init__(self, path):
        self.path = path
        self.folder = path.parent
        self.create()

    def read(self):
        with open(self.path, "r") as file:
            data = json.load(file)
        return data


    def write(self,data,indent=4):
        with open(self.path, "w") as file:
            json.dump(data,file,indent=indent)

    def create(self):
        if not os.path.exists(self.path):
            print("SAVE FILE NOT FOUND, CREATING SAVE FILE.")
            self.write({})


class Report(Json_Handler):
    def __init__(self, path):
        super().__init__(path)

    
    def update(self, data):
        ''' data = (Chapter, Section, Score, Percent, Passed?)'''

        try:
            report = self.read(self.path)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            report = {"progress":{}}
            

        try:
            progress = report["progress"]
        except KeyError as e:
            report["progress"] = {}
            progress = report["progress"]


        if data[0] not in progress:
            progress[data[0]] = {
                data[1] : ("N/a","N/a","\u274C Not Yet Passed")
            }

        write_json(self.path, report)
        write_report()

    def display(self):
        pass

    def clear(self):
        pass

class Save(Json_Handler):
    def __init__(self, path):
        super().__init__(path)

    def save(self, data):

        try:
            save_data = self.read()
        except FileNotFoundError as e:
            self.write({})
            save_data = {}
        except json.decoder.JSONDecodeError as e:
            save_data = {}


        for key in data.keys():
            save_data[key] = data[key]

        
        self.write(save_data)
        
    def load(self):
        try:
            save_data = self.read()
        except FileNotFoundError as e:
            self.write({})
            save_data = {}
        except json.decoder.JSONDecodeError as e:
            save_data = {}


        return save_data  

             


if __name__ == "__main__":

    data = {
        "Chapter 1" :[
            "1",
            "2",
            "3"
        ],
        "Chapter 2" :[
            "1",
            "2",
            "3"
        ]
            
        
    }

    report = Json_Handler(Path(__file__).parent/"test.json")
    report.write(data)
   