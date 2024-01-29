from pynput.keyboard import Key, Controller, Listener
import sys
import time
import threading
from colorama import Fore

keyboard = Controller()
clicking = False

banner = """
███████╗         ██████╗██╗     ██╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝        ██╔════╝██║     ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗
█████╗          ██║     ██║     ██║██║     █████╔╝ █████╗  ██████╔╝
██╔══╝          ██║     ██║     ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
███████╗███████╗╚██████╗███████╗██║╚██████╗██║  ██╗███████╗██║  ██║
╚══════╝╚══════╝ ╚═════╝╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝        
"""

print(banner)
print("\nCoded By Mohamed. Message him if you have any questions.")
print("\nPress f12 to click.\nPress esc to exit the program.\n")


def on_press(key):
    global clicking
    if key == Key.f12:
        clicking = not clicking
        print(
            f"{Fore.GREEN}[LOG]{Fore.WHITE} {'Started' if clicking else 'Stopped'} clicking. Press f12 again to {'stop' if clicking else 'start'}."
        )
    elif key == Key.esc:
        print(f"{Fore.GREEN}[LOG]{Fore.WHITE} Exiting program...")
        sys.exit(0)


def click_e():
    while True:
        if clicking:
            keyboard.press("e")
            keyboard.release("e")
            print(f"{Fore.GREEN}[LOG]{Fore.WHITE} Clicked E successfully.")
            time.sleep(0.01)


with Listener(on_press=on_press) as listener:

    clicking_thread = threading.Thread(target=click_e)
    clicking_thread.daemon = True
    clicking_thread.start()

    try:
        listener.join()
    except Exception as e:
        print(
            f"{Fore.RED}[ERROR]{Fore.WHITE} An error occurred. Send a picture of this to Mohamed:"
        )
        print(e)
