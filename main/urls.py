from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from .views import login_view

app_name = 'main'

urlpatterns = [
    # path('login/', views.loginUser, name='login'),
    # path('login/',views.loginUser, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('campaigns/create/', create_campaign, name='create_campaign'),
    # path('campaigns/', campaign_list, name='campaign_list'),
]