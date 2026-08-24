import re

from src.utils.setting import (
    UPPERCASE_RULES, 
    LOWERCASE_RULES,
    NUMBER_RULES,
    SPECIAL_RULES,
    SYMBOL_RULES,
)

def checked(password: str) -> dict:
    if not password:
        return {
            "password": None,
            "score": 0
        }

    score = 0
    result = {
        "symbol_len": {
            "enable": True,
            "min": False,
            "better": False
        },

        "upper": {
            "enable": True,
            "result": False
        },

        "lower": {
            "enable": True,
            "result": False
        },

        "number": {
            "enable": True,
            "result": False
        },

        "special": {
            "enable": True,
            "result": False
        }
    }

    if SYMBOL_RULES["enable"]:
        if len(password) >= SYMBOL_RULES["min_symbol"]:
            score += 10
            result["symbol_len"]["min"] = True

            if len(password) >= SYMBOL_RULES["better_symbol"]:
                score += 15
                result["symbol_len"]["better"] = True


    else:
        result["symbol_len"]["enable"] = False
        score += 25

    if UPPERCASE_RULES["enable"]:
        if re.search(UPPERCASE_RULES["symbols"], password):
            score += 15
            result["upper"]["result"] = True

    else:
        result["upper"]["enable"] = False
        score += 15


    if LOWERCASE_RULES["enable"]:
        if re.search(LOWERCASE_RULES["symbols"], password):
            score += 15
            result["lower"]["result"] = True
    
    else:
        result["lower"]["enable"] = False
        score += 15


    if NUMBER_RULES["enable"]:
        if re.search(NUMBER_RULES["symbols"], password):
            score += 20
            result["number"]["result"] = True

    else:
        result["number"]["enable"] = False
        score += 20


    if SPECIAL_RULES["enable"]:
        if re.search(SPECIAL_RULES["symbols"], password):
            score += 25
            result["special"]["result"] = True

    else:
        result["special"]["enable"] = False
        score += 25

    print(len(password))

    return {
        "password": password,
        "score": score,
        "len_password": len(password),
        "result": result
    }