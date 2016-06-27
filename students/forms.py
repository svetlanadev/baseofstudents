from django import forms
from .models import Studentsprofile

class StudentsForm(forms.ModelForm):

	class Meta:
		model = Studentsprofile
		fields = ('firstname', 'lastname', 'middlename', 'date_of_birth', 'students_ticket', 'group',)
