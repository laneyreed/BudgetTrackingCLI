from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich import box
from rich.align import Align
from rich.table import Table

console = Console()
layout = Layout()

def create_layout():
    #===============================================================
    # Define the overall layout structure
    #===============================================================
    layout.split(
        Layout(name="header", size=3),
        Layout(ratio=1, name="main"),
        Layout(size=10, name="footer"),
    )

    layout["main"].split_row(Layout(name="side_menu"), Layout(name="body", ratio=3))

    #================================================================
    # Appplication Header   
    #================================================================
    header_text = Text("💰 WELCOME TO BUDGET TRACKER CLI 💰", justify="center")
    header = Panel(header_text, box=box.DOUBLE)
    layout["header"].update(header)


def update_body():
    layout["body"].update(
        Align.center(
            Text(
                """This is a demonstration of rich.Layout\n\nHit Ctrl+C to exit""",
                justify="left",
            ),

        )
    )


def create_menu_table():
    menu_table = Table( title="MENU", show_lines=True)
    menu_table.add_column("Description")
    menu_table.add_column("Option")
    return menu_table


def update_menu():
    #================================================================
    # USER MENU SECTION
    #================================================================
    menu = create_menu_table()
    menu.add_row("EXISTING USER", "1")
    menu.add_row("NEW USER", "2")
    layout["side_menu"].update(menu)


def main():
    create_layout()
    update_body()
    update_menu()
    console.print(layout)

main()


