from django.shortcuts import render
from django.http import HttpResponse
from parametry.models import Groupofstudents

def parametry(request):
	groups = Groupofstudents.objects.all()
	return render(request, 'index1.html', {'groupsall' : groups})