# Generated by Django 4.2 on 2023-07-26 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client_app', '0005_client_first_name_client_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionrecord',
            name='issue_description',
            field=models.TextField(null=True, verbose_name='Додаткова інформація'),
        ),
        migrations.AlterField(
            model_name='client',
            name='issue_description',
            field=models.TextField(null=True, verbose_name='Інформація про клієнта'),
        ),
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач'),
        ),
    ]
