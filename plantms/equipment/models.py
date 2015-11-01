from django.db import models
from audit_log.models import AuthStampedModel
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User

# Create your models here.
class site(TimeStampedModel,AuthStampedModel):
	name = models.CharField(max_length=100)
	reportingUsers = models.ManyToManyField(User)
	def __str__(self):
		return self.name

class department(TimeStampedModel,AuthStampedModel):
	name = models.CharField(max_length=100)
	reportingManager = models.ForeignKey(User)
	sites = models.ManyToManyField(site)
	def __str__(self):
		return self.name

class equipment(TimeStampedModel,AuthStampedModel):
	name = models.CharField(max_length=100)
	code = models.IntegerField
	department = models.ForeignKey(department)
	site = models.ForeignKey(site)
	lastMaintenanceDate = models.DateTimeField('Last Maintenance Conducted')
	#TODO lastMaintenanceJob will be linked to MaintenanceJob App in
	#Future for now I will just set it to an integer field, will 
	#change later
	lastMaintenanceJob = models.IntegerField(default=0)
	nextMaintenanceDate = models.DateTimeField('Next Maintenance Job')
	#TODO nextMaintenanceJob as with above will be linked to foreign
	#key when ready
	nextMaintenanceJob = models.IntegerField(default=0)
	#TODO as with above two the maintenance schedule functionality will
	#be added in the second sprint cycle
	maintenanceSchedule = models.IntegerField(default=0)
	intervalType = models.CharField(max_length=100)
	active = models.BooleanField
	def __str__(self):
		return self.name
		
		