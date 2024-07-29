from django.shortcuts import render , redirect , HttpResponse
from datetime import datetime
from .models import Contact ,course, sign_up_table
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

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
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile_no = request.POST.get('cont_no')
        role= request.POST.get('role')
        print(request.POST)
        # if password == password1:
        myuser = User.objects.create_user(email=email,username=username,password=password)
        if role =="teacher":
            myuser.is_staff = True
        myuser.save()
        sign_up =sign_up_table(main=myuser,mobile=mobile_no)
        sign_up.save()
        return render(request,"singup.html",{"status":"Hey, {} Registered Successfully".format(username)})
    return render(request, "singup.html")   



def check_user(request):
    if request.method =="GET":
        un=request.GET["usern"]
        check =User.objects.filter(username=un)
        if len(check)==1:
            return HttpResponse("exist")
        else:
            return HttpResponse("not exist")

def log(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password = request.POST.get('password')
        key_user = authenticate(request,username=username,password=password )
        if key_user is not None:
            login(request,key_user)
            return redirect('dashboard')
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