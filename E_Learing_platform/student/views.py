from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from home.models import sign_up_table
# Create your views here.

def index1(request):
    return render(request,"studentdesh.html")


def student_logout(request):
    logout(request)
    return render(request,"login.html")
    # return HttpResponse("back to home")


def update_info(request):
    if request.method == "POST":
        profile_pic = request.POST.get('profile-photo')
        frist_name= request.POST.get('Frist_Name')
        last_name = request.POST.get('Last_Name')
        add = request.POST.get('Address')
        city = request.POST.get('City')
        state = request.POST.get('State')
        pincode = request.POST.get('Pincode')
        parent_no = request.POST.get('p_no')
        parent_email = request.POST.get('p_email')
        qualification = request.POST.get('Qualification')
        college = request.POST.get('College')
        updateinfo = sign_up_table( profile_pic=profile_pic,f_name=frist_name,s_name=last_name,add=add,city_name=city,state=state,pincode=pincode,p_mobile=parent_no,p_email=parent_email,qualification=qualification,collge_name=college)
        updateinfo.save()
    return render(request, "update_form.html")
    # return HttpResponseRedirect('update_info')

def feedback_info(request):
    return render(request, "feedbackform.html")