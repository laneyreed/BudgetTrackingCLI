from rich.console import Console
from rich.theme import Theme
from ui.interface import main_menu, otherErrorMessage, keyboardInterruptMessage
from ui.categories import initialize_categories


# ============================================
# MAIN ENTRY POINT
# ============================================

def main():
    """Main entry point for the CLI application."""
    categories =initialize_categories()
    
    try:
        main_menu(categories)
    except KeyboardInterrupt:
        keyboardInterruptMessage
    except Exception as e:
        otherErrorMessage(e)

if __name__ == "__main__":
    main()