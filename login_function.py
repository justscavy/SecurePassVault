import sys
from pathlib import Path

from cryptography.fernet import Fernet

from key_manager import generate_key
from getpass import getpass


def login(crypter: Fernet, key_file: Path) -> bool:
    """Login with key"""
    while True:
        #hide user input with getpass
        password = getpass("Enter your Masterpassword to login or press 3 to exit:\n")
        if password == "3":
            sys.exit()
        try:
            with open(key_file, "rb") as f:
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
                    return False
        except Exception as e:
            print(f"Login failed: {e}")
            return False