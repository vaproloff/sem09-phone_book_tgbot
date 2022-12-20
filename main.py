from secrets import TG_TOKEN
from tg_server import *

app = ApplicationBuilder().token(TG_TOKEN).build()

app.add_handler(CommandHandler("add", add_phone))
app.add_handler(CommandHandler("show", show_book))
app.add_handler(CommandHandler("find", find_record))
app.add_handler(CommandHandler("menu", main_menu))

app.run_polling()
