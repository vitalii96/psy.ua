# Generated by Django 4.2 on 2023-10-08 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_topic_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='color',
            field=models.CharField(choices=[('pink', 'Рожевий'), ('blue', 'Блакитний'), ('green', 'Бірюзовий'), ('maline', 'Малиновий'), ('violet', 'Фіолетовий'), ('darkblue', 'Синій'), ('none', 'Прозорий')], default='pink', max_length=20),
        ),
    ]