from django.shortcuts import render
from django.http import HttpResponse
from .models import department
from django.template import RequestContext, loader


# Create your views here.
def  departments(request):
	department_list = department.objects.all()
	template = loader.get_template('equipment/departments.html')
	context = RequestContext(request, {
			'department_list': department_list,
		})
	return HttpResponse(template.render(context))

def sites(request):
	return HttpResponse("Sites Page")

def equipment(request):
	return HttpResponse("Equipment Page")