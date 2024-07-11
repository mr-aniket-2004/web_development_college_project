from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name= "home"),
    path("about/",views.course, name= "about"),
    path("home/",views.index, name="home"),
    path("about/python/",views.python,name="python"),
    path("about/java/",views.java,name="java")
]
