import extract
import add_to_db
import validate
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def add_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # phone_record = [input('Введите имя: ').title(), input('Введите фамилию: ').title()]
    # phone = ''
    # while not validate.check_phone(phone):
    #     phone = input('Введите номер телефона: ')
    #     if not validate.check_phone(phone):
    #         print('Телефон введен неверно. Попробуйте снова.')
    # phone_record.append(phone)
    # description = input('Введите описание: ')
    # if description:
    #     phone_record.append(description)
    # print(f'Запись внесена в книгу: {str.join(", ", phone_record)}')
    # return phone_record

    await update.message.reply_text(f'Укажите имя:')


async def show_book(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phone_book = extract.full_output()
    output = f'Найдено записей: {len(phone_book)}\n---\n'
    for line in phone_book:
        output += line + '\n'
    await update.message.reply_text(output)


async def find_record(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data_to_search = str.join('', update.message.text.split()[1::])
    print(data_to_search)
    data_found = extract.find_data(data_to_search)
    output = f'Найдено записей: {len(data_found)}\n---\n'
    for line in data_found:
        for text in line:
            output += text + '\n'
    await update.message.reply_text(output)


async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/add\n/show\n/find\n/menu')
