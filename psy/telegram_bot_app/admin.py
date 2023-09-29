from django.contrib import admin
from .models import *
class TelegramBotAdmin(admin.ModelAdmin):
    list_display = ('telegram_token','chat_id', 'user_id', 'webhook_url')
# Register your models here.
admin.site.register(TelegramBot,TelegramBotAdmin)
# Register your models here.
