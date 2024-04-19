from . import views
from django.urls import path, re_path

urlpatterns = [
    path("", views.index, name="home"),
    path("new/", views.login, name="login"),
]