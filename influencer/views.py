from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from helpers.decorators import anonymous_required
from influencer.forms import InfluencerRegistrationForm
from influencer.models import Influencer
from main.models import Campaign
# Create your views here.
@anonymous_required
def register_influencer(request):
    form = InfluencerRegistrationForm()
    if request.method == 'POST':
        form = InfluencerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            influencer = Influencer.objects.create(
                category=form.cleaned_data.get('category'),
                niche=form.cleaned_data.get('niche'),
                reach=form.cleaned_data.get('reach')
            )
            influencer.save()
            user.user_type = 'influencer'
            user.influencer = influencer
            user.save()
            return HttpResponse("Influencer registered successfully")
    return render(request, 'influencer/register_influencer.html', {'form': form})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    campaign=Campaign.objects.filter(visibility='public')
    user = request.user
    context = {
        'username': user.username,
        'email': user.email,
        # 'campaign':campaign
        'user.profile_picture': user.profile_picture.url
        
    }
    
    return render(request, 'influencer/home.html', context)

def all_campaigns(request):
    campaign = Campaign.objects.filter(visibility='public')
    return render(request, 'influencer/all_campaigns.html', {'campaign': campaign})

from main.models import Campaign
from .models import Influencer

# @login_required
# def campaign_list(request):
#     campaigns = Campaign.objects.filter(status='open')
#     return render(request, 'influencer/campaign_list.html', {'campaigns': campaigns})

@login_required
def campaign_detail(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    if request.method == 'POST':
        campaign.influencer = request.user.influencer
        campaign.status = 'closed'
        campaign.save()
        return redirect('campaign_detail', pk=pk)
    return render(request, 'influencer/campaign_detail.html', {'campaign': campaign})

@login_required
def apply_for_campaign(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    if request.method == 'POST':
        campaign.influencer = request.user.influencer
        campaign.status = 'closed'
        campaign.save()
        return redirect('campaign_detail', pk=pk)
    return render(request, 'influencer/apply_for_campaign.html', {'campaign': campaign})


from django.shortcuts import render, get_object_or_404
from main.models import Campaign
@login_required
def public_campaign_list(request):
    campaigns = Campaign.objects.filter(status='public')
    return render(request, 'public_campaign_list.html', {'campaigns': campaigns})
@login_required
def campaign_detail(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    return render(request, 'campaign_detail.html', {'campaign': campaign})


 