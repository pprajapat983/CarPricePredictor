from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.


class car(models.Model):
    #car_id = models.AutoField(default=0)
    car_name=models.CharField(max_length=50)
    year=models.IntegerField(default=0)
    car_type=models.CharField(max_length=50,default="SEDAN")
    selling_price=models.IntegerField(default=0)
    present_price=models.IntegerField(default=0)
    kms_driven=models.IntegerField(default=0)
    pub_date = models.DateField(default=datetime.date.today)
    owner=models.CharField(max_length=100)
    fuel_type=models.CharField(max_length=50)
    phone=models.IntegerField(default=0)
    image=models.ImageField(upload_to="car/images",default="")

    def __str__(self):
        return self.car_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key="True")
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.name        