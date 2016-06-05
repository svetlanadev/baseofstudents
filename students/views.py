from django.shortcuts import render
from django.http import HttpResponse
from students.models import Studentsprofile

def index(request):
	return render(request, 'base.html')

def students(request):
	studvariable = Studentsprofile.objects.all()
	return render(request, 'index.html', {'sequence': studvariable})