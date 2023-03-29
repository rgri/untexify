from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:x>/", views.quadratic, name="quadratic"),
    path("home/", views.get_drawing, name="home"),
]
