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

  Get Website Info | @dsmuix   
"""


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def start():
    clear()
    print(Fore.YELLOW + ascii)

    print(Fore.RED + "- [!] Only works with HTTPS webistes (https://...)")
    website_input = input(Fore.YELLOW + "- [?] What is the website url?: ")
    r = requests.get(website_input)
    print(Fore.YELLOW + "- [!] Trying connection...")

    if r.status_code == 200:
        print(Fore.GREEN + "\n- [!] Connected [200]")
        time.sleep(2)
        verify(website_input)
    else:
        print(Fore.RED + "\n- [x] Connection failed")
        time.sleep(1)
        start()


def verify(website_input):
    if '.com.br' in website_input:
        website_br(website_input)
    else:
        website_com(website_input)


def website_br(website_input):
    print(Fore.YELLOW + "- [!] Getting website info...\n")
    time.sleep(1)
    domain = whois.whois(website_input)

    print("### WEBSITE ###")
    print(domain)
    print("- [#] Domain:", domain.get('domain', 'Not found'))
    print("- [#] Registrant:", domain.get('registrant', 'Not found'))
    print("- [#] DNS:", domain.get('nserver', 'Not found'))
    print("- [#] Names:", domain.get('person', 'Not found'))
    print("- [#] Emails:", domain.get('email', 'Not found'))

    print(Fore.MAGENTA + "\n### LOCALIZATION ###")
    print("- [#] Name:", domain.get('name', 'Not found'))
    print("- [#] Address:", domain.get('address', 'Not found'))
    print("- [#] Country:", domain.get('country', 'Not found'))


def website_com(website_input):
    print(Fore.YELLOW + "- [!] Getting website info...\n")
    time.sleep(1)
    domain = whois.whois(website_input)

    print("### WEBSITE ###")
    print("- [#] Domain:", domain.get('domain_name', 'Not found'))
    print("- [#] Registrant:", domain.get('registrar', 'Not found'))
    print("- [#] DNS:", domain.get('name_servers', 'Not found'))
    print("- [#] Emails:", domain.get('emails', 'Not found'))

    print(Fore.MAGENTA + "\n### LOCALIZATION ###")
    print("- [#] Name:", domain.get('name', 'Not found'))
    print("- [#] Address:", domain.get('address', 'Not found'))
    print("- [#] Country:", domain.get('country', 'Not found'))


start()
