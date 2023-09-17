# Generated by Django 4.2 on 2023-08-27 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychologist_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Назва')),
                ('description', models.TextField(verbose_name='Опис')),
                ('image', models.ImageField(blank=True, null=True, upload_to='psychologist_profiles/', verbose_name='Фото')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Контент',
                'verbose_name_plural': 'Контенти',
            },
        ),
    ]
