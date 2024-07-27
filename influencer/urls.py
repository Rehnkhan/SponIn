from django.urls import path

import main.views
from . import views
# import main

app_name = 'influencer'

urlpatterns = [
    # path('register/', views.registerUser, name='register'),
    path('register/', views.register_influencer, name='register'),
    # path('login/', , name='login'),
]