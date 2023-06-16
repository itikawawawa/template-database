from django.db import models
from django.utils import timezone


class User(models.Model):
    userid = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=20)
    bio = models.CharField(max_length=200,default='こんにちわ。よろしくお願いします')
    emailField = models.EmailField(max_length=255)
    userimage = models.ImageField()

    def __str__(self):
    	return self.name

class Post(models.Model):
    userid = models.ForeignKey('User', on_delete=models.CASCADE)
    praceid = models.ForeignKey('Prace', on_delete=models.CASCADE)
    desc = models.CharField(max_length=150)
    postimage = models.ImageField()
    day = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return str(self.userid)

class Anime(models.Model):
    amineid = models.IntegerField(primary_key=True, editable=False)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    related = models.CharField(max_length=200)
    animeimage = models.ImageField()

    def __str__(self):
    	return self.title

class Prace(models.Model):
    pracename = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    notes = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    acsess = models.CharField(max_length=150)
    praceimage = models.ImageField()
    animeid = models.ForeignKey('Anime', on_delete=models.CASCADE)
    
    def __str__(self):
    	 return self.pracename
# Create your models here.
