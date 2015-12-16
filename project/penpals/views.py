from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from .models import Applicant, interests
import pdb

# Create your views here.
#class register(View):
#	def get(self, request):
#		super(register, self).__init__()
		

def register(request):
	try:
		name 				= 	request.POST["name"]
		address 			= 	request.POST["address"]
		gender				=	request.POST["gender"]
		selectedInterests 	=	request.POST.getlist("interests")
		# selectedIntrests 	= 	{ 	
		# 							"sports"	: 	request.POST.getlist("sports"),
		# 							"moviesTV"	:	request.POST.getlist("moviesTV"),
		# 							"dancePA"	:	request.POST.getlist("dancePA"),
		# 							"pfa"		:	request.POST.getlist("pfa"),
		# 							"lit"		:	request.POST.getlist("lit"),
		# 							"gaming"	:	request.POST.getlist("gaming"),
		# 							"music"		:	request.POST.getlist("music"),
		# 							"other"		:	request.POST.getlist("other"),
		# 						}
	except:	
		template = loader.get_template('penpals/register.html')
		context = RequestContext(request, {},)
		return HttpResponse(template.render(context))
	else:
		applic = Applicant(name=name, address=address, gender=gender)
		applic.save()
		for interest in selectedInterests:
			i = interests.objects.filter(name=interest)[0]
			applic.interests.add(i);
		HttpResponseRedirect(register)
		
def result(request):
	template = loader.get_template('penpals/result.html')
	context = RequestContext(request, {},)
	return HttpResponse(template.render(context))