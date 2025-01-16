import os
import json
from pathlib import Path
from datetime import datetime

def write_json(path, data):
    with open(path, "w") as file:
        json.dump(data,file,indent=4)

def read_json(path):
    with open(path, "r") as file:
        data = json.load(file)

    return data

def delete_fromdir(path,extension=None):
    for file in path.iterdir():
        if file.is_file():
            if extension is None:
                file.unlink()
            if extension in str(file):
                file.unlink()
          
def log(info):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    path = Path(__file__).parent.parent / "logs"

    if(not os.path.exists(path)):
        os.mkdir(path)

    with open(path / ".log", "ab") as file:
        file.write(bytes(f"{time} : {info}\n".encode("utf-8")))

if __name__ == "__main__":
    log("testing log")