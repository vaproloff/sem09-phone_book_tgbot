import time
import validate

# Функция главного меню
def main_menu():
    print('---')
    time.sleep(1)
    print('Главное меню')
    mode = input('1. Записать данные в книгу\n2. Показать всю книгу\n3. Поиск записи\n4. Выход\nВведите 1, 2, 3 и 4: ')
    if mode in '1234':
        print('---')
        return int(mode)
    else:
        print('Ошибка! Введите 1, 2, 3 или 4!')

# Функция ввода данных от пользователя для записи в телефонную книгу
def write_data():
    phone_record = [input('Введите имя: ').title(), input('Введите фамилию: ').title()]
    phone = ''
    while not validate.check_phone(phone):
        phone = input('Введите номер телефона: ')
        if not validate.check_phone(phone):
            print('Телефон введен неверно. Попробуйте снова.')
    phone_record.append(phone)
    comment = input('Введите комментарий: ')
    if comment:
        phone_record.append(comment)
    print(f'Запись внесена в книгу: {str.join(", ", phone_record)}')
    return phone_record


# Функция ввода данных от пользователя для поиска
def search_data():
    return input('Введите текст или номер для поиска: ')

# Функция вывода записи телефонной книги в консоль
def show_data(data):
    print(f'Найдено записей: {len(data)}')
    for line in data:
        print(line)
