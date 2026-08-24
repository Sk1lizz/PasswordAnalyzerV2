# src/utils/constans.py

""" Файл с константами проекта """



# ===============================
# Приложение
# ===============================

APP_NAME = "PasswordAnalyzerV2"
APP_VERSION = "2.0.0"
APP_AUTHOR = [
    "sk1lizz",
]

APP_YEAR = "2026"
APP_URL = "https://github.com/Sk1lizz/PasswordAnalyzerV2"



# ===============================
# Настройки логирования
# ===============================

LOG_CONSOLE_LEVEL = 20
LOG_FILE_LEVEL = 10

LOG_FORMAT = "[%(levelname)s] %(asctime)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

LOG_FILE = "passwordanalyzer.log"

LOG_MAX_BYTES = 10 * 1024 * 1024
LOG_BACKUP_COUNT = 10           # На релизе изменить на 3/5. Во время тестов можно увеличить до 10.


# ===============================
# Настройки по умолчанию
# ===============================

DEFAULT_LANGUAGE = "ru-RU"
CONFIG_FILE = "config.json"
SETTING_FILE = "setting.json"


DEFAULT_SETTING = {
    "analyzer": {
        "lowercase_letter": "abcdefghijklmnopqrstuvwxyz",
        "uppercase_letter": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "number": "0123456789",
        "special": "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~",

        "rules": {
            "symbol": {
                "enable": True,
                "min": 8,
                "better": 16
            },

            "lowercase_letter": {
                "enable": True,
                "list_symbol": "abcdefghijklmnopqrstuvwxyz"
            },

            "uppercase_letter": {
                "enable": True,
                "list_symbol": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            },

            "number": {
                "enable": True,
                "list_symbol": "0123456789"
            },

            "special": {
                "enable": True,
                "list_symbol": "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
            },

            "entropy": {
                "enable": True
            }
        }
    },
}