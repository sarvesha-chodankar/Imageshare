from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'ImageShare/index.html')


def login(request):
    return HttpResponse("Hey there")
