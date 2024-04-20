from . import views
from django.urls import path, re_path


urlpatterns = [
path("rent-login/", views.renter_login, name="renter-login"),
    path("host-login/", views.provider_login, name="provider-login"),
    path('post', views.provider_form, name='provider_form'),
    path('submit', views.renter_form, name='renter_form'),
    path("", views.index, name="home"),
    path('export/', views.your_view, name='export_data'),
]