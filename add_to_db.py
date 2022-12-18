# Функция добавления записи в базу в txt
def add_to_txt(data):
    with open('phone_book.txt', 'a') as book:
        data_str = (f'Имя: {data[0]}\nФамилия: {data[1]}\n'
                   f'Номер телефона: {data[2]}\nОписание: {data[3]}\n\n')
        book.write(data_str)

# Функция добавления записи в базу в csv
def add_to_csv(data):
    with open('phone_book.csv', 'a') as book:
        data_str = str.join(';', data) + '\n'
        book.write(data_str)
