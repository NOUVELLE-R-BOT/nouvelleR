// 1) Installer : npm init -y && npm i node-telegram-bot-api
// 2) Crée bot.js, colle ton token et ton URL, puis lance : node bot.js

const TelegramBot = require('node-telegram-bot-api');
const token = '7962971206:AAGnseTd-YWLej65aIWpt8ZW0R9HhJFw6bE';               // -> colle ton token BotFather ici
const bot = new TelegramBot(token, { polling: true });

bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, "Clique pour ouvrir la mini-app :", {
    reply_markup: {
      inline_keyboard: [[
        { text: "🚀 Ouvrir la mini-app", web_app: { url: "https://nouvelle-r-bot.github.io/nouvelleR/" } }
      ]]
    }
  });
});
