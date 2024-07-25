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

class course(models.Model):
    product_name= models.CharField(max_length=200)
    categroy =models.CharField(max_length=200)
    price =models.CharField(max_length=100)
    img =models.ImageField(upload_to='img')
    duration =models.CharField(max_length=120)
    info= models.CharField(max_length=200)
    button =models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.product_name

# class Sign(models.Model):
#     fname=models.CharField(max_length=120)
#     email= models.EmailField(max_length=120)
#     password = models.CharField(max_length=50)
#     password1 = models.CharField(max_length=60)
#     date =models.DateField()
#     def __str__(self):
#         return self.fname
    
# class log(models.Model):
#     email=models.EmailField(max_length=120)
#     password =models.CharField(max_length=100)
#     date =models.DateField()
#     def __str__(self):
#         return self.email