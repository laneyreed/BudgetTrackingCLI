from rich.table import Table
from rich import box
from rich.panel import Panel
from rich.align import Align



def create_expense_table():
    """
    Creates Expense Table
    """
    main_expense_table = Table(title="Expense History", title_style="title", box=box.ROUNDED)
    main_expense_table.add_column("ID", style="dim")
    main_expense_table.add_column("Description", style="green")
    main_expense_table.add_column("Amount", justify="right")
    main_expense_table.add_column("Type")

    main_expense_table.add_row("001", "Rent", "$3,000", "Expense")
    main_expense_table.add_row("002", "Entertainment", "$200", "Expense")
    main_expense_table.add_row("003", "Groceries", "$500", "Expense")
    main_expense_table.add_row("004", "Utility Bills", "$386", "Expense")
    main_expense_table.add_row("005", "Insurance", "$300", "Expense")

    main_expense_content = Panel(
        Align.center(main_expense_table, vertical="middle"),
        border_style="info",
        box=box.ROUNDED,
        title="[bold]Expenses[/bold]"
    )
    return main_expense_content