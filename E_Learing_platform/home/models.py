from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    fname= models.CharField(max_length=120)
    sname= models.CharField(max_length=120)
    email= models.CharField(max_length=120)
    phoneno = models.CharField(max_length=15)
    desc = models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.fname

class course(models.Model):
    product_name= models.CharField(max_length=200)
    price =models.CharField(max_length=100)
    img =models.ImageField(upload_to='img')
    duration =models.CharField(max_length=120)
    info= models.CharField(max_length=200)
    button =models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.product_name


class sign_up_table (models.Model):
    main = models.OneToOneField(User,on_delete= models.CASCADE)
    mobile = models.IntegerField()
    profile_pic = models.ImageField(upload_to='profiles')
    f_name = models.CharField(max_length=120)
    s_name = models.CharField(max_length=200)
    add = models.CharField(max_length=500)
    city_name = models.CharField(max_length=100)
    state =models.CharField(max_length=50)
    pincode = models.IntegerField()
    p_mobile = models.CharField(max_length=15)
    p_email =models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    collge_name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.main.username
