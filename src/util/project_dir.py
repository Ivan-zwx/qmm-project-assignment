import os
from pathlib import Path


def get_project_dir() -> str:
    return str(Path(__file__).parent.parent.parent) + os.path.sep
