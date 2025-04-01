import os
import sys
from pathlib import Path

suppress = False


def gen_key(length):
    return os.urandom(length)

def xor_crypt(data,key):
    return bytes(a ^ b for a,b in zip(data,key))

def enxor(file_in, file_out, key_file):
    with open(file_in, "rb") as file:
        data = file.read()

    key = gen_key(len(data))

    with open(key_file, "wb") as file:
        file.write(key)

    encrypted_data = xor_crypt(data, key)

    with open(file_out, "wb") as file:
        file.write(encrypted_data)

    if not suppress:
        print(f"File encrypted and saved to {file_out}")
        print(f"Key saved to {key_file}")



root = Path(__file__).parent
q_sets = root / "ciphers"
q_sets_plain = root / "json-files"


def main():
    if not os.path.exists(q_sets):
        os.mkdir(q_sets)
        
    for file in q_sets.iterdir():
        if file.is_file():
            file.unlink()


    for file in q_sets_plain.iterdir():
        if file.is_file():
            name = file.parts[-1].replace(".json","")
            enxor(file,q_sets/f"{name}",q_sets/f"{name}.key")



