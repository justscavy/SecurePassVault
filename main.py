
from resultwriter import Datawriter
from icecream import ic
from account_manager import account_management, create_account #generate_key
from generator_settings import password_generator
from plates import sheet
from cryptography.fernet import Fernet
def main():
   
    sheet(input_word="PASSWORD-MANAGER",input_width=40) #create template
    crypter: Fernet = Fernet(Fernet.generate_key())
    user = account_management(crypter=crypter)

    password, hashed = password_generator(crypter=crypter) #generator_logic
    user.password_maker(password, hashed) #eh weis ned so wirklich
    datawriter: Datawriter = Datawriter(
        user.website,
        user.name,
        user.password,
        user.hashed,
    )
    datawriter.writeresults()   #write results to .csv #fixing
    Datawriter.view_file(crypter=crypter)

    ic(f"hash: {user.hashed}")
    ic(f"Website: {user.website}")
    ic(f"Username: {user.name}")
    ic(f"Password: {user.password}")


main()
    