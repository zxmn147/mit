from django.conf.urls import url
from teacher import views

urlpatterns = [
    
    url(r'^$', views.teacher, name='teacher'),
    
]