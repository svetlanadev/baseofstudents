from django.shortcuts import render, redirect
from django.http import HttpResponse
from parametry.models import Groupofstudents
from students.models import Studentsprofile
from .forms import GroupofstudentsForm

def parametry(request):
	groups = Groupofstudents.objects.all()
	return render(request, 'index1.html', {'groupsall' : groups})

def group_add(request):
	if request.method == "POST":
		form = GroupofstudentsForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('parametry')
	else:
		form = GroupofstudentsForm()
	return render(request, 'group_add.html', {'form' : form})

def group_list(request, group_id):
	context_dict = {}
	group = Groupofstudents.objects.get(id=group_id)
	context_dict['group_id'] = group.id
	student = Studentsprofile.objects.filter(group=group)
	context_dict['student'] = student
	context_dict['group'] = group
	return render(request, 'group_list.html', context_dict)
	