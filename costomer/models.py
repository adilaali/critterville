from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class SignUp(models.Model):
    FirstName=models.CharField(max_length=255)
    LastName=models.CharField(max_length=255)
    Phone_Number=models.CharField(max_length=15)
    Email=models.EmailField()
    Pass_word=models.CharField(max_length=15)

    def __str__(self):
        return self.FirstName
    
    


    