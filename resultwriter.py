
import csv
from classes import User
from datetime import datetime as dt
from icecream import ic
import os


class Datawriter(User):
    """write data in .txt and csv file"""
    def __init__(self, website: str, name: str, password: str = "", hashed="", time= str):
        
        super().__init__(website, name, password, hashed)
        self.time = dt.now().strftime("%d-%m-%Y %H:%M:%S")
        
    def writeresults(self):
        file_path_csv = "/home/ubuntuuser/py_practice/day1/FINALPROJECT/results/nopassword.csv"
        rows = []

        with open(file=file_path_csv, mode = "r", newline="") as f:
            reader = csv.reader(f)
            header, *rows = reader
            rows = [[self.website, self.name, self.password, self.hashed, self.time] if row[0] == self.website else row for row in rows]

        with open(file=file_path_csv, mode = "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows([header] + rows)

        if not any(row[0] == self.website for row in rows):
            with open(file=file_path_csv, mode = "a", newline="") as f:
                writer = csv.writer(f)
                if f.tell() == 0:
                    writer.writerow(["Website", "Name", "Password", "Hashed", "Date"])
                writer.writerow([self.website, self.name, self.password, self.hashed, self.time])


"""
#class Datawriter(User):
#    write data in .txt and csv file
#    def __init__(self, website: str, name: str, password: str = "", hashed="", time= str):
#        super().__init__(website, name, password, hashed)
#        self.time = dt.now().strftime("%d-%m-%Y %H:%M:%S")
#
#    def WriteResults(self) -> None:
#        file_path_txt = "/home/ubuntuuser/py_practice/day1/FINALPROJECT/results/nopassword.txt"
#        
#        with open(file=file_path_txt, mode="r+") as f:
#            file_content = f.read()
#            if self.website in file_content:
#                website_pos = file_content.find(f"the website: {self.website}")
#                if website_pos != -1:
#                    f.seek(website_pos)
#                    data_list = [
#                        f"the website: {self.website}\n",
#                        f"Your name: {self.name}\n",
#                        f"Your password: {self.password}\n",
#                        f"Your hash:{self.hashed}\n"
#                        f"last changed:{self.time}\n",
#                    ]
#                    f.writelines(data_list)
#                    f.writelines("\n")
#            else:
#                with open(file_path_txt, mode="a") as f:
#                    data_list = [
#                        f"the website: {self.website}\n",
#                        f"Your name: {self.name}\n",
#                        f"Your password: {self.password}\n",
#                        f"Your hash:{self.hashed}\n"
#                        f"last changed:{self.time}",
#                    ]
#                    f.writelines(data_list)
#                
#        return data_list 
"""