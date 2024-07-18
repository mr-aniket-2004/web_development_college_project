from django.shortcuts import *
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "index.html")

def course(request):
    return render(request, "course.html")

def community(request):
    return render(request, "community.html")

def contactus(request):
    if request.method =="POST":
        fname=request.POST.get('fname')
        sname=request.POST.get('sname')
        email=request.POST.get('email')
        phoneno=request.POST.get('phoneno')
        desc=request.POST.get('desc')
        contact = Contact(fname=fname,sname=sname,email=email,phoneno=phoneno,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your form submit sucessfully!")
    # return redirect('contact-us')
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