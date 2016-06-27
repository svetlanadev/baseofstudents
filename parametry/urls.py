from django.conf.urls import patterns, url
from parametry import views

urlpatterns = [
    url(r'^$', views.parametry, name= 'parametry'), 
    url(r'^group/add/$', views.group_add, name='group_add'),
]