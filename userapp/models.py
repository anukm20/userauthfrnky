from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Products(models.Model):
    name=models.CharField( max_length=50)
    image=models.ImageField(upload_to='images')
    def __str__(self):
        return self.name

class UserDetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images')
    phone=models.IntegerField()
    destination=models.CharField(max_length=50)
    experience=models.IntegerField()
