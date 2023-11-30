import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from pathlib import Path
from cryptography.hazmat.backends import default_backend


#key should be stores in registry or somewhere
key_directory = Path(__file__).parent
key_file = key_directory / "key.key"


def key_manager():
    """If key exist use it else, create it"""
    #if key exists use it, else create it!
    if key_file.is_file():
        with open(file=key_file, mode='rb') as f:
            key = f.read()
    else:
        key = Fernet.generate_key()               #TODO: new key_manager with given user password 
        with open(key_file, 'wb') as f:           #into key encryption is ready but login doesnt wortk check teststuff.py  
            f.write(key)
    return Fernet(key)


########WORK IN PROGRESS#########
def login(crypter):
    """Login with key"""
    with open(file=key_file, mode='rb') as f:
        stored_key: bytes = f.read()
        #decode the key to make it comparable to key_input 
        stored_key_str: str = stored_key.decode()

    while True:
        key_input: str = input("Enter your key: ")
        #compare user_input & key.key file
        if key_input == stored_key_str:
            print(f"\nLogin successfull!\n")
            return True
        else:
            print("Wrong key")


###




            
        

    