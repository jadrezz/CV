from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView

from users.forms import LoginForm, RegistrationUser
from users.models import MyUser


# Create your views here.
# class LoginUser(LoginView):
#     template_name = 'users/login.html'
#     form_class = LoginForm
#

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user and user.is_active:
                    login(request, user)
                    return HttpResponseRedirect((request.GET.get('next')) or reverse('home'))
        else:
            form = LoginForm()
        return render(request, 'users/login.html',
                          {'form': form})
    else:
        return redirect('home')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def profile_user(request, username):
    user_profile = get_object_or_404(MyUser, username=username)
    return render(request, 'users/profile.html', {'user_profile': user_profile})



class Register(CreateView):
    form_class = RegistrationUser
    template_name = 'users/register.html'

    def get_success_url(self):
        messages.success(self.request, 'Аккаунт успешно зарегистрирован!')
        return reverse_lazy('users:login')


