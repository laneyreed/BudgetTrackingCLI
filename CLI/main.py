import sys
from pathlib import Path


project_dir = Path(__file__).parent

sys.path.insert(0, str(project_dir))

from ui.main_cli import main

if __name__ == "__main__":
    main()