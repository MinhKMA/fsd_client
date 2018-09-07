from django.conf.urls import url, include
from client import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^your-name/$', views.oke)
        ]