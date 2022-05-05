from django.db import models

# Create your models here.

class usertable(models.Model):
    id=models.BigAutoField(primary_key=True)
    username=models.CharField(max_length=25)
    email=models.EmailField()
    dob=models.DateField()
    phone_num=models.BigIntegerField()
    password=models.CharField(max_length=10)
    gender=models.CharField(max_length=20,null=True)