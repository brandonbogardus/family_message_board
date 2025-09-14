from django.urls import path, include
from . import views

app_name = "users"

urlpatterns = [
    path("logout/", views.custom_logout, name="logout"),  # Place this first!
    path("", include("django.contrib.auth.urls")),
]
