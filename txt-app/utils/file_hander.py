import os
import json

def write_json():
    pass

def read_json():
    pass



def delete_fromdir(path,extension=None):
    for file in path.iterdir():
        if file.is_file():
            if extension is None:
                file.unlink()
            if extension in str(file):
                file.unlink()

            

