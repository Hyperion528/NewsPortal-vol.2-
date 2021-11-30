from django.db import models
from django.conf import settings

from datetime import datetime

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=128)
    full_text=models.TextField()
    date_create=models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='Category')

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/posts/{self.id}' 


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # названия категорий тоже не должны повторяться
 
    def __str__(self):
        return f'{self.name}'