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
        self.noextension = self.parent / self.path.stem
        self.xor = Xor(path,self.noextension, str(self.noextension) + ".key")


    def read(self):
        '''TODO:
            decrypt file
            read data
            delete plain file
            return data
        '''
        self.xor.dexor()    
        jsondata = super().read()
        self.path.unlink()
        return jsondata
        
    def write(self,data):
        '''TODO:
            decrypt file
            read data
            write data
            write file
            encrypt file
            delete plain
        '''
        self.xor.dexor()
        jsondata = super().read()

        for key,val in data.items():
            jsondata[key] = val
        
        super().write(jsondata)

        self.xor.enxor()
        self.path.unlink()
        
        

class Xor():
    def __init__(self, plainpath, cipherpath, keypath):
        self.parent = plainpath.parent
        self.plainpath = plainpath
        self.cipherpath = cipherpath
        self.keypath = keypath
        
    def gen_key(self, length):
        return os.urandom(length)

    def xor(self, data, key):
        return bytes(a ^ b for a,b in zip(data,key))

    def enxor(self):
        with open(self.plainpath,"rb") as file:
            data = file.read()

        key = self.gen_key(len(data))
        with open(self.keypath, "wb") as file:
            file.write(key)

        cipher_data = self.xor(data,key)
        with open(self.cipherpath, "wb") as file:
            file.write(cipher_data)

    def dexor(self):
        with open(self.cipherpath,"rb") as file:
            data = file.read()

        with open(self.keypath, "rb") as file:
            key = file.read()

        plain = self.xor(data,key)
        with open(self.plainpath, "wb") as file:
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

