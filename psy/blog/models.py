from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from psychologist_app.models import Psychologist

class Topic(models.Model):
    STATUS_CHOICES = (
        ('style1', 'Рожевий'),
        ('style2', 'Блакитний'),
        ('style3', 'Бірюзовий'),
        ('style4', 'Малиновий'),
        ('style5', 'Фіолетовий'),
        ('style6', 'Синій'),
        ('none', 'Прозорий'),
    )
    title = models.CharField(max_length=255, db_index=True, verbose_name='Назва')
    description = models.CharField(max_length=255,verbose_name='Опис теми', null=True, blank=True)
    profile_picture = models.ImageField(upload_to='topic_images/', verbose_name='Зображення', null=True, blank=True)
    color = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pink')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)

    class Meta:
        verbose_name = 'Теми'
        verbose_name_plural = 'Теми'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('topic', kwargs={'topic_slug': self.slug})


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,  verbose_name='Автор')
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE,  verbose_name='Автор посту', null=True, blank=True)
    subtitle = models.CharField(max_length=255,verbose_name='Короткий опис', null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, verbose_name='Тема') #якщо буде видалено звязаний запис "Тема", то в дане поле буде записано NULL
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Текст')
    profile_picture = models.ImageField(upload_to='post_profiles/', verbose_name='Зображення', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубліковано')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'
        ordering = ['-created_at','title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
