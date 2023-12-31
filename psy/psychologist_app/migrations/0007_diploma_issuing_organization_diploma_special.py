# Generated by Django 4.2 on 2023-11-12 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychologist_app', '0006_alter_psychologist_certificates_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='diploma',
            name='issuing_organization',
            field=models.CharField(max_length=255, null=True, verbose_name='Видавник/Організація'),
        ),
        migrations.AddField(
            model_name='diploma',
            name='special',
            field=models.CharField(max_length=255, null=True, verbose_name='Спеціальність'),
        ),
    ]
