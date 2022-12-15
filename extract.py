import view

# Функция поиска и вывода записи из телефонной книги
def find_data(data):
    with open('phone_book.csv', 'r') as book:
        for line in book:
            if data.title() in line.split(';'):
                view.show_data(line)

# Функция выводит всю телефонную книгу
def full_output():
    with open('phone_book.csv', 'r') as book:
        for line in book:
            view.show_data(line)