from django.shortcuts import render
from django.views.generic import ListView

from .models import Category

class AllCategoriesView(ListView):
    template_name = 'flashcards/all-categories.html'
    model = Category
