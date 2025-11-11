from rich.table import Table
from rich import box
from rich.panel import Panel
from rich.align import Align


def create_income_table():
    """
    Creates Income Table
    """
    main_income_table = Table(title="Income History", title_style="title", box=box.ROUNDED)
    main_income_table.add_column("ID", style="dim")
    main_income_table.add_column("Description", style="green")
    main_income_table.add_column("Amount", justify="right")
    main_income_table.add_column("Type")

    main_income_table.add_row("001", "Salary", "$5,000", "Income")
    main_income_table.add_row("002", "Freelance", "$1,200", "Income")
    main_income_table.add_row("003", "Investments", "$300", "Income")
    main_income_table.add_row("004", "Gifts", "$150", "Income")
    main_income_table.add_row("005", "Other Income", "$250", "Income")

    main_income_content = Panel(
        Align.center(main_income_table, vertical="middle"),
        border_style="info",
        box=box.ROUNDED,
        title="[bold]Income[/bold]"
    )
    return main_income_content