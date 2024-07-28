from django.urls import path
from . import views

app_name = 'sponsor'

urlpatterns = [
    path('register/', views.registerSponsor, name='register'),
    path('', views.home, name='home'),
    path('find_influencers/', views.find_influencers, name='find_influencers'),
    path('campaign/<int:pk>', views.sponsor_campaign_list, name='sponsor_campaign_list'),
]