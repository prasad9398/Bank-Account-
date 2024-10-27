from django.db import models

# Create your models here.
class Withdraw(models.Model):
    name=models.CharField(max_length=1000)
    accountno=models.IntegerField()
    contact=models.CharField(max_length=1000)
    address=models.CharField(max_length=1000)
    amount=models.CharField(max_length=1000)

class Deposite(models.Model):
    name=models.CharField(max_length=1000)
    accountno=models.IntegerField()
    contact=models.CharField(max_length=1000)
    address=models.CharField(max_length=1000)
    amount=models.CharField(max_length=1000)
