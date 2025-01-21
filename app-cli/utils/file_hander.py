import os
import json
from pathlib import Path
from datetime import datetime


class JSON_Handler():
    
    def __init__(self, path):
        self.path = path
        self.parent = path.parent

    def read(self):
        with open(self.path, "r") as file:
            data = json.load(file)

        return data

    def write(self, data, indent=4):
        with open(self.path, "w") as file:
            json.dump(data, file, indent=indent)


    def create(self):
        if not os.path.exists(self.path):
            self.write({})

    def delete(self):
        if os.path.exists(self.path):
            self.path.unlink()

class Save(JSON_Handler):
    def __init__(self, path):
        super().__init__(path)


    def read(self):
        '''TODO:
            decrypt file
            read data
            delete plain file
            return data
        '''
        pass

    def write(self):
        '''TODO:
            decrypt file
            read data
            write data
            write file
            encrypt file
            delete plain
        '''
        pass

class Xor():
    def __init__(self, path):
        self.path = path
        self.parent = path.parent
        
    def gen_key(self, length):
        return os.urandom(length)

    def xor(self, data, key):
        return bytes(a ^ b for a,b in zip(data,key))

    def enxor(self, inpath, outpath, keypath):
        with open(inpath,"rb") as file:
            data = file.read()

        key = self.gen_key(len(data))
        with open(keypath, "wb") as file:
            file.write(key)

        cipher_data = self.xor(data,key)
        with open(outpath, "wb") as file:
            file.write(cipher_data)

    def dexor(self, inpath, outpath, keypath):
        with open(inpath,"rb") as file:
            data = file.read()

        with open(keypath, "rb") as file:
            key = file.read()

        plain = self.xor(data,key)
        with open(outpath, "wb") as file:
            file.write(plain)









def delete_files(path,extension=None):
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

