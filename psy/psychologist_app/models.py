from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User


class Diploma(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва диплому')
    issuing_organization = models.CharField(max_length=255, verbose_name='Видавник/Організація', null=True)
    special = models.CharField(max_length=255, verbose_name='Спеціальність', null=True)
    date = models.DateField(verbose_name='Коли виданий')
    image = models.ImageField(upload_to='diploma_images/', verbose_name='Фото диплому')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    number = models.CharField(max_length=255, verbose_name='Номер')

    class Meta:
        verbose_name = 'Дипломи'
        verbose_name_plural = 'Дипломи'

    # Додаткові поля про диплом

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва сертифікату')
    issuing_organization = models.CharField(max_length=255, verbose_name='Видавник/Організація')
    image = models.ImageField(upload_to='certificate_images/', verbose_name='Фото сертифікату')
    date = models.DateField(verbose_name='Коли виданий')
    link = models.CharField(max_length=100, verbose_name='Посилання на сертифікат', null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    number = models.CharField(max_length=255, verbose_name='Номер')

    class Meta:
        verbose_name = 'Сертифікат'
        verbose_name_plural = 'Сертифікати'

    # Додаткові поля про сертифікат

    def __str__(self):
        return self.title


class Psychologist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    description = models.TextField(verbose_name='Про психолога')
    certificates = models.ManyToManyField('Certificate', verbose_name='Сертифікати', null=True, blank=True)
    diplomas = models.ManyToManyField('Diploma', verbose_name='Дипломи', null=True, blank=True)
    contact_numbers = ArrayField(models.CharField(max_length=200), verbose_name='Номери телефонів')
    email = models.EmailField()# закоментувати, в базовій моделі юзера вже є поле під мило
    profile_picture = models.ImageField(upload_to='psychologist_profiles/', verbose_name='Фото')
    telegram = models.CharField(max_length=20, verbose_name='Телеграм', null=True, blank=True)
    instagram = models.CharField(max_length=255, verbose_name='Інстаграм', null=True, blank=True)
    facebook = models.CharField(max_length=255, verbose_name='Фейсбук', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Психолог'
        verbose_name_plural = 'Психолог'

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Sign(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва ознаки')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ознака'
        verbose_name_plural = 'Ознаки'
        ordering = ['title']

    def __str__(self):
        return self.title

class ContentItems(models.Model):
    title = models.TextField(verbose_name='Назва')
    description = models.TextField(verbose_name='Опис', null=True, blank=True)
    image = models.ImageField(upload_to='psychologist_profiles/', verbose_name='Фото', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    icons = models.CharField(max_length=30, verbose_name='Назва іконки', blank=True, null=True)
    sign = models.ForeignKey(Sign, on_delete=models.SET_NULL, null=True, verbose_name='Ознака')

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контенти'
        ordering = ['created_at']

    def __str__(self):
        return f"{self.title}"