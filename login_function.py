import sys

from getpass import getpass

from key_manager import generate_key




key_file: str = "key.key"


def login(crypter):
    """Login with key"""
    while True:
        #hide user input with getpass
        password = getpass("Enter your Masterpassword to login or press 3 to exit:\n")
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