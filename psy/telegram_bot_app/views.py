from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from telegram import Update
import json

# Налаштування бота (наприклад, у telegram_bot_app/bot.py)
#from .bot import bot

# Встановлення вебхука
# def set_webhook(request):
#     webhook_url = f"{settings.WEBHOOK_URL}/telegram-webhook/"
#     bot.set_webhook(url=webhook_url)
#     return JsonResponse({"message": "Webhook set successfully"})
#
# # Обробка запитів від Telegram
# @csrf_exempt
# def telegram_webhook(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         update = Update.de_json(data, bot.bot)
#         bot.process_update(update)
#     return JsonResponse({"status": "ok"})

