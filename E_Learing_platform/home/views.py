from django.shortcuts import render , redirect , HttpResponse
from datetime import datetime
from .models import Contact ,course
from django.contrib import messages
from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, "index.html")

def course1(request):
    if 'put' in request.GET:
        put =request.GET['put']
        cour =course.objects.filter(product_name__icontains=put)
    else :
            cour= course.objects.all()

    context ={
        'cour':cour
    }
    return render(request, "course.html",context)

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



def sign(request):
    # if request.method == "POST":
    #     username = request.POST.get('username')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     password1 = request.POST.get('password1')
    #     if password == password1:
    #         myuser = User.objects.create_user(username=username,email=email,password=password)
    #         myuser.save()
    #         return redirect('log')
    #     else:
            # return HttpResponse("password and confirm not same")
    return render(request, "singup.html")   


def log(request):
    # if request.method == "POST":
    #     username=request.POST.get('username')
    #     password = request.POST.get('password')
    #     key_user = authenticate(request,username=username,password=password)
    #     if key_user is not None:
    #         login(request,key_user)
    #         return redirect('home')
    #     else:
    #         return HttpResponse("worng info")
    return render(request, "login.html")


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