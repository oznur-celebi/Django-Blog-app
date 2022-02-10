from django.db import models
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect


# class Category(models.Model):
#   color = models.CharField(max_length=6, choices=, default='green')
paths =[('Fullstack','Fullstack'),('Frontend', 'Frontend'),('Backend','Backend')]
class Post(models.Model):
    title = models.CharField(max_length=100)
    content =models.TextField()
    date_posted =models.DateTimeField(default= timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    cover = models.ImageField(default='post.jpg', upload_to='profile_pics/cover/')
    category = models.CharField(max_length=20, choices=paths, default='fullstack')
    category

    def __str__(self):
        return self.title
    def get_absolute_url(self):
       
        return reverse('blog-home')
#     class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content =models.TextField()
#     date_posted =models.DateTimeField(default= timezone.now)
#     author = models.ForeignKey(User, on_delete = models.CASCADE)
   