from django.shortcuts import render
from django.db.models import Count, Q
from django.utils import timezone

from django.views.generic import ListView

from .models import Category, Flashcard


class AllCategoriesView(ListView):
    template_name = 'flashcards/all-categories.html'
    model = Category
    context_object_name = 'categories'


    def get_queryset(self): # Annotate the queryset with the count of related flashcards 
        return Category.objects.annotate( 
            flashcard_count=Count('flashcard'), 
            learned_flashcard_count=Count('flashcard', filter=Q(flashcard__is_learned=True)))



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flashcards"] = Flashcard.objects.all()
        context["now"] = timezone.now()
        return context



class AllFlashcardsView(ListView):
    template_name = 'flashcards/all-flashcards.html'
    model = Flashcard
    context_object_name = 'flashcards'