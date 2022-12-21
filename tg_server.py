import db_interact
import validate
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters

PRESS_MENU_BUTTON, INPUT_NEW_DATA, INPUT_SEARCH_DATA = range(3)

menu_keyboard = [
    ["Добавить новую запись", "Поиск"],
    ["Показать всё", "Выход"]
]
markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True)


async def start(update: Update, _):
    await update.message.reply_text(
        "Главное меню",
        reply_markup=markup,
    )
    return PRESS_MENU_BUTTON


async def add_new_record(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['queue'] = ['name', 'surname', 'phone', 'description']
    await update.message.reply_text(f"Добавление новой записи."
                                    f"\nВведите имя")
    return INPUT_NEW_DATA


async def receive_new_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = context.user_data
    text = update.message.text
    if user_data['queue'][0] == 'phone' and not validate.check_phone(text):
        await update.message.reply_text('Телефон введен некорректно. Попробуйте снова')
        return INPUT_NEW_DATA
    else:
        category = user_data['queue'].pop(0)
        user_data[category] = text
        if len(user_data['queue']):
            match user_data['queue'][0]:
                case 'surname':
                    await update.message.reply_text('Введите фамилию')
                case 'phone':
                    await update.message.reply_text('Введите телефон')
                case 'description':
                    await update.message.reply_text('Введите описание')
            return INPUT_NEW_DATA
        else:
            del user_data['queue']
            db_interact.add_to_csv([user_data['name'],
                                    user_data['surname'],
                                    user_data['phone'],
                                    user_data['description']])
            await update.message.reply_text('Запись добавлена:\n'
                                            f'Имя: {user_data["name"]}\n'
                                            f'Фамилия: {user_data["surname"]}\n'
                                            f'Телефон: {user_data["phone"]}\n'
                                            f'Описание: {user_data["description"]}')
            del user_data['name']
            del user_data['surname']
            del user_data['phone']
            del user_data['description']
            await update.message.reply_text('Главное меню', reply_markup=markup)
            return PRESS_MENU_BUTTON


async def show_phone_book(update: Update, _):
    phone_book = db_interact.full_output()
    output = f'Найдено записей: {len(phone_book)}\n---\n'
    for line in phone_book:
        output += line + '\n'
    await update.message.reply_text(output)
    await update.message.reply_text('Главное меню', reply_markup=markup)
    return PRESS_MENU_BUTTON


async def search_record(update: Update, _):
    await update.message.reply_text('Введите данные для поиска')
    return INPUT_SEARCH_DATA


async def receive_search_data(update: Update, _):
    data_to_search = str.join('', update.message.text)
    data_found = db_interact.find_data(data_to_search)
    output = f'Найдено записей: {len(data_found)}\n---\n'
    for line in data_found:
        for text in line:
            output += text + '\n'
    await update.message.reply_text(output)
    await update.message.reply_text('Главное меню', reply_markup=markup)
    return PRESS_MENU_BUTTON


async def done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data = context.user_data
    if "choice" in user_data:
        del user_data["choice"]

    await update.message.reply_text('Для запуска нажмите /start',
                                    reply_markup=ReplyKeyboardRemove())
    user_data.clear()
    return ConversationHandler.END


conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        PRESS_MENU_BUTTON: [
            MessageHandler(filters.Regex("^Добавить новую запись$"), add_new_record),
            MessageHandler(filters.Regex("^Показать всё$"), show_phone_book),
            MessageHandler(filters.Regex("^Поиск$"), search_record),
        ],
        INPUT_NEW_DATA: [
            MessageHandler(
                filters.TEXT & ~(filters.COMMAND | filters.Regex("^Выход$")),
                receive_new_data,
            )
        ],
        INPUT_SEARCH_DATA: [
            MessageHandler(
                filters.TEXT & ~(filters.COMMAND | filters.Regex("^Выход$")),
                receive_search_data,
            )
        ],
    },
    fallbacks=[MessageHandler(filters.Regex("^Выход$"), done)],
)
