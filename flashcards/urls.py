

from django.contrib import admin
from django.urls import path, include

from .views import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", HomeView.as_view(), name='home'),
    path("", include('user_account.urls')),

]
