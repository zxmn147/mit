from django.conf.urls import url
from project import views

urlpatterns = [
    
    url(r'^$', views.project, name='project'),
    url(r'^projectCreate/$', views.projectCreate, name='projectCreate'),
    url(r'^projectRead/(?P<projectId>[0-9]+)/$', views.projectRead, name='projectRead'),
]