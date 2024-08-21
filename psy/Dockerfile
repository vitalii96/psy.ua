FROM python:3.11.5

WORKDIR /app
COPY . /app/


RUN pip install -r requirements.txt

# Копіюємо скрипт до контейнера
COPY entrypoint.sh /app/entrypoint.sh

# Встановлюємо права на виконання для скрипту
RUN chmod +x /app/entrypoint.sh

# Запускаємо скрипт при старті контейнера
CMD ["/app/entrypoint.sh"]

#CMD python manage.py migrate \
#    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='root').exists() or User.objects.create_superuser('root', 'panch.vit@gmail.com', 'root')"
#    && python manage.py loaddata fixture.json \
#    && python manage.py runserver 0.0.0.0:8000