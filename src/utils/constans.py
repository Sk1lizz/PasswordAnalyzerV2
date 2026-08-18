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


