from django.http import HttpResponse
from django.shortcuts import render
from sponsor.forms import SponsorRegistrationForm
from sponsor.models import Sponsor

# Create your views here.
def registerSponsor(request):
    form = SponsorRegistrationForm()
    if request.method == 'POST':
        form = SponsorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            sponsor = Sponsor.objects.create(
                company_name=form.cleaned_data.get('company_name'),
                industry=form.cleaned_data.get('industry'),
                budget=form.cleaned_data.get('budget')
            )
            sponsor.save()
            user.sponsor = sponsor
            user.save()
            return HttpResponse("Sponsor registered successfully")
    return render(request, 'sponsor/register_sponsor.html', {'form': form})