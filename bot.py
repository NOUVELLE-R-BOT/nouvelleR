from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Ton message d'accueil 
WELCOME_MESSAGE = """Bonjour et bienvenue chez ɴᴏᴜᴠᴇʟʟᴇ’ʀ 🌐

Nous allons vous répondre d’ici 15 minutes maximum 📱

Pour faciliter notre travail veuillez commencer à écrire votre commande :

Produit 🎁
Adresse 📍
Numéro de téléphone 📱 
Photo visage + Carte d’identité*🪪 
(Si première commande*)

Pour toute question nous restons à votre disposition

Ps: si vous envoyez un message après 0h il sera ouvert demain, horaires du standard : 11h-0h"""

# Clavier personnalisé
keyboard = [
    ["📋 Informations", "🧾 Menu ɴᴏᴜᴠᴇʟʟᴇ’ʀ 🌐"],
    ["🌐 Telegram", "🍟 Potato", "📦 Commande"]
]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Commande /start

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE, reply_markup=markup, parse_mode="Markdown")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # 1. Envoie une image d'accueil
    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://github.com/NOUVELLE-R-BOT/nouvelleR/blob/main/logo.png.jpg?raw=true"  # ou un lien direct vers une image hébergée
    )

    # 2. Envoie le message texte après l'image
    await context.bot.send_message(
        chat_id=chat_id,
        text=WELCOME_MESSAGE
    )


# Gestion des boutons
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "📋 Informations":
        await update.message.reply_text("ɴᴏᴜᴠᴇʟʟᴇ’ʀ 🌐")
        await update.message.reply_photo(
    photo=open("static/logo2.jpg", "rb"),
    caption="Nous bossons avec personne, équipe totalement indépendante qui vous propose un services rapide,sérieux et à l'écoute de la clientèle,disponible dans le 06 & 67 ses alentours(sur place / livraison)"
)

    elif text == "🧾 Menu ɴᴏᴜᴠᴇʟʟᴇ’ʀ 🌐":
        await update.message.reply_text("""
ɴᴏᴜᴠᴇʟʟᴇ’ʀ 🌐 Officiel

Qualité premium | Livraison rapide & discrète | Côte d’Azur 06/83 & Alsace 67/68 🇫🇷

Le 10/08/25

                                 Menu
———

HASH

🧽 Jaune Mousseux
LA SANTA MOUSSE 
Strain : forbiden fruit 🍇
 
 
3g - 20€
7g - 50€
10g - 70€
25g - 160€
50g - 280€
100g - 420€


———

Static⚡️
Static sift  (mountain giants) 
Yellow melon 🍑🍈

———

Frozen 🧊

Sour Diesel / Limosa / Panacotta 2.0

2,5g - 50€
5g - 80€
10g - 140€
25g - 260€

Rs 11 / Rs 11 x Exodus Cheese

2,5g - 50€
5g - 80€
10g - 160€
25g - 280€

Sec et pétant                    

———
                                   
WEED

Purpel Gummy 🍬

3,5g - 50€
7g - 100€
10,5g - 130€

White runtz 🥶

3,5g - 50€
7g - 100€
10,5g - 130€

Orange bud🍊 

3,5g - 50€
7g - 100€
10,5g - 130€

———                                        
                                        
COCO

❄️ NEIGE – PREMIUM

1g-60€

2g-110€

5g-250€

———                                        

🌈BUVARDS & TAZ

• L*D Buvards ❌
🌈5 pièces  → 50€
🌈10pièces → 80€

• Taz ❌ (Indisponible)
💊10 pièces → 50€
💊25 pièces → 100€

———
                                        
💥SYNTHÉTIQUES – CLEAN TESTÉ ✅

• Ket❌
💠 1g → 40€
💠 2g → 60€
💠 10g → 180€

• MD
💎 1g → 40€
💎 2g → 60€
💎 10g → 180€

• 3M ❌ (Indisponible)
🧪 1g → 40€
🧪 2g → 60€
🧪 10g → 180€

⸻

🚚Livraison & Envoi

📍06/83 Côte d’Azur → Gratuite dès 50€ ✅
📍67/68 Alsace → Gratuite dès 50€ ✅
📦Expédition France → Discrète & sécurisée ✉️

Suivi dispo

Paiement à la livraison 🚚

Espèce seulement 💶

⸻

🎁OFFRE DE BIENVENUE

🛍️ +1g offert pour chaque achat ! 🎉

📲📲📲📲📲📲
🤖
@NouvelleR_bot""")

    elif text == "🌐 Telegram":
        await update.message.reply_text("https://t.me/+fSQ_5R5A_wIzYWY0")
    elif text == "🍟 Potato":
        await update.message.reply_text("https://dym168.org/nouveller")
    elif text == "📦 Commande":
        await update.message.reply_text("Merci d’envoyer votre commande en message ou note vocale."
        "                                                                                          " \
        "@zzluxur ✅ Livraison rapide, discrète sur la Côte d’Azur (06)"
        "                                                                                          " \
        "@jackysparo ✅ Livraison rapide, discrète sur Strasbourg (67)")
    else:
        await update.message.reply_text("Choisis une option ci-dessus ⬆️")

# Lancer le bot
app = ApplicationBuilder().token("7962971206:AAGnseTd-YWLej65aIWpt8ZW0R9HhJFw6bE").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("✅ Bot lancé...")

app.run_polling()
