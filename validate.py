import re

# Функция валидации номера телефона
def check_phone(phone):
    if re.fullmatch('(?:\+7|8)\d{10}', phone):
        return True
    return False