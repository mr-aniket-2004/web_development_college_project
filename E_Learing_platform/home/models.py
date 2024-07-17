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