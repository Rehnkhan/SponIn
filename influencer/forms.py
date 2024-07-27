from django import forms
from main.models import MyUser
from django.contrib.auth.forms import UserCreationForm

class InfluencerRegistrationForm(UserCreationForm):
    category = forms.CharField(max_length=100)
    niche = forms.CharField(max_length=100)
    reach = forms.IntegerField()

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
