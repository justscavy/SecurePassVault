import pandas as pd

from datetime import datetime as dt
from typing import Union
from cryptography.fernet import Fernet

from pathlib import Path
from classes import PWManagerEntry

class PWFileManager:
    """Manages files used by the password manager."""

    def __init__(self, csv_file_name: Union[str, Path] = "nopassword.csv") -> None:
        current_directory: Path = Path.cwd()
        self.csv_file_path = current_directory / csv_file_name
        self.time = dt.now().strftime("%d-%m-%Y %H:%M:%S")

    

    def store(self, pw_manager_entry: PWManagerEntry):
        """write given user data & gen.pw"""
        #try to read, if it doesnt exist create it!
        try:
            df = pd.read_csv(self.csv_file_path)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Website", "Name", "Password", "Last updated"])
        
        mask = df["Website"] == pw_manager_entry.website 
        if mask.any():
            #if given website already exists, just update it with new data
            df.loc[mask, ["Name", "Password", "Last updated"]] = [
                pw_manager_entry.name,
                pw_manager_entry.encrypted_pw,
                self.time
            ]
        else:
            #else create new row & list
            row = pd.DataFrame(
                [[
                    pw_manager_entry.website,
                    pw_manager_entry.name,
                    pw_manager_entry.encrypted_pw,
                    self.time
                ]], 
                columns=["Website", "Name", "Password", "Last updated"]
            )
            df = pd.concat([df, row], ignore_index=True)
        df.to_csv(self.csv_file_path, index=False)

    def view(self, crypter: Fernet):
        """Display data"""
        data = pd.read_csv(self.csv_file_path)
        #decrypt and replace the cleartext.
        pws: list = [] 
        for entry in data.Password:
            decrypted_pw: bytes = crypter.decrypt(entry.encode())
            decoded_pw: str = decrypted_pw.decode()
            pws.append(decoded_pw)
        #column password = cleartext password
        data["Password"] = pws
        print(data)
        
        
