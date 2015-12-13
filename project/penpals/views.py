from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .model import Applicant

# Create your views here.

def register(request):
	template = loader.get_template('penpals/register.html')
	context = RequestContext

def result(request):
	try:
		#Get all data treating request like a POST req using request.POST(stuff). If it fails its a GET req
		#and will go into the except block of code else it will go to the else part of it.
	except:
		#display get request result
		template = loader.get_template('penpals/result.html')
		context = RequestContext("""Whatever you need""")
		return HttpResponse(template.render(context))
	else:
		#add entry to db
		return HttpResponseRedirect(reverse('result')) #Redirect to itself
