from django.urls import path
from ImageShare import views

urlpatterns=[
    path("", views.index, name="index"),
    path("login",views.login,name="login"),
]