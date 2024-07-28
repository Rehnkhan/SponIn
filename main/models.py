from django.db import models
from django.contrib.auth.models import AbstractUser

from influencer.models import Influencer

class MyUser(AbstractUser):
    email = models.EmailField()
    user_type = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('sponsor', 'Sponsor'), ('influencer', 'Influencer')], default='admin')

    sponsor = models.OneToOneField('Sponsor', on_delete=models.CASCADE, null=True, blank=True)
    influencer = models.OneToOneField(Influencer, on_delete=models.CASCADE, null=True, blank=True)

    profile_picture = models.ImageField(upload_to='profile_pictures/')

class Sponsor(models.Model):
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    budget = models.IntegerField()

class Negotiate(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    msg= models.CharField(max_length=500, null=True, blank=True)
    amt= models.IntegerField()
    adreq = models.ForeignKey('Adrequest', on_delete=models.CASCADE)

class Adrequest(models.Model):
    name = models.CharField(max_length=30)
    requirements = models.CharField(max_length=2000)
    influencer = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.IntegerField()
    visibility = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')])
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, null=False, blank=False)
    adrequests = models.ForeignKey(Adrequest, on_delete=models.CASCADE, null=True, blank=True)
    campaign_image = models.ImageField(upload_to='campaign_images/')
    
    def __str__(self):
        return self.name
    
