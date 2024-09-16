from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'auth'}),
                               label='Логин')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'auth'}),
                               label='Пароль')

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class RegistrationUser(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'auth'}),)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'auth'}),)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'auth'}),)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']




