import view

# Функция поиска и вывода записи из телефонной книги
def find_data(data):
    with open('phone_book.csv', 'r') as book:
        data_found = []
        for line in book:
            for text in line.split(';'):
                if data.lower() in text.lower():
                    data_found.append(line.replace(';', ', ').replace('\n', ''))
        view.show_data(data_found)

# Функция выводит всю телефонную книгу
def full_output():
    with open('phone_book.csv', 'r') as book:
        data_found = []
        for line in book:
            data_found.append(line.replace(';', ', ').replace('\n', ''))
        view.show_data(data_found)