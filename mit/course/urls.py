from django.conf.urls import url
from course import views

urlpatterns = [
    
    url(r'^$', views.course, name='course'),
    
]