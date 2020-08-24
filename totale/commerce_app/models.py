from django.db import models

# Create your models here.
class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=5000)

    def __str__(self):
        return self.name


class AdmissionModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=5000)
    course = models.CharField(max_length=100)
    phone = models.BigIntegerField()

    def __str__(self):
        return_str = self.name+", "+self.course
        return return_str
