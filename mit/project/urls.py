from django.conf.urls import url
from project import views

urlpatterns = [
    
    url(r'^$', views.project, name='project'),
    
]