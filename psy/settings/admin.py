from django.contrib import admin
from .models import *
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title','telegram_token',)
# Register your models here.
admin.site.register(Settings,SettingsAdmin)