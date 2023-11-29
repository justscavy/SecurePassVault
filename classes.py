from dataclasses import dataclass


@dataclass
class PWManagerEntry:
    """Represents an entry for the password manager."""
    website: str
    name: str
    password: str = ""
    encrypted_pw: str = ""

    def password_maker(self, password: str, encrypted_pw: str): ###andre was mache ich hier
        self.password = password
        self.encrypted_pw = encrypted_pw
