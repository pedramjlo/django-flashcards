from django.urls import path, include

from .views import logout

urlpatterns = [
    path("logout/", logout, name='logout'),

]
