import json
from pathlib import Path

from src.utils.paths import get_config_path
from src.utils.constans import (
    APP_NAME as _name,
    APP_VERSION as _version,
    APP_AUTHOR as _author,
    APP_YEAR as _year,
    APP_URL as _url,

    LOG_CONSOLE_LEVEL as _console_level,
    LOG_FILE_LEVEL as _file_level,
    LOG_FORMAT as _format,
    LOG_DATE_FORMAT as _date_format,
    LOG_FILE as _file,
    LOG_MAX_BYTES as _bytes,
    LOG_BACKUP_COUNT as _log_backup,
    DEFAULT_LANGUAGE as _lang,
    CONFIG_FILE as _cfg,
    SETTING_FILE as _setting,
)

def get_data(path: Path) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as file:
            config_data = json.load(file)

    except:
        config_data = {}

    return config_data

data = get_data(path=get_config_path())

try: 
    data_app = data["APP_SETTING"]

    _ = data_app["Name"]
    _ = data_app["Version"]
    _ = data_app["Year"]

except:
    data_app = {
        "Name": _name,
        "Version": _version,
        "Year": _year,
    }

APP_NAME = data_app["Name"]
APP_VERSION = data_app["Version"]
APP_YEAR = data_app["Year"]
APP_AUTHOR = _author
APP_URL = _url

try:
    data_logs = data["LOGS"]

    _ = data_logs["Console_Level"]
    _ = data_logs["File_Level"]
    _ = data_logs["Format"]
    _ = data_logs["Date_Format"]
    _ = data_logs["File"]
    _ = data_logs["Backup_Count"]

    _max_bytes = 1

    for _symbol in data_logs["Max_Bytes"].split(" * "):
        _max_bytes *= int(_symbol)


except:
    data_logs = {
        "Console_Level": _console_level,
        "File_Level": _file_level,
        "Format": _format,
        "Date_Format": _date_format,
        "File": _file,
        "Backup_Count": _log_backup,
    }

    _max_bytes = _bytes

LOG_CONSOLE_LEVEL = data_logs["Console_Level"]
LOG_FILE_LEVEL = data_logs["File_Level"]
LOG_FORMAT = data_logs["Format"]
LOG_DATE_FORMAT = data_logs["Date_Format"]
LOG_FILE = data_logs["File"]
LOG_MAX_BYTES = _max_bytes
LOG_BACKUP_COUNT = data_logs["Backup_Count"]

try: 
    DEFAULT_LANGUAGE = data["Default_Language"]
except:
    DEFAULT_LANGUAGE = _lang

CONFIG_FILE = _cfg
SETTING_FILE = _setting