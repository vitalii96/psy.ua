from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, null=True,  on_delete=models.CASCADE, verbose_name='Користувач',blank=True)
    contact_number = models.CharField(max_length=20, verbose_name='Номер телефону')
    issue_description = models.TextField(verbose_name='Інформація про клієнта', null=True)
    first_name = models.CharField(max_length=50, verbose_name="Ім'я", null=True)
    last_name = models.CharField(max_length=50, verbose_name="Прізвище", null=True)
    profile_picture = models.ImageField(upload_to='client_profiles/', verbose_name='Фото', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Клієнти'
        verbose_name_plural = 'Клієнти'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class SessionRecord(models.Model):
    STATUS_CHOICES = (
        ('pending_confirmation', 'Очікує підтвердження'),
        ('confirmed', 'Підтверджено'),
        ('canceled', 'Скасовано'),
        ('rescheduled', 'Перенесено'),
        ('completed', 'Завершено'),
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клієнт', blank=True, null=True)
    session_date = models.DateField(verbose_name='Дата сессії')
    session_time = models.TimeField(verbose_name='Час сессії', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending_confirmation')

    # Додаткові поля, наприклад, тип сеансу, тривалість, статус і т.д.
    class Meta:
        verbose_name = 'Сесія'
        verbose_name_plural = 'Сесії'

    def __str__(self):
        return f"Запис на сессію {self.client.first_name} на  {self.session_date}"
