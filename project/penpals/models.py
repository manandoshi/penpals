from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Applicant(models.Model):
	name = models.CharField(max_length = 128)
	address = models.TextField()
	gender = models.CharField(max_length = 15)
	sports = models.CommaSeperatedIntegerField(max_length = 20)
	moviesTV = models.CommaSeperatedIntegerField(max_length = 20)
	dancePA = models.CommaSeperatedIntegerField(max_length = 20)
	lit = models.CommaSeperatedIntegerField(max_length = 20)
	travel = models.BooleanField(default = False)
	gaming = models.CommaSeperatedIntegerField(max_length = 20)
	pfa = models.CommaSeperatedIntegerField(max_length = 20)
	cooking = models.BooleanField(default = False)
	collection = models.BooleanField(default = False)
	music = models.CommaSeperatedIntegerField(max_length = 20) 
	#here i put sports = models.CommaSepejdgjorsthotsrField(max_length = 10)
