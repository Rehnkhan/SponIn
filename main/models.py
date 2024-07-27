from django.db import models
from django.contrib.auth.models import AbstractUser

from influencer.models import Influencer
from sponsor.models import Sponsor

class MyUser(AbstractUser):
    email = models.EmailField()
    user_type = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('sponsor', 'Sponsor'), ('influencer', 'Influencer')], default='sponsor')

    sponsor = models.OneToOneField(Sponsor, on_delete=models.CASCADE, null=True, blank=True)
    influencer = models.OneToOneField(Influencer, on_delete=models.CASCADE, null=True, blank=True)

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    visibility = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')])
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



# class Adrequest(models.Model):
#     influencer = models.ForeignKey(MyUser, on_delete=models.CASCADE)
#     sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
#     status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)