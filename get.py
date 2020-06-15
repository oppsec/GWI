import requests
import time
import whois
import os
from colorama import Fore, Back, Style

ascii = """
  ▄████  █     █░ ██▓
 ██▒ ▀█▒▓█░ █ ░█░▓██▒
▒██░▄▄▄░▒█░ █ ░█ ▒██▒
░▓█  ██▓░█░ █ ░█ ░██░
░▒▓███▀▒░░██▒██▓ ░██░
 ░▒   ▒ ░ ▓░▒ ▒  ░▓  
  ░   ░   ▒ ░ ░   ▒ ░
░ ░   ░   ░   ░   ▒ ░
      ░     ░     ░  
                     
Get Website Info 1.0 | @dsmuix   
"""


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def start():
    clear()
    print(Fore.LIGHTYELLOW_EX + ascii)

    print(Fore.LIGHTRED_EX + "- [!] Only works with HTTPS webistes (https://...)")
    website_input = input(Fore.YELLOW + "- [?] What is the website url?: ")
    r = requests.get(website_input)
    print(Fore.LIGHTYELLOW_EX + "- [!] Trying connection...")

    try:
        if r.status_code == 200:
            print(Fore.LIGHTGREEN_EX + "\n- [!] Connected [200]")
            time.sleep(2)
            verify(website_input)
        else:
            print(Fore.LIGHTRED_EX + "\n- [x] Connection failed")
            time.sleep(1)
            start()
    except ConnectionRefusedError:
        print(Fore.RED + "- [x] Website blocked the request")
        time.sleep(2)
        start()


def verify(website_input):
    if '.com.br' in website_input:
        website_br(website_input)
    else:
        website_com(website_input)


def website_br(website_input):
    print(Fore.LIGHTYELLOW_EX + "- [!] Getting website info...\n")
    time.sleep(1)
    domain = whois.whois(website_input)
    dget = domain.get

    print("### WEBSITE ###")
    print("- [#] Domain:", dget('domain', 'Not found'))
    print("- [#] Registrant:", dget('registrant', 'Not found'))
    print("- [#] DNS:", dget('nserver', 'Not found'))
    print("- [#] Names:", dget('person', 'Not found'))
    print("- [#] Mails:", dget('email', 'Not found'))
    print("- [#] Organization:", dget('org', 'Not found'))

    print(Fore.LIGHTCYAN_EX + "\n\n### LOCALIZATION ###")
    print("- [#] Name:", dget('name', 'Not found'))
    print("- [#] Address:", dget('address', 'Not found'))
    print("- [#] Country:", dget('country', 'Not found'))
    print("- [#] State:", dget('state', 'Not found'))


def website_com(website_input):
    print(Fore.LIGHTYELLOW_EX + "- [!] Getting website info...\n")
    time.sleep(1)
    domain = whois.whois(website_input)
    dget = domain.get

    print("### WEBSITE ###")
    print("- [#] Domain:", dget('domain_name', 'Not found'))
    print("- [#] Registrant:", dget('registrar', 'Not found'))
    print("- [#] DNS:", dget('name_servers', 'Not found'))
    print("- [#] Mails:", dget('emails', 'Not found'))
    print("- [#] Organization:", dget('org', 'Not found'))

    print(Fore.LIGHTCYAN_EX + "\n### LOCALIZATION ###")
    print("- [#] Name:", dget('name', 'Not found'))
    print("- [#] Address:", dget('address', 'Not found'))
    print("- [#] Country:", dget('country', 'Not found'))
    print("- [#] State:", dget('state', 'Not found'))


start()
