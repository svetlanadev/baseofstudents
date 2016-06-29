from django.shortcuts import render, redirect
from django.http import HttpResponse
from students.models import Studentsprofile
from .forms import StudentsForm

def base(request):
	return render(request, 'base.html')


def students(request):
	students = Studentsprofile.objects.all()
	return render(request, 'index.html', {'studentsall': students})

def students_add(request):
	if request.method == 'POST':
		form = StudentsForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('students')
	else:
		form = StudentsForm()
	return render(request, 'students_add.html', {'form' : form})
	
