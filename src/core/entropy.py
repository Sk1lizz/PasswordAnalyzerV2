import math
import re

from zxcvbn import zxcvbn

from src.utils.setting import (
    LOWERCASE,
    UPPERCASE,
    NUMBER,
    SPECIAL,
)

def calculate_entropy(password: str) -> float:
    if not password:
        return 0.0

    alphabet_size = len(set(password))

    entropy = len(password) * math.log2(alphabet_size)

    return round(entropy, 2)

def calculate_entropy_theoretical(password: str) -> float:
    if not password:
        return 0.0

    alphabet_size = 0

    if re.search(UPPERCASE, password):
        alphabet_size += len(UPPERCASE) - 2

    if re.search(LOWERCASE, password):
        alphabet_size += len(LOWERCASE) - 2

    if re.search(NUMBER, password):
        alphabet_size += len(NUMBER) - 2

    if re.search(SPECIAL, password):
        alphabet_size += len(SPECIAL) - 2

    entropy = len(password) * math.log2(alphabet_size)

    return entropy

def calculate_entropy_zxcvbn(password: str) -> dict:
    if not password:
        return {
            "entropy": 0.0,
            "score": 0,
            "crack_time": "мгновенно",
            "crack_time_seconds": 0,
            "warning": "Пароль пустой",
            "suggestions": ["Введите пароль"],
            "guesses": 0
        }

    result = zxcvbn(password=password)

    entropy = result.get("guesses_log10", 0) * math.log2(10)
    entropy = round(entropy, 2)

    score = result.get("score", 0)
    guesses = result.get("guesses", 0)

    crack_times = result.get("crack_times_display", {})
    crack_time = crack_times.get("offline_slow_hashing_1e4_per_second", "неизвестно")
    crack_time_seconds = result.get("crack_times_seconds", {}).get("offline_slow_hashing_1e4_per_second", 0)

    feedback = result.get("feedback", {})
    warning = feedback.get("warning", "")
    suggestions = feedback.get("suggestions", [])

    return {
        "entropy": entropy,
        "score": score,
        "crack_time": crack_time,
        "crack_time_seconds": float(crack_time_seconds) if crack_time_seconds else 0,
        "warning": warning,
        "suggestions": suggestions,
        "guesses": int(guesses) if guesses else 0,
        "raw_result": result
    }