from django.urls import path
from requests import request
from ImageShare.views import index

urlpatterns=[
    path('/index',index(request)),
]