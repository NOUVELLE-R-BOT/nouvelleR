from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7962971206:AAGnseTd-YWLej65aIWpt8ZW0R9HhJFw6bE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Image à envoyer (tu peux mettre une URL ou un fichier local)
    image_url = "https://example.com/ton_image.jpg"

    # Texte du message (tu peux utiliser du markdown ou html)
    texte = (
        "👋 Bienvenue chez MA DISCOUNT\n\n"
        "Tu viens d’entrer dans l’univers premium, rapide et discret de la French Riviera 🌊\n"
        "Ici, c’est qualité garantie, livraison express et vibes chill du 12h au 00h 🕐\n\n"
        "📍 Zone couverte : Toute la Côte d’Azur (06)\n"
        "📦 Menu photos, vidéos, prix & promos à jour"
    )

    # Boutons inline
    keyboard = [
        [InlineKeyboardButton("Informations ℹ️", callback_data='info')],
        [InlineKeyboardButton("Contact 📲", callback_data='contact')],
        [InlineKeyboardButton("Discount Menu", url='https://tonlien.com/menu')],
        [InlineKeyboardButton("Potato", url='https://potato.com')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Envoi de la photo avec la légende et les boutons
    await update.message.reply_photo(photo=image_url, caption=texte, reply_markup=reply_markup, parse_mode='HTML')


if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot lancé...")
    app.run_polling()
