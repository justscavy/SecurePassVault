import bcrypt
import string
import random
import sys
from cryptography.fernet import Fernet



def password_generator():
    """generator logic"""
    while True:
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

            if not isinstance(password_len, int) or password_len < 4:      #checking for type and min len
                raise ValueError("\nInvalid Input. Password is not long enough!")           #handle errors
            else:
                break
        except ValueError as e:
            print(e)


    password: str = "".join(random.choice(pw_unhashed) for _ in range(password_len))    #choose random characters depending on type & len choosen
    key = Fernet.generate_key()
    crypter = Fernet(key)
    #crypter = generate_key()
    #hashed: bytes = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())          #hashing the password with gensalt=adding a rnd. value to the password.
    hashed = crypter.encrypt(password.encode())
    
    return password, hashed


#def generate_key():
#    key = Fernet.generate_key()
#    with open("key.txt", "wb") as f:
#        f.write(key)
#
#    return key

   



  