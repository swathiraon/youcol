from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Topic(models.Model):
	name=models.CharField(max_length=100)
	tdescription=models.TextField()

	def __str__(self):
		return str(self.name)


class Playlist(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
	title=models.CharField(max_length=160)
	description=models.TextField()
	url=ArrayField(models.CharField(max_length=250))
	
	def __str__(self):
		return str(self.title)






