from django.db import models

# Create your models here.

class Login(models.Model):
    UserName=models.CharField(max_length=255)
    Password=models.CharField(max_length=10)

class Category(models.Model):
    Name=models.CharField(max_length=50)
    Image=models.ImageField(upload_to='media/',null=True,blank=True)
    
    def __str__(self):
        return self.Name

    