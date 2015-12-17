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

# def rs(apps, points, currpairing, bestpairing):
# 		mx = 0
# 		pt = 0

# 		if(len(apps) == 1):
# 			return 0
		
# 		if(len(apps) == 2):
# 			currpairing[(currpairing[int(apps[0].id) - 1])-1]	=	0
# 			currpairing[(currpairing[int(apps[1].id) - 1])-1]	=	0
# 			currpairing[int(apps[0].id) - 1] 					= 	apps[1].id
# 			currpairing[int(apps[1].id) - 1]					= 	apps[0].id
# 			return points[int(apps[0].id)-1][int(apps[1].id)-1]
		
# 		for x in xrange(1,len(apps)):
			
# 			a0 		= 	apps[0]
# 			ax 		= 	apps[x]
# 			apps 	= 	apps[1:x] + apps[x+1:]
# 			#pdb.set_trace();
# 			pt = points[int(a0.id)-1][int(ax.id)-1] + rs(apps,points, currpairing, bestpairing)
			
# 			currpairing[(currpairing[int(a0.id) - 1])-1]=0
# 			currpairing[(currpairing[int(ax.id) - 1])-1]=0
# 			currpairing[int(a0.id) - 1] = ax.id
# 			currpairing[int(ax.id) - 1]	= a0.id
# 			#pdb.set_trace();
			
# 			if (pt > mx):
# 				mx	=	pt
# 				if(mx == 160):
# 					pdb.set_trace();
# 				if (int(a0.id) == int(Applicant.objects.all()[0].id)):
# 					#pdb.set_trace();
# 					for i in range(len(currpairing)):
# 						bestpairing[i] = currpairing[i]
			
# 			currpairing[int(a0.id) - 1] = 0
# 			currpairing[int(ax.id) - 1]	= 0
# 			apps = [a0] + apps[0:x-1] + [ax] + apps[x-1:]
		
# 		apps = apps [1:]
# 		pt = rs(apps,points, currpairing, bestpairing)
# 		currpairing[a0.id-1] = 0
# 		if (pt > mx):
# 				mx	=	pt
# 				if (int(a0.id) == int(Applicant.objects.all()[0].id)):
# 					for i in range(len(currpairing)):
# 						bestpairing[i] = currpairing[i]
# 		apps = [a0] + apps[:]

# 		return mx

def rs(apps,points):
	mxval = 0
	mxconfig = []
	if (len(apps)==1):
		return 0,[[apps[0].id, apps[0].id]]
	if (len(apps)==2):
		return points[int(apps[0].id)-1][int(apps[1].id)-1] , [[apps[0].id, apps[1].id]]
	else:
		for x in xrange(0,len(apps)):
			a0 				= 	apps[0]
 			ax 				= 	apps[x]
			appsp 			= 	apps[1:x] + apps[x+1:]
			
			pt 				= 	points[ int(a0.id)-1 ][ int(ax.id)-1 ]
			#pdb.set_trace()
			pval, pconfig 	=	rs(appsp, points)
			if(pt+pval > mxval):
				mxval 		= pt + pval
				mxconfig	= pconfig[:] + [[a0.id, ax.id]]
		return mxval, mxconfig



def register(request):
	try:
		name 				= 	request.POST["name"]
		address 			= 	request.POST["address"]
		gender				=	request.POST["gender"]
		selectedInterests 	=	request.POST.getlist("interests")
		#return HttpResponse(selectedInterests[1])
		
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
		return HttpResponseRedirect('/register')

def view(request):
	template = loader.get_template('penpals/view.html')
	context = RequestContext(request, {"applic": Applicant.objects.all(), "interests":interests,},)
	return HttpResponse(template.render(context))

def result(request):
	n 	= (Applicant.objects.all().order_by("-id")[0].id)
	num = len(Applicant.objects.all())
	
	for interest in interests.objects.all():
		interest.points = num - len(interest.applicant_set.all())
		interest.save()
	points = [[0 for i in xrange(n)] for j in xrange(n)]
	currpairing = [0 for i in xrange(n)]
	bestpairing = [0 for i in xrange(n)]
	for i in xrange(num):
		for j in xrange(i+1,num):
			if(Applicant.objects.all()[i].gender != Applicant.objects.all()[j].gender):
				points[int(Applicant.objects.all()[i].id) - 1][int(Applicant.objects.all()[j].id) - 1] += 100;
				points[int(Applicant.objects.all()[j].id) - 1][int(Applicant.objects.all()[i].id) - 1] += 100;
			for interest in Applicant.objects.all()[i].interests.all():
				if(len(Applicant.objects.all()[i].interests.filter(name=interest.name))):
					points[int(Applicant.objects.all()[i].id) - 1][int(Applicant.objects.all()[j].id) - 1] += interest.points
					points[int(Applicant.objects.all()[j].id) - 1][int(Applicant.objects.all()[i].id) - 1] += interest.points
	strot = ""
	for i in xrange(n):
		for j in xrange(n):
			strot += str(points[i][j]) + "\t"
		strot += "<br>"
	#return HttpResponse(strot)
	apps = Applicant.objects.all()[:]
	apps2 = Applicant.objects.all()[:]
	m, conf = rs(apps, points)
	return HttpResponse(conf)
	template = loader.get_template('penpals/result.html')
	context = RequestContext(request, {},)
	