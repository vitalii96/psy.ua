from django.db import models
from client_app.models import Client


class Review(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Користувач')
    content = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'
        ordering = ['created_at']

    def __str__(self):
        return f"Відгук від  {self.client.user.first_name+' '+self.client.user.last_name}"
