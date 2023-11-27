import bcrypt
import string
import random
import sys


def password_generator():
    while True:
        password_method = input("\nChose ur password type:\n1.Only letters:\n2.Letters and numbers: \n3.Letters, numbers and Special Characters:\n4.Exit\n>>")
        
        if password_method == "1":
            pw_unhashed = string.ascii_letters
            break
        elif password_method == "2":
            pw_unhashed = string.ascii_letters + string.digits
            break
        elif password_method == "3":
            pw_unhashed = string.ascii_letters + string.digits + string.punctuation
            break
        elif password_method == "4":
            sys.exit()
        else:
            print("Invalid Input")
            continue


    password_len: int = int(input(f"\nLength of password?\n>>"))
            
    
    password: str = "".join(random.choice(pw_unhashed) for _ in range(password_len))
    hashed: bytes = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return password, hashed
    
   



  