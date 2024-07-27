from django.db import models

# Create your models here.
class Sponsor(models.Model):
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    budget = models.IntegerField()