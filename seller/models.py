from django.db import models
from adminapp.models import Category
from costomer.models import SignUp
# Create your models here.

class PetDetails(models.Model):
    Username=models.ForeignKey(SignUp,on_delete=models.CASCADE,default='')
    Name = models.CharField(max_length=250)
    Category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    Breed = models.CharField(max_length=250)
    Gender = models.CharField(max_length=250)
    Age = models.CharField(max_length=250)
    Size = models.CharField(max_length=250)
    Weight = models.CharField(max_length=250)
    Health = models.CharField(max_length=250)
    Location = models.CharField(max_length=250)
    Photo1 = models.ImageField(upload_to='media/',null=True,blank=True)
    Photo2 = models.ImageField(upload_to='media/',null=True,blank=True)
    Contact_No = models.CharField(max_length=10)
    Description = models.TextField(blank=True)
    Price = models.CharField(max_length=250)
    Uploaded_at = models.DateTimeField(auto_now_add=True)
    
    


