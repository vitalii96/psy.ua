import telebot
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TelegramBot


class GetBotSettings:
    def get_telegram_token(self):
        try:
            bot_token = TelegramBot.objects.first()
            return bot_token.telegram_token
        except TelegramBot.DoesNotExist:
            return None
    def get_telegram_chat_id(self):
        try:
            bot_token = TelegramBot.objects.first()
            return bot_token.chat_id
        except TelegramBot.DoesNotExist:
            return None

bot_settings = GetBotSettings()
bot = telebot.TeleBot(bot_settings.get_telegram_token())


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    mess = f'твій ід {chat_id}'
    bot.send_message(message.chat.id, mess)


@bot.message_handler()
def SendInformationForm(name, phone_number, description="", telegram=''):
    chat_id = bot_settings.get_telegram_chat_id()
    information = f'Отримані дані з сайту : \n Імя : {name} \n Телеграм: {telegram} \n Номер телефону: {phone_number} \n Опис проблеми: {description}'
    bot.send_message(chat_id, information)


@csrf_exempt  # Вимикає перевірку csrf токена для post даних
def webhook(request):
    if request.method == 'POST':
        json_str = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
    return HttpResponse("Webhook endpoint reached", status=200)


def set_telegram_webhook():
    # Налаштовуємо webhook на біч Telegram з URL від ngrok
    webhook_url = 'https://f7f1-91-201-147-221.ngrok-free.app/webhook/'  # Виправлено URL
    # url який надав ngrok
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)
