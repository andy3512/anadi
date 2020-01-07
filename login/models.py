from django.db import models

# Create your models here.
class xeroxdetails(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    hostelname = models.CharField(max_length=100)
    roomno = models.CharField(max_length=100)
    contectno = models.CharField(max_length=100)
    
   
   