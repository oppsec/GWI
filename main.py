import whois
import os
import requests

from rich import print

from design.ascii import get_ascii
from design.clear import clear

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ascii_dots = "[bold white]. . . . . . . . . . . . . . . . . . .[/] \n"


def main():
    clear()
    get_ascii()

    print(ascii_dots)
    check_website()


def check_website():
    website_url = input("::  Website URL ~> ")

    try:
        response = requests.get(website_url, verify=False, timeout=10)
        status_code = response.status_code

        if(status_code == 200):
            print('\n[bold green][!] | Connected[/]', ":smiley:")
            whois_website(website_url)
        else:
            print("\n[bold red][!] | Can't connect [/]", ":rage:")

    except requests.exceptions.ConnectionError:
        return print("[bold red][!] | Connection error, check your URL and website status.")
    except requests.exceptions.MissingSchema:
        return print("[bold red][!] | URL without http or https, please verify.")

def whois_website(website_url):
    domain = whois.whois(website_url)
    
    name = domain.name
    registrant_name = domain.registrar
    name_servers = domain.name_servers

    print(f"""[magenta]
:: Domain: {name}
:: Registrant Name: {registrant_name}
:: Name Servers: {name_servers}
    [/]""")
    

if __name__ == '__main__':
    main()