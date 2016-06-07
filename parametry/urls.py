from django.conf.urls import patterns, url
from parametry import views

urlpatterns = [
	url(r'^parametry', views.parametry, name= 'parametry'),
]