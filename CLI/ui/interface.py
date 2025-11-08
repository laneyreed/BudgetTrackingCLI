from rich.console import Console
from rich.text import Text
from rich import box
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich.theme import Theme


from ui.users import user_management_menu, current_user
from ui.accounts import manage_accounts_menu, view_accounts
from ui.transactions import add_transaction, view_transactions, view_summary

#===============================================================
# UI Color Theme 
#===============================================================
PROMPT_COLOR = "YELLOW" 
HEADER_COLOR = "#4c067a"
MENU_OPTION_COLOR = "yellow"
MENU_DESCRIPTION_COLOR = "green"

# Custom theme for the CLI
custom_theme = Theme({
    "prompt.choices": PROMPT_COLOR,  
    # "prompt.default": "bright_magenta",
    "menu.option": MENU_OPTION_COLOR,
    "menu.description": MENU_DESCRIPTION_COLOR,
    "header": HEADER_COLOR,

})
#===============================================================

#===============================================================
# Choices for menus
#===============================================================
LOGGED_OUT_CHOICES = ["0", "1"]
LOGGED_IN_CHOICES = ["0", "1", "2", "3", "4", "5"]
#===============================================================

#===============================================================
# Initialize Rich console with custom theme
#===============================================================
console = Console(theme=custom_theme)


#=================================================================================
# Helper Functions
#=================================================================================
def keyboardInterruptMessage():
    """Displays a keyboard interrupt message."""
    console.print("\n\n[yellow]Application interrupted. Goodbye! 👋[/yellow]")

def otherErrorMessage(e):
    """Displays an error message for unexpected exceptions."""
    console.print(f"\n[red]An error occurred: {e}[/red]")

def loggedOut(menu):
    """Menu options for logged out users."""
    menu.add_row("1", "Create/Select User")
    menu.add_row("0", "Exit")

def loggedIn(menu):
    """Menu options for logged in users."""

    menu.add_row("1", "Manage Accounts")
    menu.add_row("2", "Add Transaction")
    menu.add_row("3", "View Transactions")
    menu.add_row("4", "View Summary")
    menu.add_row("5", "Switch User")
    menu.add_row("0", "Exit")

def createMenu():
    """Creates and returns a menu table."""

    menu_table = Table(show_header=False, box=box.SIMPLE, padding=(0, 2))
    menu_table.add_column("Option", style=MENU_OPTION_COLOR, justify="right")
    menu_table.add_column("Description", style=MENU_DESCRIPTION_COLOR)
    return menu_table




def show_header(console):
    """Displays CLI Header"""

    console.clear()
    header_text = Text("💰 BUDGET TRACKER 💰", justify="center")
    console.print(Panel(header_text, box=box.DOUBLE))
    if current_user:
        console.print(f"[green]Logged in as:[/green] [bold]{current_user.name}[/bold] ({current_user.email})\n")
#===========================================================================


#==========================================================================
# Main Menu Function
#==========================================================================
def main_menu(categories):
    """Display the main menu and handle user input."""

    current_user = None


    while True:
        show_header(console)
        
        menu = createMenu()
        
        if not current_user:
            loggedOut(menu)
        else:
            loggedIn(menu)

        console.print(Panel(menu, title="[bold]Main Menu[/bold]", border_style="yellow"))

        choice = Prompt.ask(
            "\n[green]Select an option[/green]",
            choices=LOGGED_IN_CHOICES if current_user else LOGGED_OUT_CHOICES,
            default=None,
            show_choices=True,
            console=console
        )

        if choice == "0":
            console.print("\n[green]Thank you for using Budget Tracker! Goodbye! 👋[/green]")
            break
        elif choice == "1":
            if current_user:
                manage_accounts_menu(show_header, console, current_user)
            else:
                current_user = user_management_menu(show_header, console)
        elif choice == "2" and current_user:
            user_accounts = view_accounts(show_header, console, current_user)
            add_transaction(show_header, console, current_user, user_accounts, categories)
        elif choice == "3" and current_user:
            view_transactions(show_header, console, current_user)
        elif choice == "4" and current_user:
            user_accounts = view_accounts(show_header, console, current_user)
            view_summary(show_header, console, current_user, user_accounts)
        elif choice == "5" and current_user:
            user_management_menu(show_header, console)
