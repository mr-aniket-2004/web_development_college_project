from django.contrib import admin
from django.urls import path
from student import views
# from home import views


urlpatterns = [
   path("/student",views.index1,name='dashboard'),
   path("/update",views.update_info, name="update_info"),
   path("/feedback",views.feedback_info, name="feedback_info"),
#    path("log",views.student_logout,name='log'),
]