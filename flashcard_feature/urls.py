from django.urls import path
from .views import AllCategoriesView

urlpatterns = [
    path("all-categories/", AllCategoriesView.as_view(), name='all-categories'),
]
