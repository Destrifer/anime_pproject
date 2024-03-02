from django.db import models

class User(models.Model):
	login = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	email = models.EmailField()
	date = models.DateField(auto_now_add=True)


class Anime(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	date = models.DateField()
	rating = models.SmallIntegerField(default=0)
	poster = models.ImageField(blank=True)

class Episode(models.Model):
	anime = models.SmallIntegerField()
	number = models.SmallIntegerField()
	title = models.CharField(max_length=100)
	time = models.TimeField()
	video = models.FileField()

class Comments(models.Model):
	user = models.SmallIntegerField()
	anime = models.SmallIntegerField()
	text = models.TextField()
	date = models.DateField(auto_now_add=True)
	rating = models.SmallIntegerField(default=0)