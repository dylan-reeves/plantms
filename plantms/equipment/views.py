from django.shortcuts import render
from django.http import HttpResponse
from .models import department, site, equipment
from django.template import RequestContext, loader


# Create your views here.
def  departments(request):
	department_list = department.objects.prefetch_related('sites').all()
	context ={'department_list': department_list}
	return render(request, 'equipment/departments.html', context)

def sites(request):
	site_list = site.objects.all()
	context ={'site_list': site_list}
	return render(request, 'equipment/sites.html', context)
	
def equipment(request):
	equipment_list = equipment.objects.all()
	context ={'equipment_list': equipment_list}
	return render(request, 'equipment/equipment.html', context)
	
def index(request):
	return render(request, 'equipment/index.html')

def departmentdetail(request, department_id):
	department_details = department.objects.prefetch_related('sites').get(pk=department_id)
	site_list = list(department_details.sites.all())
	context = {'department_details': department_details,
				'site_list': site_list,
	}
	return render(request, 'equipment/departmentdetails.html', context)