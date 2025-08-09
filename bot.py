from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Ton message d'accueil
WELCOME_MESSAGE = """👋 Bienvenue chez *Ma Coffee Discount* – COFFEE DELIVERY 06 🌴❄️

Tu viens d’entrer dans l’univers premium, rapide et discret de la French Riviera 🌊
Ici, c’est qualité garantie, livraison express et vibes chill de 12h au 00h 🕐
📍 Zone couverte : Toute la Côte d’Azur (06)
📸 Menu photos, vidéos, prix & promos à jour
"""

# Clavier personnalisé
keyboard = [
    ["📋 Informations", "🧾 Discount Menu"],
    ["🍟 Potato", "📦 Commande"]
]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE, reply_markup=markup, parse_mode="Markdown")

# Gestion des boutons
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📋 Informations":
        await update.message.reply_text("✅ Livraison rapide, discrète sur la Côte d’Azur (06)")
    elif text == "🧾 Discount Menu":
        await update.message.reply_text("Voici notre menu :\n📸 Photos + Prix : [à insérer]")
    elif text == "🍟 Potato":
        await update.message.reply_text("Patate spéciale du chef 🥔🔥")
    elif text == "📦 Commande":
        await update.message.reply_text("Merci d’envoyer votre commande en message ou note vocale.")
    else:
        await update.message.reply_text("Choisis une option ci-dessus ⬆️")

# Lancer le bot
app = ApplicationBuilder().token("7962971206:AAGnseTd-YWLej65aIWpt8ZW0R9HhJFw6bE").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("🤖 Bot lancé...")

app.run_polling()
