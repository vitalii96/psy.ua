from django.contrib.auth.models import User
from psychologist_app.models import *
from client_app.models import Client
from review_app.models import Review
from blog.models import *
def data ():
    # Створення звичайного користувача
    # user = User.objects.create_user( username='client1', password='123',email='budanov@gmail.com')
    # user.first_name = 'Кирило'  # Встановлюємо ім'я
    # user.last_name = 'Буданов'  # Встановлюємо прізвище
    # user.save()
    # # Створення адміністратора
    admin = User.objects.create_superuser(username='admin', password='root', email='panch.vit@gmail.com')
    admin.save()
    # ------------------Дипломи-----------
    # diploma = Diploma(title='Диплом бакалавра ЧНУ', year=2020)
    # diploma.save()
    #-------------------Сертифікати----------------
    # certificate = Certificate(title='Сертифікат про проходження курсів КПТ', issuing_organization='Державні онлайн курси')
    # certificate.save()
    #---------------------Витяг дипломів і сертифікатів-------------
    # certificate = Certificate.objects.get(pk=2)
    # diploma = Diploma.objects.get(pk=2)
    # -------------Витяг юзера-----------------
    # user = User.objects.get(username='psylogist')
    # psychologist = Psychologist(user=user, description='Вітаю ! Мене звуть Анастасія, я практичний та соціальний психолог', contact_numbers=['0680984469'], email='anastasion@panchuk.gmail.com')
    # psychologist.save()
    # psychologist.diplomas.add(diploma)
    # psychologist.certificates.add(certificate)
    # psychologist.save()
    # client = Client(user=user,contact_number='0955649694',issue_description='Голова ГУР')
    # client.save()
    # client = Client.objects.get(pk=2)
    # review = Review(client =client,content='чудовий психолог !')
    # review.save()
    # topic = Topic(title='ОКР')
    # topic.save()
    # topic2 = Topic(title='СДУГ')
    # topic2.save()
    # user = User.objects.get(pk=1)
    # topic = Topic.objects.get(title='ОКР')
    # post = Post(author=user,topic=topic,title='Як боротися з ОКР',content='Щоб побороти ОКР потрібно частіше мити руки!')
    # post.save()
    # post = Post(author=user, topic=topic, title='Як боротися з СДУГ',
    #             content='Щоб побороти СДУГ потрібно бути уважнішим!')
    # post.save()