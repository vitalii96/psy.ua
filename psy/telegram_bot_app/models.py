from django.db import models
class TelegramBot(models.Model):
    telegram_token = models.CharField(max_length=255, verbose_name='Токен Телеграм')
    chat_id = models.CharField(max_length=50, verbose_name='id Чату')
    user_id = models.CharField(max_length=50, verbose_name='id Користувача', null=True, blank=True)
    webhook_url = models.CharField(max_length=255, verbose_name='Адреса веб-хука', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Телеграм Бот'
        verbose_name_plural = 'Телеграм Боти'
        ordering = ['created_at']

    def __str__(self):
        return self.chat_id
# Create your models here.
