from django.conf.urls import patterns, url
from students import views


urlpatterns = [
	url(r'^$', views.base, name = 'base'),
	url(r'^students', views.students, name= 'students'),
]

# url(r'^blog/', include('blog.urls'))