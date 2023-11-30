import sys
import string
import random

from cryptography.fernet import Fernet

from classes import PWManagerEntry
from pw_file_manager import PWFileManager


class PWManager:
    """Allows password management."""
    def __init__(self, crypter: Fernet) -> None:
        self.crypter: Fernet = crypter
        #composition like ArjanCodes
        self.pw_file_manager: PWFileManager = PWFileManager()
        self.pw_manager_entries: list[PWManagerEntry] = []

    def main_menu(self):
        """main_menu 1.create password or 2.view password"""
        while True:
            try:
                select = int(input("\nSelect:\n1.Create password:\n2.View password entries\n3.Exit\n>> "))
                if select == 1:
                    #Create entry with user_name & website
                    pw_manager_entry = self.create_pw_manager_entry()
                    #Generate password
                    password, encrypted_pw = self.generate_password(crypter=self.crypter)
                    #TODO: works but thats it...
                    pw_manager_entry.password = password
                    pw_manager_entry.encrypted_pw = encrypted_pw
                    #Store password entry
                    self.pw_file_manager.store(pw_manager_entry=pw_manager_entry) 
                    print(f"\n\n\n\nPassword successfully created!")            
                    print(f"Website: {pw_manager_entry.website}")
                    print(f"Username: {pw_manager_entry.name}")
                elif select == 2:
                    self.pw_file_manager.view(crypter=self.crypter)
                elif select == 3:
                    sys.exit()
                else:
                    raise ValueError("\nInvalid Input.")
            except ValueError as e:
                print(e)

    def create_pw_manager_entry(self):
        """gathering user_info WEBSITE & USERNAME"""
        while True:
            try:
                website = input("What Website u looking to setup a Password for? ").casefold()
                while not website:
                    website = input("You have to specifie a Website:").casefold()
                name = input("Whats the Username u'r using? ").casefold()
                while not name:
                    name = input("You need to insert a Username: ").casefold()
                pw_manager_entry = PWManagerEntry(website, name)
                return pw_manager_entry     
            except ValueError as ve:          
                print(f"Error: {ve}")
                

    def generate_password(self, crypter: Fernet):
        """generator logic"""
        while True:
            try:
                password_method = int(input("\nChose ur password type:\n1.Only letters:\n2.Letters and numbers: \n3.Letters, numbers and Special Characters:\n4.Exit\n>> "))

                if password_method == 1:
                    possible_pw_characters = string.ascii_letters
                    break
                elif password_method == 2:
                    possible_pw_characters = string.ascii_letters + string.digits
                    break
                elif password_method == 3:
                    possible_pw_characters = string.ascii_letters + string.digits + string.punctuation
                    break
                elif password_method == 4:
                    sys.exit()
                else:
                    raise ValueError("\nInvalid Input.")
            except ValueError as ve:
                print(ve)

        while True:
            try:
                password_len = int(input("\nLength of password? (4 characters atleast!)\n>> "))
                #checking for type and min len
                if not isinstance(password_len, int) or password_len < 4:      
                    raise ValueError("\nInvalid Input. Password is not long enough!")
                else:
                    break
            except ValueError as ve:
                print(ve)
        #choose random characters depending on type & len choosen
        password: str = "".join(random.choice(possible_pw_characters) for _ in range(password_len))
        #encrypt the random given characters and handle utf-8 special character issues with .decode()
        encrypted_pw: bytes = crypter.encrypt(password.encode())
        return password, encrypted_pw.decode()
