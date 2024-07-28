import uuid
from django import forms
from .models import Adrequest

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ['username', 'password']

from .models import Campaign
class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'description', 'start_date', 'end_date', 'budget', 'visibility', 'campaign_image']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'grow textarea textarea-bordered', 'placeholder': 'Description of the campaign'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'visibility': forms.Select(attrs={'class': 'select select-bordered w-full grow'}),
            'campaign_image': forms.FileInput(attrs={'class': 'grow file-input file-input-bordered w-full'})
        }
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if 'campaign_image' in self.cleaned_data and self.cleaned_data['campaign_image']:
            file = self.cleaned_data['campaign_image']
            ext = file.name.split('.')[-1]
            unique_filename = f"{uuid.uuid4()}.{ext}"
            file.name = unique_filename
            instance.campaign_image = file
        if commit:
            instance.save()
        return instance

class AdrequestForm(forms.Form):
    name = forms.CharField(max_length=20)
    requirements = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={
        'class': 'grow textarea textarea-bordered',
        'placeholder': 'Enter the requirements of the ad request',
    }))
    amount = forms.IntegerField()
    msg = forms.CharField(max_length=200)
    username = forms.CharField(max_length=150)

