from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich import box
from rich.prompt import FloatPrompt, IntPrompt
from models.account import Account, AccountType



# In-memory storage (in a real app, this would be a database)
accounts = []
# ============================================
# ACCOUNT MANAGEMENT FUNCTIONS
# ============================================

def manage_accounts_menu(show_header, console, current_user):
    """Display account management menu."""
    while True:
        show_header(console)
        console.print("[bold cyan]Account Management[/bold cyan]\n")
        
        menu_table = Table(show_header=False, box=box.SIMPLE, padding=(0, 2))
        menu_table.add_column("Option", style="cyan", justify="right")
        menu_table.add_column("Description", style="white")
        
        menu_table.add_row("1", "View Accounts")
        menu_table.add_row("2", "Create Account")
        menu_table.add_row("0", "Back to Main Menu")
        
        console.print(Panel(menu_table, title="[bold]Account Menu[/bold]", border_style="blue"))
        
        choice = Prompt.ask("\n[yellow]Select an option[/yellow]", choices=["0", "1", "2"])
        
        if choice == "0":
            break
        elif choice == "1":
            view_accounts(show_header, console, current_user)
        elif choice == "2":
            create_account(show_header, console, current_user)


def view_accounts(show_header, console, current_user):
    """Display all accounts for the current user."""
    show_header(console)
    console.print("[bold cyan]Your Accounts[/bold cyan]\n")
    
    user_accounts = [acc for acc in accounts if acc.user_id.id == current_user.id]
    
    if not user_accounts:
        console.print("[yellow]No accounts found. Create one to get started![/yellow]")
    else:
        account_table = Table(show_header=True, header_style="bold magenta")
        account_table.add_column("ID", justify="right", style="cyan")
        account_table.add_column("Name", style="green")
        account_table.add_column("Type", style="blue")
        account_table.add_column("Balance", justify="right", style="yellow")
        
        total_balance = 0
        for acc in user_accounts:
            account_table.add_row(
                str(acc.id),
                acc.name,
                acc.account_type.value.replace('_', ' ').title(),
                f"${acc.balance:,.2f}"
            )
            total_balance += acc.balance
        
        console.print(account_table)
        console.print(f"\n[bold green]Total Balance: ${total_balance:,.2f}[/bold green]")
    
    Prompt.ask("\n[dim]Press Enter to continue[/dim]")
    return user_accounts


def create_account(show_header, console, current_user):
    """Create a new account for the current user."""
    show_header(console)
    console.print("[bold cyan]Create New Account[/bold cyan]\n")
    
    name = Prompt.ask("[green]Account name[/green]")
    
    console.print("\n[cyan]Account Types:[/cyan]")
    for i, acc_type in enumerate(AccountType, 1):
        console.print(f"  {i}. {acc_type.value.replace('_', ' ').title()}")
    
    type_choice = IntPrompt.ask("\n[yellow]Select account type[/yellow]", choices=["1", "2", "3", "4"])
    account_type = list(AccountType)[type_choice - 1]
    
    balance = FloatPrompt.ask("[green]Initial balance[/green]", default=0.0)
    
    account_id = len(accounts) + 1
    new_account = Account(
        id=account_id,
        user_id=current_user,
        name=name,
        account_type=account_type,
        balance=balance
    )
    accounts.append(new_account)
    
    console.print(f"\n[green]✓ Account created successfully![/green]")
    console.print(new_account)
    Prompt.ask("\n[dim]Press Enter to continue[/dim]")

