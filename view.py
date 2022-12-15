# Сергей
import validate

def main_menu():
    print('Вас приветствует телефонный справочник')
    print('Главное меню')
    mode = input('1. Записать данные в книгу\n2. Показать всю книгу\n3. Поиск по фамилии\n4. Выход\nВведите 1, 2, 3 и 4: ')
    if mode in '1234':
        return int(mode)
    else:
        print('Ошибка! Введите 1, 2, 3 или 4!')

def write_data():
    # Функция ввода данных от пользователя
    phone_record = [input('Введите фамилию: ').title(), input('Введите имя: ').title()]
    phone = ''
    while not validate.check_phone(phone):
        phone = input('Введите телефон: ')
        if not validate.check_phone(phone):
            print('Телефон введен неверно. Попробуйте снова.')
    phone_record.append(phone)
    return phone_record

def search_data():
    return input('Введите фамилию: ').title()

def show_data(data):
    print(data)
