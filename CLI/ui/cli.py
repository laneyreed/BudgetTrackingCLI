"""
Budget Tracker CLI Application
A command-line interface for managing personal finances.
"""

from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm, IntPrompt, FloatPrompt
from rich import box
from rich.layout import Layout
from rich.text import Text

from models.user import User
from models.account import Account
from models.category import Category
from models.transaction import Transaction
from utils.constants import (
    AccountType, 
    TransactionType, 
    DEFAULT_EXPENSE_CATEGORIES, 
    DEFAULT_INCOME_CATEGORIES
)

# Initialize Rich console
console = Console()

# In-memory storage (in a real app, this would be a database)
users = []
accounts = []
categories = []
transactions = []
current_user = None

# Initialize some default categories
def initialize_categories():
    """Initialize default categories for the application."""
    global categories
    category_id = 1
    
    for cat_name in DEFAULT_EXPENSE_CATEGORIES:
        categories.append(Category(id=category_id, name=cat_name, description=f"Expense: {cat_name}"))
        category_id += 1
    
    for cat_name in DEFAULT_INCOME_CATEGORIES:
        categories.append(Category(id=category_id, name=cat_name, description=f"Income: {cat_name}"))
        category_id += 1


def show_header():
    """Display the application header."""
    console.clear()
    header_text = Text("💰 BUDGET TRACKER 💰", style="#4c067a", justify="center")
    console.print(Panel(header_text, border_style="#4c067a", box=box.DOUBLE))
    if current_user:
        console.print(f"[green]Logged in as:[/green] [bold]{current_user.name}[/bold] ({current_user.email})\n")


def main_menu():
    """Display the main menu and handle user input."""
    while True:
        show_header()
        
        menu_table = Table(show_header=False, box=box.SIMPLE, padding=(0, 2))
        menu_table.add_column("Option", style="cyan", justify="right")
        menu_table.add_column("Description", style="white")
        
        if not current_user:
            menu_table.add_row("1", "Create/Select User")
            menu_table.add_row("0", "Exit")
        else:
            menu_table.add_row("1", "Manage Accounts")
            menu_table.add_row("2", "Add Transaction")
            menu_table.add_row("3", "View Transactions")
            menu_table.add_row("4", "View Summary")
            menu_table.add_row("5", "Switch User")
            menu_table.add_row("0", "Exit")
        
        console.print(Panel(menu_table, title="[bold]Main Menu[/bold]", border_style="blue"))
        
        choice = Prompt.ask("\n[yellow]Select an option[/yellow]", choices=["0", "1", "2", "3", "4", "5"] if current_user else ["0", "1"])
        
        if choice == "0":
            console.print("\n[green]Thank you for using Budget Tracker! Goodbye! 👋[/green]")
            break
        elif choice == "1":
            if current_user:
                manage_accounts_menu()
            else:
                user_management_menu()
        elif choice == "2" and current_user:
            add_transaction()
        elif choice == "3" and current_user:
            view_transactions()
        elif choice == "4" and current_user:
            view_summary()
        elif choice == "5" and current_user:
            user_management_menu()


# ============================================
# USER MANAGEMENT FUNCTIONS
# ============================================

def user_management_menu():
    """Handle user creation and selection."""
    global current_user
    
    show_header()
    
    if users:
        console.print("[bold cyan]Existing Users:[/bold cyan]\n")
        user_table = Table(show_header=True, header_style="bold magenta")
        user_table.add_column("ID", justify="right", style="cyan")
        user_table.add_column("Name", style="green")
        user_table.add_column("Email", style="blue")
        user_table.add_column("Currency", justify="center")
        
        for user in users:
            user_table.add_row(str(user.id), user.name, user.email, user.currency)
        
        console.print(user_table)
        console.print()
    else:
        console.print("[yellow]No users found. Create your first user![/yellow]\n")
    
    action = Prompt.ask(
        "[yellow]Choose action[/yellow]",
        choices=["new", "select"] if users else ["new"],
        default="new"
    )
    
    if action == "new":
        create_user()
    elif action == "select":
        select_user()


def create_user():
    """Create a new user."""
    global current_user
    
    show_header()
    console.print("[bold cyan]Create New User[/bold cyan]\n")
    
    name = Prompt.ask("[green]Enter your name[/green]")
    email = Prompt.ask("[green]Enter your email[/green]")
    currency = Prompt.ask("[green]Preferred currency[/green]", default="USD")
    
    user_id = len(users) + 1
    new_user = User(id=user_id, name=name, email=email, currency=currency)
    users.append(new_user)
    current_user = new_user
    
    console.print(f"\n[green]✓ User created successfully![/green]")
    console.print(new_user)
    Prompt.ask("\n[dim]Press Enter to continue[/dim]")


def select_user():
    """Select an existing user."""
    global current_user
    
    if not users:
        console.print("[red]No users available![/red]")
        Prompt.ask("\n[dim]Press Enter to continue[/dim]")
        return
    
    user_id = IntPrompt.ask("[yellow]Enter User ID[/yellow]")
    
    for user in users:
        if user.id == user_id:
            current_user = user
            console.print(f"\n[green]✓ Logged in as {user.name}![/green]")
            Prompt.ask("\n[dim]Press Enter to continue[/dim]")
            return
    
    console.print("[red]User not found![/red]")
    Prompt.ask("\n[dim]Press Enter to continue[/dim]")


# ============================================
# ACCOUNT MANAGEMENT FUNCTIONS
# ============================================

def manage_accounts_menu():
    """Display account management menu."""
    while True:
        show_header()
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
            view_accounts()
        elif choice == "2":
            create_account()


def view_accounts():
    """Display all accounts for the current user."""
    show_header()
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


def create_account():
    """Create a new account for the current user."""
    show_header()
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


# ============================================
# TRANSACTION FUNCTIONS
# ============================================

def add_transaction():
    """Add a new transaction."""
    show_header()
    console.print("[bold cyan]Add Transaction[/bold cyan]\n")
    
    # Check if user has accounts
    user_accounts = [acc for acc in accounts if acc.user_id.id == current_user.id]
    if not user_accounts:
        console.print("[red]You need to create an account first![/red]")
        Prompt.ask("\n[dim]Press Enter to continue[/dim]")
        return
    
    # Select account
    console.print("[cyan]Select Account:[/cyan]")
    for i, acc in enumerate(user_accounts, 1):
        console.print(f"  {i}. {acc.name} ({acc.account_type.value}) - ${acc.balance:,.2f}")
    
    acc_choice = IntPrompt.ask("\n[yellow]Account number[/yellow]", choices=[str(i) for i in range(1, len(user_accounts) + 1)])
    selected_account = user_accounts[acc_choice - 1]
    
    # Select transaction type
    console.print("\n[cyan]Transaction Type:[/cyan]")
    console.print("  1. Income")
    console.print("  2. Expense")
    
    type_choice = IntPrompt.ask("\n[yellow]Select type[/yellow]", choices=["1", "2"])
    transaction_type = TransactionType.INCOME if type_choice == 1 else TransactionType.EXPENSE
    
    # Select category
    if transaction_type == TransactionType.INCOME:
        available_categories = [cat for cat in categories if cat.name in DEFAULT_INCOME_CATEGORIES]
    else:
        available_categories = [cat for cat in categories if cat.name in DEFAULT_EXPENSE_CATEGORIES]
    
    console.print(f"\n[cyan]Select Category:[/cyan]")
    for i, cat in enumerate(available_categories, 1):
        console.print(f"  {i}. {cat.name}")
    
    cat_choice = IntPrompt.ask("\n[yellow]Category number[/yellow]", choices=[str(i) for i in range(1, len(available_categories) + 1)])
    selected_category = available_categories[cat_choice - 1]
    
    # Get amount and description
    amount = FloatPrompt.ask("\n[green]Amount[/green]")
    description = Prompt.ask("[green]Description[/green]", default="")
    
    # Create transaction
    transaction_id = len(transactions) + 1
    new_transaction = Transaction(
        id=transaction_id,
        user_id=current_user,
        account_id=selected_account,
        transaction_type=transaction_type,
        category=selected_category,
        amount=amount,
        date=datetime.now(),
        description=description
    )
    transactions.append(new_transaction)
    
    # Update account balance
    if transaction_type == TransactionType.INCOME:
        selected_account.balance += amount
    else:
        selected_account.balance -= amount
    
    console.print(f"\n[green]✓ Transaction added successfully![/green]")
    console.print(f"New account balance: [bold]${selected_account.balance:,.2f}[/bold]")
    Prompt.ask("\n[dim]Press Enter to continue[/dim]")


def view_transactions():
    """View all transactions for the current user."""
    show_header()
    console.print("[bold cyan]Your Transactions[/bold cyan]\n")
    
    user_transactions = [t for t in transactions if t.user_id.id == current_user.id]
    
    if not user_transactions:
        console.print("[yellow]No transactions found. Add one to get started![/yellow]")
    else:
        transaction_table = Table(show_header=True, header_style="bold magenta")
        transaction_table.add_column("ID", justify="right", style="cyan")
        transaction_table.add_column("Date", style="blue")
        transaction_table.add_column("Account", style="green")
        transaction_table.add_column("Type", style="magenta")
        transaction_table.add_column("Category", style="yellow")
        transaction_table.add_column("Amount", justify="right")
        transaction_table.add_column("Description")
        
        # Sort by date (newest first)
        user_transactions.sort(key=lambda t: t.date, reverse=True)
        
        for trans in user_transactions:
            amount_style = "green" if trans.transaction_type == TransactionType.INCOME else "red"
            amount_prefix = "+" if trans.transaction_type == TransactionType.INCOME else "-"
            
            transaction_table.add_row(
                str(trans.id),
                trans.date.strftime("%Y-%m-%d %H:%M"),
                trans.account_id.name,
                trans.transaction_type.value.title(),
                trans.category.name,
                f"[{amount_style}]{amount_prefix}${trans.amount:,.2f}[/{amount_style}]",
                trans.description[:30] + "..." if len(trans.description) > 30 else trans.description
            )
        
        console.print(transaction_table)
    
    Prompt.ask("\n[dim]Press Enter to continue[/dim]")


def view_summary():
    """Display financial summary for the current user."""
    show_header()
    console.print("[bold cyan]Financial Summary[/bold cyan]\n")
    
    user_transactions = [t for t in transactions if t.user_id.id == current_user.id]
    user_accounts = [acc for acc in accounts if acc.user_id.id == current_user.id]
    
    # Calculate totals
    total_income = sum(t.amount for t in user_transactions if t.transaction_type == TransactionType.INCOME)
    total_expenses = sum(t.amount for t in user_transactions if t.transaction_type == TransactionType.EXPENSE)
    net_balance = total_income - total_expenses
    account_balance = sum(acc.balance for acc in user_accounts)
    
    # Create summary table
    summary_table = Table(show_header=False, box=box.ROUNDED, padding=(0, 2))
    summary_table.add_column("Metric", style="cyan", justify="right")
    summary_table.add_column("Value", style="bold")
    
    summary_table.add_row("Total Income", f"[green]+${total_income:,.2f}[/green]")
    summary_table.add_row("Total Expenses", f"[red]-${total_expenses:,.2f}[/red]")
    summary_table.add_row("Net (Income - Expenses)", f"[yellow]${net_balance:,.2f}[/yellow]")
    summary_table.add_row("", "")
    summary_table.add_row("Current Account Balance", f"[bold green]${account_balance:,.2f}[/bold green]")
    summary_table.add_row("Number of Transactions", str(len(user_transactions)))
    summary_table.add_row("Number of Accounts", str(len(user_accounts)))
    
    console.print(Panel(summary_table, title="[bold]Financial Overview[/bold]", border_style="green"))
    
    # Category breakdown for expenses
    if user_transactions:
        console.print("\n[bold cyan]Expense Breakdown by Category:[/bold cyan]\n")
        
        expense_by_category = {}
        for trans in user_transactions:
            if trans.transaction_type == TransactionType.EXPENSE:
                cat_name = trans.category.name
                expense_by_category[cat_name] = expense_by_category.get(cat_name, 0) + trans.amount
        
        if expense_by_category:
            category_table = Table(show_header=True, header_style="bold magenta")
            category_table.add_column("Category", style="cyan")
            category_table.add_column("Amount", justify="right", style="yellow")
            category_table.add_column("% of Total", justify="right", style="blue")
            
            for cat_name, amount in sorted(expense_by_category.items(), key=lambda x: x[1], reverse=True):
                percentage = (amount / total_expenses * 100) if total_expenses > 0 else 0
                category_table.add_row(
                    cat_name,
                    f"${amount:,.2f}",
                    f"{percentage:.1f}%"
                )
            
            console.print(category_table)
    
    Prompt.ask("\n[dim]Press Enter to continue[/dim]")


# ============================================
# MAIN ENTRY POINT
# ============================================

def main():
    """Main entry point for the CLI application."""
    initialize_categories()
    
    try:
        main_menu()
    except KeyboardInterrupt:
        console.print("\n\n[yellow]Application interrupted. Goodbye! 👋[/yellow]")
    except Exception as e:
        console.print(f"\n[red]An error occurred: {e}[/red]")
        console.print("[dim]Please report this issue if it persists.[/dim]")


if __name__ == "__main__":
    main()
