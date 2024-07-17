from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name= "home"),
    path("home/",views.index, name="home"),
    path("about/",views.course, name= "about"),
    path("community/",views.community, name= "community"),
    path("contact-us/",views.contactus, name= "contact-us"),
    path("log/",views.log, name= "log"),
    # path("home/contact-us/",views.contactus, name="contact-us"),
    # path("home/community/",views.community, name="community"),
    path("python/",views.python,name="python"),
    path("java/",views.java,name="java")
]
