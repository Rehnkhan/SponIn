from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from helpers.decorators import anonymous_required
from .forms import LoginForm, AdrequestForm
from .models import MyUser, Adrequest,Negotiate
from django.shortcuts import redirect, render, get_object_or_404, redirect
from .models import Campaign

def home(request):
    if request.user.is_authenticated:
        return redirect(request.user.user_type+':home')
    else:
        return redirect('main:login')

@anonymous_required
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None :
                user_type = MyUser.objects.get(username=username).user_type
                login(request, user)
                if user_type == 'admin':
                    return redirect('/admin')
                return redirect(user_type+':home')
            else:
                form.add_error('password', 'Invalid username or password')
                return redirect('main:login')
                
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('main:login')

@login_required
def adrequest_list(request):
    adrequests = Adrequest.objects.all()
    return render(request, 'adrequests/adrequest_list.html', {'adrequests': adrequests})

@login_required
def adrequest_detail(request, pk):
    adrequest = get_object_or_404(Adrequest, pk=pk)
    return render(request, 'adrequests/adrequest_detail.html', {'adrequest': adrequest})

@login_required
def adrequest_create(request):
    if request.method == 'POST':
        form = AdrequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adrequest_list')
    else:
        form = AdrequestForm()
    return render(request, 'adrequests/adrequest_form.html', {'form': form})

@login_required
def adrequest_update(request, pk):
    adrequest = get_object_or_404(Adrequest, pk=pk)
    if request.method == 'POST':
        form = AdrequestForm(request.POST, instance=adrequest)
        if form.is_valid():
            form.save()
            return redirect('adrequest_detail', pk=pk)
    else:
        form = AdrequestForm(instance=adrequest)
    return render(request, 'adrequests/adrequest_form.html', {'form': form})

@login_required
def adrequest_delete(request, pk):
    adrequest = get_object_or_404(Adrequest, pk=pk)
    if request.method == 'POST':
        adrequest.delete()
        return redirect('adrequest_list')
    return render(request, 'adrequests/adrequest_confirm_delete.html', {'adrequest': adrequest})

@login_required
def campaign_view(request, pk=None):
    if pk:
        campaign = get_object_or_404(Campaign, pk=pk)
        if request.method == 'POST':
            if 'accept' in request.POST:
                # Add logic to accept the campaign
                pass
            elif 'reject' in request.POST:
                # Add logic to reject the campaign
                pass
            return redirect('campaign_list')
        
        return render(request, 'main:campv.html', {'campaign': campaign})
    else:
        campaigns = Campaign.objects.all()
        return render(request, 'main:campv.html', {'campaigns': campaigns})
    

def negotiate(request):
    if request.method == 'POST':

        username=request.POST['username']
        msg=request.POST['msg']
        amt=request.POST['amt']
      

        if username and msg and amt:       
            if MyUser.objects.filter(username=username).first():
                n=Negotiate()                
                return render(request, 'main/negotiate.html', {'err': 'User does not exist'})
            else:
                return render(request, 'main/negotiate.html', {'err': 'User does not exist'})
        else:
            return render(request, 'main/negotiate.html', {'err': 'Please fill all fields'})
        
    return render(request, 'sponser/negotiate.html')
