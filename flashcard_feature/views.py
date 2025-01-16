from django.shortcuts import render
from django.db.models import Count

from django.views.generic import ListView

from .models import Category, Flashcard


class AllCategoriesView(ListView):
    template_name = 'flashcards/all-categories.html'
    model = Category
    context_object_name = 'categories'


    def get_queryset(self): # Annotate the queryset with the count of related flashcards 
        return Category.objects.annotate(flashcard_count=Count('flashcard'))


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flashcards"] = Flashcard.objects.all()
        return context
