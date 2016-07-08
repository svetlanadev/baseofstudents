"""baseofstudents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from students import views


app_name = "students"
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.students, name= 'students'),
    url(r'^parametry/', include('parametry.urls')),
    url(r'^students/add/$', views.students_add, name='students_add'),
    url(r'^students/test/$', views.students_test, name='students_test'),      
    url(r'^students/(?P<stud_id>[0-9]+)/edit/$', views.students_edit, name='students_edit'), 

] 

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
# urlpatterns += static(settings.MEDIA_URL,
#     document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns() 

# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

