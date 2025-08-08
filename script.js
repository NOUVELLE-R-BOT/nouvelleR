let tg = window.Telegram.WebApp;
tg.expand();

function envoyer() {
  tg.sendData("Hello depuis la mini-app !");
}
