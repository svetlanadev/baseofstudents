from django.conf.urls import patterns, url
from parametry import views

urlpatterns = [
    url(r'^$', views.parametry, name= 'parametry'), 
]