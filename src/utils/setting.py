import json
from pathlib import Path

from src.utils.paths import get_setting_path
from src.utils.constans import DEFAULT_SETTING

def get_data(path: Path) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

    except:
        data = {}

    return data

data = get_data(path=get_setting_path())

try:
    data_analyzer = data["analyzer"]

    _ = data_analyzer["lowercase_letter"]
    _ = data_analyzer["uppercase_letter"]
    _ = data_analyzer["number"]

except:
    data_analyzer = DEFAULT_SETTING["analyzer"]

LOWERCASE = f"[{data_analyzer["lowercase_letter"]}]"
UPPERCASE = f"[{data_analyzer["uppercase_letter"]}]"
NUMBER = f"[{data_analyzer["number"]}]"
SPECIAL = f'[{data_analyzer["special"]}]'

try: 
    data_rules = data_analyzer["rules"]

except:
    data_rules = DEFAULT_SETTING["analyzer"]["rules"]

data_symbol = data_rules["symbol"]
data_lowercase = data_rules["lowercase_letter"]
data_uppercase = data_rules["uppercase_letter"]
data_number = data_rules["number"]
data_special = data_rules["special"]
data_entropy = data_rules["entropy"]

SYMBOL_RULES = {
    "enable": data_symbol["enable"],
    "min_symbol": data_symbol["min"],
    "better_symbol": data_symbol["better"]
}

LOWERCASE_RULES = {
    "enable": data_lowercase["enable"],
    "symbols": f"[{data_lowercase["list_symbol"]}]"
}

UPPERCASE_RULES = {
    "enable": data_uppercase["enable"],
    "symbols": f"[{data_uppercase["list_symbol"]}]"
}

NUMBER_RULES = {
    "enable": data_number["enable"],
    "symbols": f"[{data_number["list_symbol"]}]"
}

SPECIAL_RULES = {
    "enable": data_special["enable"],
    "symbols": f"[{data_special["list_symbol"]}]"
}

ENTROPY_RULES = {
    "enable": data_entropy["enable"]
}