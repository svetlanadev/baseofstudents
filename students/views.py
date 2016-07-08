from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from students.models import Studentsprofile
from parametry.models import Groupofstudents
from .forms import StudentsForm

def base(request):
	return render(request, 'base.html')


def students(request):
	students = Studentsprofile.objects.order_by("students_ticket")
	return render(request, 'students/index.html', {'studentsall': students})

    # class Meta:
    #     ordering = ["name"]	

def students_test(request):
	return render(request, 'students/test.html' )

def students_add(request):
	if request.method == 'POST':
		form = StudentsForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('students')
	else: 
		form = StudentsForm()
	return render(request, 'students/students_add.html', {'form' : form})
	
def students_edit(request, stud_id):
	stud = get_object_or_404(Studentsprofile, id=stud_id)
	if request.method == 'POST':
		form = StudentsForm(request.POST, instance=stud)
		if form.is_valid():
			form.save()
		return redirect('students.views.students')
	else: 
		form = StudentsForm(instance=stud)
	return render(request, 'students/students_add.html', {'form' : form})

 