from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def course(request):
    return render(request, "course.html")

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