from django.contrib.auth import logout
from django.shortcuts import render, redirect


def custom_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("message_board:message_board")  # Redirect after logout
    return redirect("message_board:message_board")
