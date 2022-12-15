# Руслан
# Модуль поиска данных из БД
import view

def find_data(data):

    view.show_data('Иванов Иван +7987654321')

def full_output():
    with open('phone_book.csv', 'r') as book:
        for line in book:
            view.show_data(line)