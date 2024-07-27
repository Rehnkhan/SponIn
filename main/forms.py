from django.forms import ModelForm
from .models import MyUser

# class LoginForm(forms.F):
#     class Meta:
#         model = MyUser
#         fields = ['username', 'password','user_type']

        
        
    # main/forms.py

from django import forms

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=[('admin', 'Admin'), ('sponsor', 'Sponsor'), ('influencer', 'Influencer')])

    class Meta:
        fields = ['username', 'password', 'user_type']

from .models import Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'description', 'start_date', 'end_date', 'budget', 'visibility']




    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']