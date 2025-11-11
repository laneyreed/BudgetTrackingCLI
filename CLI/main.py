import sys
from pathlib import Path

#========================================================================
# adds the CLI directory to Python's search path so that 
# `from ui.interface import main` works correctly
# ensures Python can find the ui package 
# when running from this file(main.py) directly
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))
#========================================================================

from ui.interface import main

if __name__ == "__main__":
    main()