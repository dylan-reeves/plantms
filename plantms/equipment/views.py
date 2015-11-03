from django.shortcuts import render
from django.http import HttpResponse
from .models import department, site, equipment
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
	site_list = site.objects.all()
	template = loader.get_template('equipment/sites.html')
	context = RequestContext(request, {
		'site_list': site_list,
		})
	return HttpResponse(template.render(context))

def equipment(request):
	equipment_list = equipment.objects.all()
	template = loader.get_template('equipment/equipment.html')
	context = RequestContext(request, {
		'equipment_list': equipment_list,
		})
	return HttpResponse(template.render(context))