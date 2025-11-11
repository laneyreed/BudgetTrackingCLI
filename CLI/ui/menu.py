


#===========================================================
# Sidebar Menu
#===========================================================
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich import box


def create_menu():
    """
    Creates Sidebar Menu Area
    """
    menu_table = Table(
        show_header=True,
        header_style="bright",
        box=box.ROUNDED,
        border_style="attention",
        show_lines=True,
    )
    menu_table.add_column("[bold]Option[/bold]", style="info", justify="center", width=8)
    menu_table.add_column("[bold]Action[/bold]", style="info", justify="center")
    
    menu_table.add_row("1", "Add Transaction")
    menu_table.add_row("2", "View Transactions")
    menu_table.add_row("3", "Add Account")
    menu_table.add_row("4", "View Accounts")
    menu_table.add_row("0", "Exit")
    
    centered_table = Align.center(menu_table)

    return Panel(centered_table, title="[bold]MENU[/bold]", border_style="attention",  box=box.DOUBLE)