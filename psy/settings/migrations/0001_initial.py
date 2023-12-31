# Generated by Django 4.2 on 2023-09-29 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Змінні')),
                ('telegram_token', models.CharField(max_length=255, verbose_name='Токен Телеграм')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Налаштування',
                'verbose_name_plural': 'Ознаки',
                'ordering': ['title'],
            },
        ),
    ]
