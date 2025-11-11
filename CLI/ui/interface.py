from rich.console import Console
from rich.theme import Theme
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich import box
from rich.align import Align

from ui.menu import create_menu
from ui.expenses import create_expense_table
from ui.income import create_income_table
from ui.month_overview import create_month_overview_table

# only needed to run files directly from the ui/ directory
# #========================================================================
# try:
#     # When running from parent directory (via main.py)
#     from ui.menu import create_menu
#     from ui.expenses import create_expense_table
#     from ui.income import create_income_table
#     from ui.month_overview import create_month_overview_table
# except ImportError:
#     # When running directly from ui directory
#     from menu import create_menu
#     from expenses import create_expense_table
#     from income import create_income_table
#     from month_overview import create_month_overview_table
# #========================================================================


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


#===========================================================
# Main Content
#===========================================================
def create_main_content():
    """
    Creates Main Content Area
    """

    expense_table = create_expense_table()
    income_table = create_income_table()
    
    # Create a layout to hold both panels
    content_layout = Layout()
    content_layout.split_row(
        Layout(name="income"),
        Layout(name="expense")
    )
    
    main_income_content = income_table
    
    main_expense_content = expense_table
    
    content_layout["income"].update(main_income_content)
    content_layout["expense"].update(main_expense_content)
    
    return content_layout


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
        Layout(name="footer", size=16)
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
    layout["footer"].update(create_month_overview_table())
#===========================================================


def main():
    """
    Test Layout Rendering
    """
    main_layout = create_layout()
    update_layout(main_layout)
    console.print(main_layout)


if __name__ == "__main__":
    main()

