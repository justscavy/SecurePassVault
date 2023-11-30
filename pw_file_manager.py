from datetime import datetime as dt
from typing import Union
from pathlib import Path

from cryptography.fernet import Fernet
import pandas as pd

from classes import PWManagerEntry


class PWFileManager:
    """Manages files used by the password manager."""
    def __init__(self, csv_file_name: Union[str, Path] = "nopasswords.csv") -> None:
        #create user input file if it doesnt exist into current dir.
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
        
        checker = df["Website"] == pw_manager_entry.website 
        if checker.any():
            #if given website exists already just update the selected (loc) row with name,pw and timestamp
            df.loc[checker, ["Name", "Password", "Last updated"]] = [
                pw_manager_entry.name,
                pw_manager_entry.encrypted_pw,
                self.time
            ]
        else:
            #if no website dublicates exist, create a new row & insert entrys from pw_manager_entry
            new_row = pd.DataFrame(
                [[
                    pw_manager_entry.website,
                    pw_manager_entry.name,
                    pw_manager_entry.encrypted_pw,
                    self.time
                ]], 
                columns=["Website", "Name", "Password", "Last updated"]
            )#concat the new created entry to the existing df
            df = pd.concat([df, new_row], ignore_index=True)
            #finaly convert type df back to csv
        df.to_csv(self.csv_file_path, index=False)

    def view(self, crypter: Fernet):
        """Display data from the menu"""
        try:
            data = pd.read_csv(self.csv_file_path)
            #decrypt and replace with cleartext for each field in Password.
            pws_cleartext: list = [] 
            for entry in data.Password:
                decrypted_pw: bytes = crypter.decrypt(entry.encode())
                decoded_pw: str = decrypted_pw.decode()
                #put all cleartexts into pws
                pws_cleartext.append(decoded_pw)
                #concat pws_cleartext with df
            data["Password"] = pws_cleartext
            print(data)
        except FileNotFoundError as e:
                print(f"There are no entries yet. {e}")


        
        
