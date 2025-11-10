# import sys
# from pathlib import Path

# # Add the project directory to Python path
# project_dir = Path(__file__).parent
# sys.path.insert(0, str(project_dir))

# Now import and run the CLI with absolute imports


from ui.login import main

if __name__ == "__main__":
    main()