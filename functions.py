import os
import sys
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from getpass import getpass



key_file: str = "key.key"


def generate_key(password: str, salt: bytes):
    #use key derivation instead of generate
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=salt,
        iterations=100000,
        length=32,
    )
    key: bytes = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key


def key_manager():
    """If key exists use it else, create it"""
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            key_salted = f.read()
            #split the salted part from the key generation apart
            key, salt = key_salted.split(b';')
    else:
        password = getpass("Its ur first time!\nCreate a Masterpassword:")
        print("i have no idea how to get it back yet...\nso better dont lose it :D")
        print(f"Your Masterpassword: {password}\n")
        #if key exists we use it and seperate the key from the salt again since its added after the password
        salt = os.urandom(16)
        key = generate_key(password, salt)
        #join key + salt back together
        with open(key_file, 'wb') as f:
            f.write(key + b';' + salt)
    return Fernet(key)


def login(crypter):
    """Login with key"""
    while True:
        #hide user input with getpass
        password = getpass("Enter your password to login or press 3 to exit:\n")
        if password == "3":
            sys.exit()
        try:
            with open(key_file, 'rb') as f:
                key_salted = f.read()
                #split key from salt
                stored_key, salt = key_salted.split(b';')
                key_input = generate_key(password, salt)
                #compare unsalted key to user input
                if key_input == stored_key:
                    print("Login successful!\n")
                    return True
                else:
                    print("Wrong password")
        except Exception as e:
            print(f"Login failed: {e}")