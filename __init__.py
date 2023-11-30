import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from pathlib import Path
from cryptography.hazmat.backends import default_backend


key_file = Path("key.key") #poc Should be stores in registry or somewhere

"""
def key_manager():
    #if key exists use it, else create it!
    if key_file.is_file():
        with open(file=key_file, mode='rb') as f:
            key = f.read()
    else:
        key = Fernet.generate_key()         #generate key based on masterpassword
        with open(key_file, 'wb') as f:
            f.write(key)
    return Fernet(key)
"""
def key_manager():
    """if key exists use it, else create it!"""
    
    if key_file.is_file():
        with open(file=key_file, mode='rb') as f:
            key = f.read()
    else:
        print("It seems like this is ur first time.")        
        password = input("Set a Masterpassword:\n").encode('utf-8')
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
)
        key = base64.urlsafe_b64encode(kdf.derive(password))
        print(f"Ur Master Password is: {password}")
        print(f"sadly u need this key to login: {key}")
        print(f"dont lose it...")
    with open(key_file, 'wb') as f:
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
            
        

    