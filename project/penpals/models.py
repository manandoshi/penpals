from __future__ import unicode_literals

from django.db import models

# Create your models here.

class interests(models.Model):
	name 		= 	models.CharField(max_length = 128)
	category	=	models.CharField(max_length = 128)
	#numpeople 	= 	modelsIntegerField()

class Applicant(models.Model):
	name 		= 	models.CharField(max_length = 128)
	address 	= 	models.TextField()
	gender 		= 	models.CharField(max_length = 15)
	interests	=	models.ManyToManyField(interests)
	# sports 		= 	models.CommaSeparatedIntegerField(max_length = 20)
	# moviesTV 	= 	models.CommaSeparatedIntegerField(max_length = 20)
	# dancePA 	= 	models.CommaSeparatedIntegerField(max_length = 20)
	# lit 		= 	models.CommaSeparatedIntegerField(max_length = 20)
	# travel 		= 	models.BooleanField(default = False)
	# gaming 		= 	models.CommaSeparatedIntegerField(max_length = 20)
	# pfa 		= 	models.CommaSeparatedIntegerField(max_length = 20)
	# cooking 	= 	models.BooleanField(default = False)
	# collection 	= 	models.BooleanField(default = False)
	# music 		= 	models.CommaSeparatedIntegerField(max_length = 20) 