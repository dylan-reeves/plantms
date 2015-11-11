from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *

class departmentForm(ModelForm):
	class Meta:
		model = department
		fields = ['name','reportingManager','sites']

	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit','Submit'))
		super(departmentForm, self).__init__(*args,**kwargs)