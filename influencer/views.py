from django.http import HttpResponse
from django.shortcuts import render
from influencer.forms import InfluencerRegistrationForm
from influencer.models import Influencer

# Create your views here.
def register_influencer(request):
    form = InfluencerRegistrationForm()
    if request.method == 'POST':
        form = InfluencerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            influencer = Influencer.objects.create(
                category=form.cleaned_data.get('category'),
                niche=form.cleaned_data.get('niche'),
                reach=form.cleaned_data.get('reach')
            )
            influencer.save()
            user.influencer = influencer
            user.save()
            return HttpResponse("Influencer registered successfully")
    return render(request, 'influencer/register_influencer.html', {'form': form})
