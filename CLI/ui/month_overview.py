from rich.table import Table
from rich import box
from rich.panel import Panel
from rich.align import Align


#===========================================================
# Footer
#===========================================================
def create_month_overview_table():
    """
    Creates Month Overview Table
    """
    main_monthoverview_table = Table(title="Month Overview", title_style="title", box=box.ROUNDED)
    main_monthoverview_table.add_column("ID", style="dim")
    main_monthoverview_table.add_column("Description", style="green")
    main_monthoverview_table.add_column("Amount", justify="right")
    main_monthoverview_table.add_column("Type")

    main_monthoverview_table.add_row("001", "Salary", "$5,000", "Income")
    main_monthoverview_table.add_row("002", "Freelance", "$1,200", "Income")
    main_monthoverview_table.add_row("003", "Investments", "$300", "Income")
    main_monthoverview_table.add_row("004", "Gifts", "$150", "Income")
    main_monthoverview_table.add_row("005", "Other Income", "$250", "Income")

    footer_overview_content = Panel(
        Align.center(main_monthoverview_table, vertical="middle"),
        border_style="info",
        box=box.ROUNDED,
        title="[bold]Month Overview[/bold]"
    )
    return footer_overview_content