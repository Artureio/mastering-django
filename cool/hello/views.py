from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello, Django, from hello.views and i even used the hello.urls</h1>')
