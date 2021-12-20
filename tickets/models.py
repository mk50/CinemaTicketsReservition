from django.db import models


class Movie(models.Model):
    hall=models.CharField(max_length=50)
    movie=models.CharField( max_length=200)
    

    def __str__(self):
        return self.movie

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