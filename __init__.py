from cryptography.fernet import Fernet

from pathlib import Path



key_file = Path("key.key") #poc SHOULD BE STORED IN A DB hashed

def key_manager():
    """if key exists use it, else create it!"""
    if key_file.is_file():
        with open(file=key_file, mode='rb') as f:
            key = f.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)
    return Fernet(key)
    




def sign_in(crypter):

    with open(file=key_file, mode='rb') as f:
        stored_key: bytes = f.read()
        stored_key_str: str = stored_key.decode()

    while True:
        key_input = input("Enter your key: ")
    

        if key_input == stored_key_str:
            print(f"\nLogin successfull!\n")
            return True
        else:
            print("Wrong key")
            
        

    