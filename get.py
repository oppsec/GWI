import requests
import time
import whois
import os
from colorama import Fore, Back, Style

ascii = """
                              
                         .-.  
  .--.    ___  ___  ___ ( __) 
 /    \  (   )(   )(   )(''") 
;  ,-. '  | |  | |  | |  | |  
| |  | |  | |  | |  | |  | |  
| |  | |  | |  | |  | |  | |  
| |  | |  | |  | |  | |  | |  
| '  | |  | |  ; '  | |  | |  
'  `-' |  ' `-'   `-' '  | |  
 `.__. |   '.__.'.__.'  (___) 
 ( `-' ;                      
  `.__.     
"""


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def start():
    clear()
    print(Fore.YELLOW + ascii)
    print("Get Website Info | @dsmuix\n")

    print(Fore.RED + "- Only works with HTTPS webistes (https://...)")
    website_input = input(Fore.YELLOW + "- What is the website url?: ")
    r = requests.get(website_input)

    if r.status_code == 200:
        print(Fore.GREEN + "\n- [!] Connected [200]")
        time.sleep(3)
        website_info(website_input)
    else:
        print(Fore.RED + "\n- [x] Connection failed")
        time.sleep(1)
        start()


def website_info(website_input):
    print(Fore.YELLOW + "- [!] Getting website info...\n")
    time.sleep(1)
    domain = whois.whois(website_input)
    print("- [!] Domain:", domain['domain'])
    print("- [!] Registrant:", domain['registrant'])
    print("- [!] Country:", domain['country'])
    print("- [!] DNS", domain['nserver'])
    print("- [!] Admins", domain['person'])
    print("- [!] Emails", domain['email'])


start()
