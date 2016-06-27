from django import forms
from .models import Groupofstudents

class GroupofstudentsForm(forms.ModelForm):

	class Meta:
		model = Groupofstudents
		fields = ('name', 'lead',)
