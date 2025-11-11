from rich.console import Console
from rich.theme import Theme
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich import box
from rich.align import Align

from ui.menu import create_menu
from ui.transactions import create_transaction_table
# ============================================
# Theme Definition
# ============================================
budget_theme = Theme({
    "header.text": "bold magenta",
    "info": "green",
    "text": "white",
    "accent": "#4c067a",
    "attention": "yellow",
})

console = Console(theme=budget_theme)
layout = Layout()

#===========================================================
# Header
#===========================================================
def create_header():
    """
    Creates Header Area
    """
    header_text = Text("💸 WELCOME TO BUDGET TRACKER CLI 💸", style="header.text", justify="center")
    header = Panel(header_text, box=box.DOUBLE, border_style="accent")
    return header


# #===========================================================
# # Sidebar Menu
# #===========================================================
# def create_sidebar():
#     """
#     Creates Sidebar Menu Area
#     """
#     menu_table = Table(
#         show_header=True,
#         header_style="bright",
#         box=box.ROUNDED,
#         border_style="attention",
#         show_lines=True,
#     )
#     menu_table.add_column("[bold]Option[/bold]", style="info", justify="center", width=8)
#     menu_table.add_column("[bold]Action[/bold]", style="info", justify="center")
    
#     menu_table.add_row("1", "Add Transaction")
#     menu_table.add_row("2", "View Transactions")
#     menu_table.add_row("3", "Add Account")
#     menu_table.add_row("4", "View Accounts")
#     menu_table.add_row("0", "Exit")
    
#     centered_table = Align.center(menu_table)

#     return Panel(centered_table, title="[bold]MENU[/bold]", border_style="attention",  box=box.DOUBLE)

#===========================================================
# Main Content
#===========================================================
def create_main_content():
    """
    Creates Main Content Area
    """

    transaction_table = create_transaction_table()
    content = Text("Budget Tracker Content", justify="center", style="text")
    main_content = Panel(
        Align.center(transaction_table, vertical="middle"),
        border_style="info",
        box=box.ROUNDED,
        title="[bold]Budget[/bold]"
    )
    return main_content


#===========================================================
# Layout
#===========================================================
def create_layout():
    """
    Creates Layout
    """
    layout = Layout()
    
    # Main split: header, body, footer
    layout.split(
        Layout(name="header", size=5),
        Layout(name="body", size=16),
        Layout(name="footer", size=3)
    )
    
    # Split body into sidebar and main content
    layout["body"].split_row(
        Layout(name="sidebar", size=55),
        Layout(name="main", ratio=1)
    )
    return layout


#===========================================================
# Update Layout
#===========================================================
def update_layout(layout):
    """
    Add Content to Layout 
    """

    # main_content = create_transaction_table()
    layout["header"].update(create_header())
    layout["sidebar"].update(create_menu())
    layout["main"].update(create_main_content())
#===========================================================


