# Generated by Django 4.2 on 2023-10-22 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychologist_app', '0004_alter_contentitems_options_alter_sign_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentitems',
            name='icons',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Назва іконки'),
        ),
        migrations.AlterField(
            model_name='contentitems',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Опис'),
        ),
    ]
