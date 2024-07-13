from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def course(request):
    return render(request, "course.html")

def community(request):
    return render(request, "community.html")

def contactus(request):
    return render(request, "contact-us.html")

def log(request):
    return render(request, "log-sign.html")

def python(request):
    context ={
        "var":"Aniket Chandiwade"
    }
    return render(request, "python.html",context)

def java(request):
    context ={
        "var":"this is java"
    }
    return render(request, "python.html",context)