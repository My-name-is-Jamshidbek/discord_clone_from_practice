from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("abouts/", views.abouts, name="abouts"),
    path("about/<int:pk>/", views.about, name="about"),
]
