import openai
from telegram.ext import Updater, MessageHandler, Filters
import logging
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(level=logging.INFO)

def responder(update, context):
    pergunta = update.message.text
    try:
        r = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um velho sábio, calmo, paciente, com fala ancestral japonesa. Suas respostas são breves, profundas e filosóficas."},
                {"role": "user", "content": pergunta}
            ]
        )
        context.bot.send_message(chat_id=update.message.chat_id, text=r.choices[0].message.content)
    except Exception as e:
        context.bot.send_message(chat_id=update.message.chat_id, text="Erro ao responder.")

updater = Updater(TELEGRAM_TOKEN, use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, responder))
updater.start_polling()
updater.idle()
