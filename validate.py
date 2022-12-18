import re

# Функция валидации номера телефона
def check_phone(phone):
    if re.fullmatch('\+?[1-9]\d{6,14}', phone):
        return True
    return False