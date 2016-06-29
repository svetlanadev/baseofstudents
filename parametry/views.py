from django.shortcuts import render, redirect
from django.http import HttpResponse
from parametry.models import Groupofstudents
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