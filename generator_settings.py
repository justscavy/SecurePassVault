import string
import random
import sys

from typing import Tuple
from cryptography.fernet import Fernet


def password_generator(crypter: Fernet) -> [str, bytes]:
    """password_generator logic"""
    while True:#set a method which charactes the password should have.
        try:
            password_method = int(input("\nChose ur password type:\n1.Only letters:\n2.Letters and numbers: \n3.Letters, numbers and Special Characters:\n4.Exit\n>> "))
            if password_method == 1:
                pw_unhashed = string.ascii_letters
                break
            elif password_method == 2:
                pw_unhashed = string.ascii_letters + string.digits
                break
            elif password_method == 3:
                pw_unhashed = string.ascii_letters + string.digits + string.punctuation
                break
            elif password_method == 4:
                sys.exit()
            else:
                raise ValueError("\nInvalid Input.")
        except ValueError as e:
            print(e)

    while True:
        try:
            password_len = int(input("\nLength of password? (4 characters atleast!)\n>> "))
            #checking for password type and min len
            if not isinstance(password_len, int) or password_len < 4:      
                raise ValueError("\nInvalid Input. Password is not long enough!")    
            else:
                break
        except ValueError as e:
            print(e)
    #choose random characters depending on type & len choosen
    password: str = "".join(random.choice(pw_unhashed) for _ in range(password_len))    
    #encrypt the given cleartext password.
    encrypted_pw: bytes = crypter.encrypt(password.encode())
    return password, encrypted_pw

