from django.db import models

# Create your models here.
class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=5000)


class AdmissionModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=5000)
    course = models.CharField(max_length=100)
    phone = models.BigIntegerField()
