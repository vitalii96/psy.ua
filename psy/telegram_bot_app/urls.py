# urls.py в telegram_bot_app або в основному проекті Django
from django.urls import path
from . import bot

urlpatterns = [
    path('webhook/', bot.webhook, name='telegram_bot_webhook'),
]
