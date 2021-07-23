#!/usr/bin/python3
# This Code Write by Mr.nope
# My-IP 1.2

import os
import platform
import time
import sys
import socket

system = platform.uname()[0]
os_Err = "\nPlease, Run This Programm on Linux, Windows, MacOS!\n"
banner = """
 __    __     __  __     __     ______  
/\ "-./  \   /\ \_\ \   /\ \   /\  == \ 
\ \ \-./\ \  \ \____ \  \ \ \  \ \  _-/ 
 \ \_\ \ \_\  \/\_____\  \ \_\  \ \_\   
  \/_/  \/_/   \/_____/   \/_/   \/_/   \n"""


def cls():
    if system == 'Windows':
        os.system("title My-IP")
        os.system("cls")
    elif system == 'Linux':
        os.system("printf '\033]2;My-IP\a'")
        os.system("clear")
    else:
        print(os_Err)
        sys.exit()
def main():
    cls()
    print(banner)
    print("------------------------------------")
    s = socket.gethostname()
    ip = socket.gethostbyname(s)
    print(f"""Host: {s}
IP: {ip}
------------------------------------\n""")
    time.sleep(0.50)
    input("\npress Enter...")
    print("\n")
    sys.exit()
if __name__ == '__main__':
    main()