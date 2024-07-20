from django.shortcuts import render , redirect , HttpResponse
from datetime import datetime
from home.models import Contact ,Sign
from django.contrib import messages
from django.contrib.auth import authenticate, login

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
    username=Sign.email
    pass1=Sign.password
    if request.method == "POST":
        email=request.POST.get('email')
        password = request.POST.get('password')
        user =authenticate(request,email==username,password==pass1)
        if user is not None:
            return redirect('home')
        else:
            return HttpResponse("user not found")
    return render(request, "login.html")

def sign(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if password == password1:
            main = Sign(fname=fname,email=email,password=password,password1=password1,date=datetime.today())
            main.save()
            return redirect('log')
        else:
            return HttpResponse("password and confirm not same")
    return render(request, "singup.html")   

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