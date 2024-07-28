from django.urls import path
from . import views
# import main

app_name = 'influencer'

urlpatterns = [
    # path('register/', views.registerUser, name='register'),
    path('register/', views.register_influencer, name='register'),
    path('home/', views.home, name='home'),
    # path('login/', , name='login'),
    # path('campaigns/', views.campaign_list, name='campaign_list'),
    # path('campaigns/<int:pk>/', views.campaign_detail, name='campaign_detail'),
    # path('campaigns/<int:pk>/apply/', views.apply_for_campaign, name='apply_for_campaign'),
    path('campaigns/', views.public_campaign_list, name='public_campaign_list'),
    path('campaigns/<int:pk>/', views.campaign_detail, name='public_campaign_detail'),
]
