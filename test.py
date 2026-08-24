import re
import math

# Правильные константы
UPPERCASE = r'[A-ZА-Я]'
LOWERCASE = r'[a-zа-я]'
DIGITS = r'\d'
# ВАЖНО: экранируем все спецсимволы
SPECIAL = r'[!@#$%^&*()_+\-=\{\}\[\]:;"\'<>,.?/~`]'

def calculate_entropy_theoretical(password: str) -> float:
    """
    Теоретическая энтропия — максимально возможная энтропия,
    основанная на том, какие типы символов используются в пароле.
    """
    if not password:
        return 0.0
    
    alphabet_size = 0
    
    if re.search(UPPERCASE, password):
        alphabet_size += 26
        print("✅ Есть заглавные буквы (+26)")
    
    if re.search(LOWERCASE, password):
        alphabet_size += 26
        print("✅ Есть строчные буквы (+26)")
    
    if re.search(DIGITS, password):
        alphabet_size += 10
        print("✅ Есть цифры (+10)")
    
    # Используем экранированную версию
    if re.search(SPECIAL, password):
        alphabet_size += 32
        print("✅ Есть спецсимволы (+32)")
    
    if alphabet_size == 0:
        return 0.0
    
    entropy = len(password) * math.log2(alphabet_size)
    print(f"📊 Размер алфавита: {alphabet_size}")
    print(f"📊 Энтропия: {entropy:.2f} бит")
    
    return round(entropy, 2)

print(len("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~pas"))