#!/bin/bash
set -e

# Міграції
python manage.py migrate
# Запуск сервера

python manage.py loaddata fixture.json
python manage.py runserver 0.0.0.0:8000

# Створення суперкористувача, якщо він не існує
#python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='root').exists() or User.objects.create_superuser('root', 'panch.vit@gmail.com', 'root')"

# Завантаження даних


