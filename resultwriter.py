
import csv
from classes import User
from datetime import datetime as dt
from icecream import ic
import os
import pandas as pd
from cryptography.fernet import Fernet


class Datawriter(User):
    """write data in a csv file"""
    def __init__(self, website="", name="", password: str = "", hashed=""):  #inherit what we already have from superclass
        super().__init__(website, name, password, hashed)
        self.time = dt.now().strftime("%d-%m-%Y %H:%M:%S")
        #self.key = key                 #add timestamp

    #def decrypt_data(self, encrypted_data):
    #    crypter = Fernet(self.key)
    #    decrypted_data = crypter.decrypt(encrypted_data)
    #    return decrypted_data.decode()

    
    def writeresults(self):
        """write given user data & gen.pw"""
        file_path_csv = "/home/ubuntuuser/FINALPROJECT/results/nopassword.csv"
        
        try:
            df = pd.read_csv(file_path_csv) #try to read, if it doesnt exist create it!
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Website", "Name", "Password", "Hashed", "Date"])
        mask = df["Website"] == self.website 
        if mask.any():
            df.loc[mask, ["Name", "Password", "Hashed", "Date"]] = [self.name, self.password, self.hashed, self.time]   # if given website already exsits update it.
        else:
            row = pd.DataFrame([[self.website, self.name, self.password, self.hashed, self.time]],         #else append given data in next row
                                   columns=["Website", "Name", "Password", "Hashed", "Date"])
            df = pd.concat([df, row], ignore_index=True)
        df.to_csv(file_path_csv, index=False)
    
    def view_file(self):
        encrypted_data = pd.read_csv("/home/ubuntuuser/FINALPROJECT/results/nopassword.csv") 
        decrypted_data = self.decrypt_data(encrypted_data)
        data = pd.read_csv(pd.compat.StringIO(decrypted_data))
        print(data)
        #key = b'your_key_here'
        #result_writer = ResultWriter()
        #result_writer.view_file()

        