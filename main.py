import whois
import os
import socket
import requests

from rich import print
from rich.prompt import Prompt

## ASCII BANNER
ascii = """[bold magenta]

   _|_|_|  _|          _|  _|_|_|
 _|        _|          _|    _|
 _|  _|_|  _|    _|    _|    _|
 _|    _|    _|  _|  _|      _|
   _|_|_|      _|  _|      _|_|_|

    Get Website Info 2.0 | oppsec [/bold magenta]
"""

ascii_dots = "[bold white]. . . . . . . . . . . . . . . . . . .[/] \n"


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    clear_terminal()

    print(ascii)
    print(ascii_dots)

    get_username = socket.gethostname()
    print(f"[!] Welcome [bold magenta]{get_username}[/]", ":smiley:", "\n")

    check_website()


## Check Website Status
def check_website():
    print("[bold red]![/] Only works with [bold red]HTTPS[/] websites")
    website_url = Prompt.ask('[bold green]#[/] Website URL', default="https://...")
    website_request = requests.get(website_url)

    if(website_request.status_code == 200):
        print('\n[bold green]# 200 | Connected[/]', ":smiley:", '\n')
        get_website_information(website_url)
    else:
        print("\n[bold red]# ERROR | Can't connect [/]", ":rage:", '\n')


def get_website_information(website_url):

    ## Website Informations - Class
    class whois_website:
        def __init__(self, website_url):
            whois_website = whois.whois(website_url)
            self.domain_name = whois_website['domain_name']
            self.registrant_name = whois_website['registrant_name']
            self.websiteCountry = whois_website['country']
            self.websiteStatus = whois_website['status']
            self.websiteEmail = whois_website['email']

        ## Return website informations

        def __str__(self):
            content_data = [
                f"Domain Name ~> {self.domain_name}\n",
                f"Registrant Name {self.registrant_name}\n",
                f"Website Country {self.websiteCountry}\n",
                f"Website Status {self.websiteStatus}\n",
                f"Emails {self.websiteEmail}"
            ]

            for info in content_data:
                print(info)

    try:
        website_info = whois_website(website_url)
        print(website_info)
    except:
        print("[bold blue]Sorry I couldn't get any information[/]", ":sob:")

if __name__ == '__main__':
    menu()
