from django.db import models

# Create your models here.
class LoginUser(models.Model):
   name = models.CharField(max_length=1000,unique=True)
   pas = models.CharField(max_length=1000)

   def __str__(self):
       return self.name
   

   