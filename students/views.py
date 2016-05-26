from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("just test!")

def about(request):
	return HttpResponse("It's about page")