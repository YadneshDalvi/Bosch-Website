from django.db import models

# Create your models here.
class Services(models.Model):
    name =models.CharField(max_length=122)
    phone =models.CharField(max_length=12)
    email =models.CharField(max_length=122)
    branch =models.CharField(max_length=122)
    reason =models.CharField(max_length=500)
    # file =models.BinaryField()