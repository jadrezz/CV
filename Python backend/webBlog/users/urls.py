from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('profile/<slug:username>/', views.profile_user, name='profile'),
]
