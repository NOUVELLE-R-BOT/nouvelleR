const TelegramBot = require('node-telegram-bot-api');
const token = '7962971206:AAGnseTd-YWLej65aIWpt8ZW0R9HhJFw6bE';
const bot = new TelegramBot(token, { polling: true });

bot.onText(/\/start/, (msg) => {
  bot.sendMessage(msg.chat.id, "📍 Zone couverte : Toute la Côte d’Azur (06)\n📦 Menu photos, vidéos, prix & promos à jour", {
    reply_markup: {
      inline_keyboard: [
        [
          { text: "Informations ℹ️", callback_data: "infos" },
          { text: "Contact 📱", callback_data: "@zzluxur" }
        ],
        [
          { text: "MaDrugs Discount Menu", url: "https://tonlien.com" }
        ],
        [
          { text: "Potato 🥔", web_app: { url: "https://tonlien-miniapp.com" } }
        ]
      ]
    }
  });
});

bot.on("callback_query", (query) => {
  const chatId = query.message.chat.id;

  if (query.data === "infos") {
    bot.sendMessage(chatId, "Voici les informations 📄 ...");
  }

  if (query.data === "contact") {
    bot.sendMessage(chatId, "📞 Contactez-nous au : +33 6 00 00 00 00");
  }
});
