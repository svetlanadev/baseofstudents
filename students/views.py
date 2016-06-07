from django.shortcuts import render
from django.http import HttpResponse
from students.models import Studentsprofile

def base(request):
	students = Studentsprofile.objects.all()
	return render(request, 'base.html', {'studentsall': students})


def students(request):
	students = Studentsprofile.objects.all()
	return render(request, 'index.html', {'studentsall': students})
	