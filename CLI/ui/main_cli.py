from layout import console, create_layout, update_layout

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


