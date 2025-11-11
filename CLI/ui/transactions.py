from rich.table import Table
from rich import box

def create_transaction_table():
    """
    Creates Transaction Table
    """
    table = Table(title="Transaction History", title_style="title", box=box.ROUNDED)
    table.add_column("ID", style="dim")
    table.add_column("Description", style="green")
    table.add_column("Amount", justify="right")
    table.add_column("Type")

    table.add_row("001", "Salary Payment", "[income]$5,000[/income]", "[success]Income[/success]")
    table.add_row("002", "Rent", "[expense]$1,500[/expense]", "[error]Expense[/error]")
    table.add_row("003", "Groceries", "[expense]$300[/expense]", "[error]Expense[/error]")
    table.add_row("004", "Freelance Work", "[income]$800[/income]", "[success]Income[/success]")
    return table