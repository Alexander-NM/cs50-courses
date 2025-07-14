from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def alex(request):
    return HttpResponse("Hello, Alex not parameter")

def home(request):
    return HttpResponse("Home page ")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })