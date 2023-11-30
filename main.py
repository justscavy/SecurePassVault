from pathlib import Path

from pw_manager import PWManager
from intro import plate
from login_function import login
from key_manager import key_management


#keypath
key_file: Path = Path("key.key")


def main() -> None:
    plate(input_word="PASSWORD-MANAGER", input_width=40) #create template
    crypter = key_management(key_file=key_file) #create or load an existing key.
    if login(crypter=crypter, key_file=key_file):
        pw_manager: PWManager = PWManager(crypter=crypter)  
        pw_manager.main_menu()


if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt:
        print("\nProgramm closed by User interrupt")

    