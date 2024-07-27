from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import MyUser
from django.shortcuts import redirect
from django.contrib import messages
from .forms import CampaignForm
# from .models import Campaign

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']
            user = authenticate(request, username=username, password=password)
            if user is not None :
                user_type = MyUser.objects.get(username=username).user_type
                login(request, user)
                # return redirect(user_type)
                # return redirect('home') 
                return HttpResponse("<h1>Logged in %s </h1>" % user_type)
                # return HttpResponse("<h1>Logged in</h1>")
            else:
                form.add_error(None, 'Invalid username, password, or user type')
                return HttpResponse("<h1>error loggin</h1>")
                
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def create_campaign(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.sponsor = request.user.sponsor
            campaign.save()
            return redirect('campaign_list')
    else:
        form = CampaignForm()
    return render(request, 'main/create_campaign.html', {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('main:login')