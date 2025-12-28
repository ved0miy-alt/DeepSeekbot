import telebot
from handlers import register_handlers

TOKEN = "******"


def main():
    bot = telebot.TeleBot(TOKEN)
    register_handlers(bot)
    bot.infinity_polling()


if __name__ == "__main__":
    main()
