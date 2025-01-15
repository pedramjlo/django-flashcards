from django.shortcuts import render, redirect
from django.contrib.auth import logout



def logout(request):
    logout(request)
    return redirect('home')