from telegram import Update, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7962971206:AAGnseTd-YWLej65aIWpt8ZW0R9HhJFw6bE"  # Remplace par ton token donné par @BotFather

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bienvenue ! Clique ci-dessous pour accéder au menu 👇",
        reply_markup=update.message.reply_markup.from_web_app(WebAppInfo(url="https://TON_DOMAINE/index"))
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot lancé...")
app.run_polling()
