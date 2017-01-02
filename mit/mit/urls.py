"""mit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^teacher/', include('teacher.urls', namespace='teacher')),
    url(r'^international/', include('international.urls', namespace='international')),
    url(r'^project/', include('project.urls', namespace='project')),
    url(r'^demand/', include('demand.urls', namespace='demand')),
    url(r'^achievement/', include('achievement.urls', namespace='achievement')),
    url(r'^course/', include('course.urls', namespace='course')),
    url(r'^main', include('main.urls', namespace='main')),
    url(r'^.*', include('main.urls')),
]
