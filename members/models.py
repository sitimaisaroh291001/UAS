from django.db import models

# Create your models here.

class Member(models.Model):
    input1=models.CharField(max_length=100)
    input2=models.CharField(max_length=100)
    input3=models.CharField(max_length=100)