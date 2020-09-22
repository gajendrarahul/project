from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Owner(models.Model):
    owner_name = models.CharField(max_length=100,null=True,blank=True,help_text="Enter the name here")
    bike_no = models.CharField(max_length=50,blank=False,null=False)
    licence_no = models.IntegerField()
    blood_group = models.CharField(max_length=10,null=False,blank=False)
    last_tax_paid = models.DateField()

    def __str__(self):
        return self.owner_name
