from django.db import models
from datetime import date

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=20, null=True)
    num_employees = models.IntegerField()
    num_tables = models.IntegerField()
    num_chairs = models.IntegerField()

    def __str__(self):
        return self.name
