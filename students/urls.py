from django.conf.urls import patterns, url
from students import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^$', views.about, name = 'about'),
]