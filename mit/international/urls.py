from django.conf.urls import url
from international import views

urlpatterns = [
    
    url(r'^$', views.international, name='international'),
    
]