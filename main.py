
from resultwriter import Datawriter
from icecream import ic
from account_creation import create_account
from generator_settings import password_generator
from plates import sheet
def main():

    sheet() #create template
    user = create_account() #user_information
    password, hashed = password_generator() #generator_logic
    user.password_maker(password, hashed) #eh weis ned so wirklich
    datawriter: Datawriter = Datawriter(user.website,
                                        user.name,
                                        user.password,
                                        user.hashed
                                                    )
    datawriter.writeresults()   #write results to .txt .csv #fixing

    ic(f"hash: {user.hashed}")
    ic(f"Website: {user.website}")
    ic(f"Username: {user.name}")
    ic(f"Password: {user.password}")


main()
    