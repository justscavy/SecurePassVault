from cryptography.fernet import Fernet
from pathlib import Path


key_file = Path("key.key") #poc Should be stores in registry or somewhere


def key_manager():
    """if key exists use it, else create it!"""
    if key_file.is_file():
        with open(file=key_file, mode='rb') as f:
            key = f.read()
    else:
        key = Fernet.generate_key()         #generate key based on masterpassword
        with open(key_file, 'wb') as f:
            f.write(key)
    return Fernet(key)
    

def login(crypter):
    """Login with key"""
    with open(file=key_file, mode='rb') as f:
        stored_key: bytes = f.read()
        #decode the key to make it comparable to key_input 
        stored_key_str: str = stored_key.decode()

    while True:
        key_input = input("Enter your key: ")
        #compare input & key
        if key_input == stored_key_str:
            print(f"\nLogin successfull!\n")
            return True
        else:
            print("Wrong key")
            
        

    