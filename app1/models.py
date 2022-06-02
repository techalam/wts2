
from django.db import models

# Create your models here.
class contactform(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField(max_length=122)
    message=models.TextField()
    date=models.DateField()

class join2(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=102)
    Experience=models.CharField(max_length=30)
    Message=models.TextField(max_length=400)
    Cv=models.CharField(max_length=250)
    Re=models.CharField(max_length=100)
    date=models.DateField()

