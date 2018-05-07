#app route controller
from django.conf.urls import url, include
from .import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^test$', views.test)

]

