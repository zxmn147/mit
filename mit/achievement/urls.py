from django.conf.urls import url
from achievement import views

urlpatterns = [
    
    url(r'^$', views.achievement, name='achievement'),
    
]