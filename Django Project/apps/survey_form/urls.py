from django.conf.urls import url, include
from .import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^result$', views.result),
    url(r'^process$', views.surveys_process),
    url(r'^reset$', views.reset)

]