from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserA (models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no=models.CharField(primary_key=True, blank=True, max_length=255)
    branch=models.CharField(max_length=255, blank=True)
    phone=models.IntegerField(max_length=10,blank=True)


