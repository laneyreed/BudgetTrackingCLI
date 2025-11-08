from models.transaction import Transaction, TransactionType
from utils.constants import DEFAULT_EXPENSE_CATEGORIES, DEFAULT_INCOME_CATEGORIES
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt, FloatPrompt
from rich import box
from datetime import datetime

transactions = []
# ============================================
# TRANSACTION FUNCTIONS
# ============================================

def add_transaction(show_header, console, current_user, accounts, categories):
    """Add a new transaction."""
    show_header(console)
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


def view_transactions(show_header, console, current_user):
    """View all transactions for the current user."""
    show_header(console)
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


def view_summary(show_header, console, current_user, accounts):
    """Display financial summary for the current user."""
    show_header(console)
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
