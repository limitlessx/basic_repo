#app route controller
from django.conf.urls import url, include
from .import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'(?P<number>\d+)$py', views.show_digit),
    url(r'(?P<number>\d+)/edit$', views.edit),
    url(r'(?P<number>\d+)/delete$', views.delete),

]

