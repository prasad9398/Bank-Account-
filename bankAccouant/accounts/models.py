from django.db import models

# Create your models here.
class AccountHolder(models.Model):
    name=models.CharField(max_length=1000)
    accountno=models.IntegerField()
    contact=models.CharField(max_length=1000)
    address=models.CharField(max_length=1000)
