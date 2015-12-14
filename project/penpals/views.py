from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Applicant

# Create your views here.

def register(request):
	template = loader.get_template('penpals/register.html')
	return HttpResponse(template.render({}))

def result(request):
	try:
		#Get all data treating request like a POST req using request.POST(stuff). If it fails its a GET req
		#and will go into the except block of code else it will go to the else part of it.
		random = request.POST("random")
	except:
		#display get request result
		template = loader.get_template('penpals/result.html')
		return HttpResponse(template.render({}))
	else:
		#add entry to db
		return HttpResponseRedirect(reverse('result')) #Redirect to itself
