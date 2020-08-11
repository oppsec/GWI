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

asciiDots = "[bold white]. . . . . . . . . . . . . . . . . . .[/bold white] \n"


def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    clearTerminal()

    # GWI Banner
    print(ascii)
    print(asciiDots)

    getUsername = socket.gethostname()
    print(
        f"[!] Welcome [bold magenta]{getUsername}[/bold magenta]", ":smiley:", "\n")

    checkWebsite()


## Check Website Status
def checkWebsite():
    print("[bold red]![/bold red] Only works with [bold red]HTTPS[/bold red] websites")
    websiteLink = Prompt.ask('[bold green]#[/bold green] Website URL', default="https://...")
    websiteRequest = requests.get(websiteLink)

    if(websiteRequest.status_code == 200):
        print('\n[bold green]# 200 | Connected[/bold green]', ":smiley:", '\n')
        getWebsiteInformations(websiteLink)
    else:
        print("\n[bold red]# ERROR | Can't connect [/bold red]", ":rage:", '\n')


def getWebsiteInformations(websiteLink):

    ## Website Informations - Class
    class WhoIsInfo:
        def __init__(self, websiteLink):
            whoIsWebsite = whois.whois(websiteLink)
            self.domain_name = whoIsWebsite['domain_name']
            self.registrant_name = whoIsWebsite['registrant_name']
            self.websiteCountry = whoIsWebsite['country']
            self.websiteStatus = whoIsWebsite['status']
            self.websiteEmail = whoIsWebsite['email']

        ## Return website informations
        def __str__(self):
            return """ Domain Name ~> {domain_name} \n Registrant Name ~> {registrant_name} \n Website Country ~> {country} \n Website Status ~> {status} \n Emails ~> {email}
            """.format(domain_name=self.domain_name, registrant_name=self.registrant_name, country=self.websiteCountry, status=self.websiteStatus, email=self.websiteEmail)
    
    try:
        websiteInfo = WhoIsInfo(websiteLink)
        print(websiteInfo)
    except:
        print("[bold blue]Sorry I couldn't get any information[/bold blue]", ":sob:")

if __name__ == '__main__':
    menu()
