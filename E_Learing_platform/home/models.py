from django.db import models

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


class Sign(models.Model):
    fname=models.CharField(max_length=120)
    email= models.EmailField(max_length=120)
    password = models.CharField(max_length=50)
    password1 = models.CharField(max_length=60)
    date =models.DateField()
    def __str__(self):
        return self.fname
    
class log(models.Model):
    fk = models.ForeignKey(Sign,on_delete=models.CASCADE)
    email=models.EmailField(max_length=120)
    password =models.CharField(max_length=100)
    date =models.DateField()
    def __str__(self):
        return self.email