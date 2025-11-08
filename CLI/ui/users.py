from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from models.user import User
from ui.accounts import manage_accounts_menu

# In-memory storage (in a real app, this would be a database)
users = []
current_user = None

# ============================================
# USER MANAGEMENT FUNCTIONS
# ============================================

def user_management_menu(show_header, console):
    """Handle user creation and selection."""
    global current_user
    
    show_header(console)
    
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
        return create_user(show_header, console)
    elif action == "select":
        return select_user(show_header, console)


def create_user(show_header, console):
    """Create a new user."""
    global current_user
    
    show_header(console)
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
    return current_user

def select_user(show_header, console):
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
            # show  manage_accounts_menu(show_header, console)
            manage_accounts_menu(show_header, console, current_user)
            return
    
    console.print("[red]User not found![/red]")
    Prompt.ask("\n[dim]Press Enter to continue[/dim]")
    return current_user
