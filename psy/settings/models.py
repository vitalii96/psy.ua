from django.db import models

class Settings(models.Model):
    title = models.CharField(max_length=100, verbose_name='Змінні')
    telegram_token = models.CharField(max_length=255, verbose_name='Токен Телеграм')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Налаштування'
        verbose_name_plural = 'Ознаки'
        ordering = ['title']

    def __str__(self):
        return self.title

# Create your models here.
