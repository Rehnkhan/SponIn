from django.shortcuts import redirect, render  # Add this line
from helpers.decorators import anonymous_required, sponsor_required
from main.forms import AdrequestForm, CampaignForm
from sponsor.forms import SponsorRegistrationForm
from main.models import Adrequest, MyUser, Sponsor, Campaign,Negotiate
from influencer.models import Influencer
from django.contrib.auth import login
from django.http import HttpResponse

@anonymous_required
def registerSponsor(request):
    form = SponsorRegistrationForm()
    if request.method == 'POST':
        form = SponsorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            sponsor = Sponsor.objects.create(
                company_name=form.cleaned_data.get('company_name'),
                industry=form.cleaned_data.get('industry'),
                budget=form.cleaned_data.get('budget')
            )
            sponsor.save()
            user.user_type = 'sponsor'
            user.sponsor = sponsor
            user.save()
            login(request, user)
            return redirect('sponsor:home')
    return render(request, 'sponsor/register_sponsor.html', {'form': form})

@sponsor_required
def home(request):
    campaigns = Campaign.objects.filter(sponsor=request.user.sponsor)
    form = CampaignForm()
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.sponsor = request.user.sponsor
            campaign.save()
            return redirect('sponsor:home')
    return render(request, 'sponsor/home.html', {'campaigns': campaigns, 'form': form})

@sponsor_required
def find_influencers(request):
    influencers = Influencer.objects.all()
    category = request.GET.get('category')
    niche = request.GET.get('niche')
    min_reach = request.GET.get('min_reach')
    max_reach = request.GET.get('max_reach')

    if category:
        influencers = influencers.filter(category__icontains=category)
    if niche:
        influencers = influencers.filter(niche__icontains=niche)
    if min_reach:
        influencers = influencers.filter(reach__gte=min_reach)
    if max_reach:
        influencers = influencers.filter(reach__lte=max_reach)

    return render(request, 'sponsor/find_influencers.html', {'influencers': influencers})


@sponsor_required
def sponsor_campaign_list(request, pk):
    campaign = Campaign.objects.get(pk=pk)
    form = AdrequestForm()
    if request.method == 'POST':
        form = AdrequestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            requirements = form.cleaned_data['requirements']
            amount = form.cleaned_data['amount']
            message = form.cleaned_data['msg']
            username = form.cleaned_data['username']
            
            user = MyUser.objects.filter(username=username).first()
            if not user.influencer:
                return redirect('sponsor_campaign_list', pk=pk)
            ad = Adrequest.objects.create(
                influencer = user,
                status = 'pending',
                name = name,
                requirements = requirements,
            )
            quote = Negotiate.objects.create(
                user = user,
                msg = message,
                amt = amount,
                adreq = ad,
            )
            ad.save()
            quote.save()
            return redirect('main:adrequest_list')
    return render(request, 'sponsor/campaign_detail.html', {'campaign': campaign, 'form': form})
   



def quote(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)
        return HttpResponse('Thank you for your message!')