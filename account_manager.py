from classes import User
from resultwriter import Datawriter
import sys
from cryptography.fernet import Fernet


def account_management(crypter: Fernet):
     while True:
        try:
            select = int(input("\nSelect:\n1.Create password:\n2.View passwords\n3.Exit\n>> "))
            if select == 1:
                user = create_account()
                return user        
            elif select == 2:
                data_writer = Datawriter()
                data_writer.view_file(crypter=crypter)       
            elif select == 3:
                sys.exit()
            else:
                raise ValueError("\nInvalid Input.")
        except ValueError as e:
            print(e)


def create_account():
        """gathering user_info WEBSITE & USERNAME"""
        while True:
            try:
                website = input("What Website u looking to setup a Password for? ").casefold()
                while not website:
                    website = input("You have to specifie a Website:").casefold()
                name = input("Whats the Username u'r using? ").casefold()
                while not name:
                    name = input("You need to insert a Username: ").casefold()
                user = User(website, name)
                return user
            
            except Exception as e:          #fix
                 print(f"Error: {e}")
