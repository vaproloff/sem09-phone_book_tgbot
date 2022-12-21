from secrets import TG_TOKEN
from tg_server import *
from telegram.ext import ApplicationBuilder

app = ApplicationBuilder().token(TG_TOKEN).build()
app.add_handler(conv_handler)
app.run_polling()
