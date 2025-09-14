from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message
from django.views.generic import ListView


class MessageView(ListView):
    model = Message
    template_name = "message_board/message_list.html"
    context_object_name = "messages"
    queryset = Message.objects.order_by("-date_added")


@login_required
def add_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.author = request.user  # Assuming Message has an author field
            new_message.save()
            return redirect("message_board:message_board")
    else:
        form = MessageForm()
    return render(request, "message_board/add_message.html", {"form": form})
