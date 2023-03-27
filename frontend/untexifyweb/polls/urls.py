# this file is called a "URLconf"
from django.urls import path
from . import views

urlpatterns = [path("", views.index, name="index")]
