from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import UserSettingsHolder, settings
from django.contrib.auth.models import User

class Movie(models.Model):
    hall=models.CharField(max_length=50)
    movie=models.CharField( max_length=200)
    

    def __str__(self):
        return self.movie

class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)

class Guest(models.Model):
    name=models.CharField( max_length=50)
    mobile=models.IntegerField()

    def __str__(self):
        return self.name
class Reversation(models.Model):
    guest=models.ForeignKey(Guest,on_delete=models.CASCADE,related_name="reversation")
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE,related_name="reversation")
    
    def __str__(self):
        return f"{self.guest} {self.movie}"

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)