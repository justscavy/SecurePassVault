from classes import User

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
            
            except Exception as e:
                 print(f"Error: {e}")