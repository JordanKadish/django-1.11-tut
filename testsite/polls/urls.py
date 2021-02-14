from django.conf.urls import url

from . import views

urlpatterns = [
    # takes anything until the end of string and gets the index view in views.py
    url(r'^$', views.index, name='index'),
]