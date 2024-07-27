from django import forms
from main.models import MyUser
from django.contrib.auth.forms import UserCreationForm

class SponsorRegistrationForm(UserCreationForm):
    company_name = forms.CharField(max_length=100)
    industry = forms.CharField(max_length=100)
    budget = forms.IntegerField()

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
