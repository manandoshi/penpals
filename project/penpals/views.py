from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from .models import Applicant
import pdb

# Create your views here.
#class register(View):
#	def get(self, request):
#		super(register, self).__init__()
		

def register(request):
	try:
		name 		= 	request.POST["name"]
		address 	= 	request.POST["address"]
		interests 	= 	{ 	
							"sports"	: 	request.POST.getlist("sports"),
							"moviesTV"	:	request.POST.getlist("moviesTV"),
							"dancePA"	:	request.POST.getlist("dancePA"),
							"pfa"		:	request.POST.getlist("pfa"),
							"lit"		:	request.POST.getlist("lit"),
							"gaming"	:	request.POST.getlist("gaming"),
							"music"		:	request.POST.getlist("music"),
							"other"		:	request.POST.getlist("other"),
						}
	except:	
		template = loader.get_template('penpals/register.html')
		context = RequestContext(request, {},)
		return HttpResponse(template.render(context))
	else:
		for i in range(interests["sports"].length):
			assert True

def result(request):
	template = loader.get_template('penpals/result.html')
	context = RequestContext(request, {},)
	return HttpResponse(template.render(context))