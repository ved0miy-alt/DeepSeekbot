import requests
from telebot import TeleBot

URL = "http://localhost:11434/api/generate"
MODEL = "deepseek-r1"


def register_handlers(bot: TeleBot):
    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        user_text = message.text

        payload = {
            "model": MODEL,
            "prompt": user_text,
            "stream": False
        }

        try:
            response = requests.post(
                URL,
                json=payload,
                timeout=120
            )
            response.raise_for_status()
            data = response.json()
            answer = data.get("response", "Пустой ответ от модели")

        except Exception as e:
            answer = f"Ошибка: {e}"

        bot.reply_to(message, answer)
