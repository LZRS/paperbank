""" The paper app urls """

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^', views.main, name='main_page'),
]

