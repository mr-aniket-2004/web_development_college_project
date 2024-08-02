from django.shortcuts import render ,HttpResponse, redirect , HttpResponseRedirect
from django.contrib.auth import logout
# Create your views here.

def index1(request):
    return render(request,"studentdesh.html")


def student_logout(request):
    logout(request)
    return render(request,"login.html")
    # return HttpResponse("back to home")


def update_info(request):
    return render(request, "update_form.html")
    # return HttpResponseRedirect('update_info')

def feedback_info(request):
    return render(request, "feedbackform.html")