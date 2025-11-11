# #=======================================================================
# # Configure import to work both when run directly and when imported
# #
# try:
#     # Relative import when running from main.py
#     from .layout import console, create_layout, update_layout
# except ImportError:
#     # Absolute import when running directly
#     from layout import console, create_layout, update_layout

from ui.layout import console, create_layout, update_layout

#===========================================================
# Main Function
#===========================================================
def main():
    """
    Main Application Starter
    """
    main_layout = create_layout()
    update_layout(main_layout)
    console.print(main_layout)

if __name__ == "__main__":
    main()


