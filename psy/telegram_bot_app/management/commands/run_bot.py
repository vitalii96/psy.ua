from django.core.management.base import BaseCommand
from telegram_bot_app.bot import bot

class Command(BaseCommand):
    help = 'Run the Telegram bot'

    def handle(self, *args, **kwargs):
        # Запустіть бот
        bot.polling(none_stop=True)

#ВИДАЛИТИ ВЕБХУК БОТА
# import requests
#
# bot_token = '6660919649:AAEtScBDPP_zmuTFK2PvMbVPQFQHni7TV6Y'  # Замініть на ваш токен бота
# url = f'https://api.telegram.org/bot{bot_token}/deleteWebhook'
#
# response = requests.post(url)
# print(response.json())
