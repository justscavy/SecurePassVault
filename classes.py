class User:
    """Class for current session informations"""
    def __init__(self,website: str,name: str ,password: str ="",hashed: str=...) -> None:
        self.website = website
        self.name = name
        self.password = password
        self.hashed = hashed
        

    def password_maker(self,password=str, hashed=str): ###andre was mache ich hier
        self.password = password
        self.hashed = hashed
        



#class Passwordmanager:
#    def __init__(self) -> None:
#        pass