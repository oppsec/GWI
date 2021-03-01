from rich import print

def get_ascii():
    with open('design/ascii.txt') as file:
        content = file.read()
        print(f"[magenta]{content}[/]")
