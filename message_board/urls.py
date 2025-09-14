from django.urls import path
from . import views

app_name = "message_board"

urlpatterns = [
    path("", views.MessageView.as_view(), name="message_board"),
    path("add/", views.add_message, name="add_message"),
]
