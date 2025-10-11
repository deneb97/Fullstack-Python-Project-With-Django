from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Feedback(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50,null=True,blank=True)
    address=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=10)
    feedback=models.CharField(max_length=250)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"




