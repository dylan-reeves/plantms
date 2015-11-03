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
	lastMaintenanceDate = models.DateField('Last Maintenance Conducted', null=True, blank=True)
	#TODO lastMaintenanceJob will be linked to MaintenanceJob App in
	#Future for now I will just set it to an integer field, will 
	#change later
	lastMaintenanceJob = models.IntegerField(default=0)
	nextMaintenanceScheduled = models.BooleanField(default=False)
	nextMaintenanceWindowStartDate = models.DateField('Next Maintenance Window Open', null=True, blank=True)
	nextMaintenanceWindowEndDate = models.DateField('Next Maintenance Window Close', null= True, blank = True)
	#TODO nextMaintenanceJob as with above will be linked to foreign
	#key when ready
	nextMaintenanceJob = models.IntegerField(default=0)
	#TODO as with above two the maintenance schedule functionality will
	#be added in the second sprint cycle
	maintenanceSchedule = models.IntegerField(default=0)
	intervalType = models.CharField(max_length=100)
	active = models.BooleanField(default=True)
	def __str__(self):
		return self.name
		
		