
import csv
from classes import User
from datetime import datetime as dt
from icecream import ic







class Datawriter(User):
    """write data in .txt and csv file"""
    def __init__(self, website: str, name: str, password: str = "", hashed="", time= str):
        super().__init__(website, name, password, hashed)
        self.time = dt.now().strftime("%d-%m-%Y %H:%M:%S")

    def WriteResults(self) -> None:
        file_path_txt = "/home/ubuntuuser/py_practice/day1/FINALPROJECT/results/nopassword.txt"
        with open(file=file_path_txt, mode="r+") as f:
            file_content = f.read()
            if self.website in file_content:
                website_pos = file_content.find(f"the website: {self.website}")
                if website_pos != -1:
                    f.seek(website_pos)
                    data_list = [
                        f"the website: {self.website}\n",
                        f"Your name: {self.name}\n",
                        f"Your password: {self.password}\n",
                        f"Your hash:{self.hashed}\n"
                        f"last changed:{self.time}\n",
                    ]
                    f.writelines(data_list)
            else:
                with open(file_path_txt, mode="a") as f:
                    data_list = [
                        f"the website: {self.website}\n",
                        f"Your name: {self.name}\n",
                        f"Your password: {self.password}\n",
                        f"Your hash:{self.hashed}\n"
                        f"last changed:{self.time}\n",
                    ]
                    f.writelines(data_list)
        return data_list 
"""
    def WriteResults(self)  -> None:
            file_path_txt = "/home/ubuntuuser/py_practice/day1/FINALPROJECT/results/nopassword.txt"
            #file_path_csv = "/home/ubuntuuser/py_practice/day1/FINALPROJECT/results/nopassword.csv"

            with open(file=file_path_txt, mode="r+") as f:
                file_content = f.read()
                if self.website in file_content:
                    
                    f.seek(0)
                    f.write(f"last changed:{time}\n")
                    f.write(f"the website: {self.website}\n")
                    f.write(f"Your name: {self.name}\n")
                    f.write(f"Your password: {self.password}\n")
                    f.write(f"Your hash:{self.hashed}\n\n")
                    f.close()
                else:
                    with open(file_path_txt, mode="a") as f:
                        f.write(f"last changed:{time}\n")
                        f.write(f"the website: {self.website}\n")
                        f.write(f"Your name: {self.name}\n")
                        f.write(f"Your password: {self.password}\n")
                        f.write(f"Your hash:{self.hashed}\n\n")
                        f.close()  
                        """
        #the overwrite always happens from line 1, maybe put lists into the file and define what element website is in and overwrite OR use sets since keys are unique
"""
            with open(file=file_path_csv, mode="a", newline="") as f:
                

                fieldnames: list = ["Last changed", "Website", "Name", "Password", "Hashed"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                # Check if the file is empty, and write headers if needed
                if f.tell() == 0:
                    writer.writeheader()
                

                writer.writerow({
                    "Last changed": time,
                    "Website": self.website,
                    "Name": self.name,
                    "Password": self.password,
                    "Hashed": self.hashed
                })"""

       


            
         
