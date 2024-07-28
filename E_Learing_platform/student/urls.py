from django.contrib import admin
from django.urls import path
from student import views
# from home import views


urlpatterns = [
   path("stud",views.index1,name='dashboard'),
#    path("log",views.student_logout,name='log'),
]