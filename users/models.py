from django.db import models
from  django.contrib.auth.models import User
from  django.contrib.auth.models import AbstractUser
from PIL import Image


class Profile(models.Model):
      user = models.OneToOneField(User, on_delete =models.CASCADE)
      image =models.ImageField(default ='default.jpg', upload_to ='profile_pics')
   
      def __str__(self):
          return f'{self.user.username} Profile'
      def save(self, *args, **kwargs):
          super().save(*args, **kwargs)

          img = Image.open(self.image.path)

          if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Bio(models.Model):
     user = models.OneToOneField(User, on_delete =models.CASCADE)
     bio = models.TextField(max_length=500, blank=True)
     location = models.CharField(max_length=30, blank=True)
     birth_date = models.DateField(null=True, blank=True)

     def __str__(self):
          return f'{self.user.username} Bio'

    