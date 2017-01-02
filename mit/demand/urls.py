from django.conf.urls import url
from demand import views

urlpatterns = [
    
    url(r'^$', views.demand, name='demand'),
    
]