import sys 
import os
from pathlib import Path

from src.utils.constans import (
    CONFIG_FILE,
    SETTING_FILE,
)

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

def get_config_path() -> Path:
    return get_resources_path(f"config/{CONFIG_FILE}")

def get_setting_path() -> Path:
    return get_resources_path(f"config/{SETTING_FILE}")