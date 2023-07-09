from django.db import models
from django.contrib.auth.models import User

class Generous(models.Model):
    genre_title = models.CharField(max_length = 200,unique=True)

    def __str__(self):
        return self.genre_title

class Post(models.Model):
    title = models.CharField(max_length=20,unique=True)
    category = models.ForeignKey(Generous,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE) 
    price = models.IntegerField(max_length=5)
    nop = models.IntegerField(max_length=20)
    genre = models.CharField(max_length=20)
    isbn = models.IntegerField(max_length=20)
    image = models.ImageField(upload_to="post/")
    description = models.TextField()

    def __str__(self):
        return self.title
    

