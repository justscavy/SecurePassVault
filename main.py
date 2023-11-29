from pw_manager import PWManager
from plates import sheet
from __init__ import key_manager, login


def main(): 
    sheet(input_word="PASSWORD-MANAGER", input_width=40) #create template
    crypter = key_manager() #create or load an existing key.
    while True:
        if login(crypter):
            pw_manager: PWManager = PWManager(crypter=crypter)  
            pw_manager.main_menu()
        else: 
            break


if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt:
        print("\nProgramm closed by User interrupt")
    