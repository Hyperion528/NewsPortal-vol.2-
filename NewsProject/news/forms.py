from django import forms
from django.forms import ModelForm, BooleanField
from django import forms  # Импортируем true-false поле

from .models import Post





class PostForm(ModelForm):
    check_box = BooleanField(label='Подтвердить')  # добавляем галочку, или же true-false поле
    

    class Meta:
        model = Post
        fields = ['title','full_text', 'category', 'author']
              # не зку в поля иначе она не будет показываться на странице!
        