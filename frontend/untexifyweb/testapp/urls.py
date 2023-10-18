from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_drawing_bootstrap, name="bootstrap"),
    path("bootstrap/", views.get_drawing_bootstrap, name="bootstrap"),
]
