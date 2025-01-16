from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import FormView

from django.contrib.auth.models import User

from .forms import LoginForm, SignupForm



class LoginView(FormView):
    form_class = LoginForm
    template_name = 'auth/login.html'
    success_url = "/home"


    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.success_url)
        else:
            return render(self.request, self.template_name, {'form': form, 'error': 'Invalid credentials'})



class SignupView(FormView):
    form_class = SignupForm
    template_name = 'auth/signup.html'
    success_url = "/home"


    def form_valid(self, form):
        user=form.save()
        user.set_password(form.cleaned_data["password1"]) 
        user.save()
        login(self.request, user)
        return redirect(self.success_url)
    