from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from .views import login_view

app_name = 'main'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('campaigns', views.campaign_view, name='campaign_detail'),
    path('home/', views.home, name='home'),
    path('adrequest_create/', views.adrequest_create, name='adrequest_create'),
    path('negotiate/', views.negotiate, name='negotiate'),

]