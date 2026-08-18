import sys 
import os
from pathlib import Path

def get_base_path() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS)

    else:
        return Path(__file__).parent.parent.parent

def get_resources_path(reletive_path: str) -> Path:
    return get_base_path() / "resources" / reletive_path

def get_logs_path() -> Path:
    if not getattr(sys, "frozen", False):
        path = Path(__file__).parent.parent.parent / ".logs"
        path.mkdir(exist_ok=True)

        return path
