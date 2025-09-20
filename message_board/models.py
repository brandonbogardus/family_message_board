from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    """A family message."""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return f"{self.message[:50]}"
