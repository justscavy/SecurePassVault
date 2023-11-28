
from resultwriter import Datawriter
from icecream import ic
from account_manager import account_management, create_account #generate_key
from generator_settings import password_generator
from plates import sheet

def main():
   
    sheet(input_word="PASSWORD-MANAGER",input_width=40) #create template
    user = account_management()
    #generate_key()  
    password, hashed = password_generator() #generator_logic
    user.password_maker(password, hashed) #eh weis ned so wirklich
    datawriter: Datawriter = Datawriter(user.website,
                                        user.name,
                                        user.password,
                                        user.hashed,
                                                    )
    datawriter.writeresults()   #write results to .csv #fixing

    ic(f"hash: {user.hashed}")
    ic(f"Website: {user.website}")
    ic(f"Username: {user.name}")
    ic(f"Password: {user.password}")


main()
    