class User:
    """"""

    def __init__(self, website: str, name: str, password: str = "", encrypted_pw: str = "") -> None:
        self.website = website
        self.name = name
        self.password = password
        self.encrypted_pw = encrypted_pw

    def password_maker(self, password: str, encrypted_pw: str): ###andre was mache ich hier
        self.password = password
        self.encrypted_pw = encrypted_pw
