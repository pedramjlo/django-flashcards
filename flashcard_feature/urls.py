from django.urls import path
from .views import AllCategoriesView, AllFlashcardsView

urlpatterns = [
    path("all-categories/", AllCategoriesView.as_view(), name='all-categories'),
    path("all-flashcards/", AllFlashcardsView.as_view(), name='all-flashcards'),
]
