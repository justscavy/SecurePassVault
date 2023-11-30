from dataclasses import dataclass


@dataclass
class PWManagerEntry:
    """Represent an entry from the user."""
    website: str
    name: str
    password: str = ""
    encrypted_pw: str = ""
    #not pretty but it works FIX
    def password_maker(self, password: str, encrypted_pw: str) -> None:
        self.password = password
        self.encrypted_pw = encrypted_pw
