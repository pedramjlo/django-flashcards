from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


# form for handling user login
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]


# form for handling user registry
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]