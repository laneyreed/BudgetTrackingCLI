from rich.console import Console
from rich.text import Text
from rich import box
from rich.panel import Panel

def printHeader():
    console = Console()
    # header_text = Text("💰 BUDGET TRACKER 💰", justify="center")
    # console.print(Panel(header_text, box=box.DOUBLE))
    console.print("\n[header]Welcome to the Application CLI![/header]\n", justify="center")

#================================================================
# Are you a new user or existing user?
# new user = login
# existing user = register
#================================================================

#================================================================
# Generic login function
#================================================================
def login():
    # for now create a generic login flow
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print(f"Logging in as: {username}")



#================================================================
# Generic register function
#================================================================
def register():    # for now create a generic register flow
    username = input("Choose a username: ")
    password = input("Choose a password: ")
    print(f"Registering new user: {username}.....")
    login()

def loginOrRegister():
    while True:
        choice = input("Enter 1 to login or 2 to register: ")
        if choice == "1":
            login()
            break
        elif choice == "2":
            register()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def main():
    while True:
        printHeader()
        loginOrRegister()
        break