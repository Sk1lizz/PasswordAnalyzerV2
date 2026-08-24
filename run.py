from src.core.entropy import calculate_entropy_theoretical
from src.core.entropy import calculate_entropy_zxcvbn
from src.core.checked import checked

result = checked("password1SAL!123123123")

print(result["score"])
print()
print()
print(result["result"])