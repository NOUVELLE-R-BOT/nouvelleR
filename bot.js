// 1️⃣ Installer les dépendances :
// npm init -y
// npm install node-telegram-bot-api

const TelegramBot = require('node-telegram-bot-api');
const token = '7962971206:AAGnseTd-YWLej65aIWpt8ZW0R9HhJFw6bE'; // Mets ici ton token BotFather
const bot = new TelegramBot(token, { polling: true });

bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;

  bot.sendMessage(
    chatId,
    "📍 Zone couverte : Toute la Côte d’Azur (06)\n📦 Menu photos, vidéos, prix & promos à jour",
    {
      reply_markup: {
        inline_keyboard: [
          [
            { text: "Informations ℹ️", callback_data: "infos" },
            { text: "Contact 📱", callback_data: "contact" }
          ],
          [
            { text: "MaDrugs Discount Menu", url: "https://tonlien.com" } // lien externe
          ],
          [
            { text: "Potato 🥔", web_app: { url: "https://tonlien-miniapp.com" } } // lien mini-app
          ]
        ]
      }
    }
  );
});

// Gestion des clics sur les boutons avec callback_data
bot.on("callback_query", (query) => {
  const chatId = query.message.chat.id;

  if (query.data === "infos") {
    bot.sendMessage(chatId, "ℹ️ Voici toutes les informations utiles...");
  }

  if (query.data === "contact") {
    bot.sendMessage(chatId, "📞 Contactez-nous au : +33 6 00 00 00 00");
  }
});
