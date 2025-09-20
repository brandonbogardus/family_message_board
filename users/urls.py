from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),  # Place this first!
    path("", include("django.contrib.auth.urls")),
]
