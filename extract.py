import view

# Функция поиска и вывода записи из телефонной книги
def find_data(data):
    with open('phone_book.csv', 'r') as book:
        data_found = []
        for line in book:
            for text in line.split(';'):
                if data.lower() in text.lower():
                    phone_record = line.split(';')
                    phone_record[0] = f'Имя: {phone_record[0]}'
                    phone_record[1] = f'Фамилия: {phone_record[1]}'
                    phone_record[2] = f'Телефон: {phone_record[2]}'
                    if len(phone_record) > 3:
                        phone_record[3] = f'Описание: {phone_record[3]}'
                    data_found.append(phone_record)
        view.show_ext_data(data_found)

# Функция выводит всю телефонную книгу
def full_output():
    with open('phone_book.csv', 'r') as book:
        data_found = []
        for line in book:
            data_found.append(line.replace(';', ', ').replace('\n', ''))
        view.show_data(data_found)