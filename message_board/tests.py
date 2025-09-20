from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Message


class MesageBoardTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass"
        )
        self.message = Message.objects.create(author=self.user, message="Hello!")

    def test_message_str(self):
        self.assertEqual(str(self.message), "Hello!")

    def test_message_list_view_logged_in(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("message_board:message_board"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello!")

    def test_message_list_view_anonymous(self):
        response = self.client.get(reverse("message_board:message_board"))
        self.assertNotEqual(response.status_code, 200)

    def test_add_message_view_logged_in(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse("message_board:add_message"), {"message": "Another message"}
        )
        self.assertEqual(Message.objects.count(), 2)

    def test_add_message_view_anonymous(self):
        response = self.client.get(reverse("message_board:add_message"))
        self.assertNotEqual(response.status_code, 200)  # Or check for redirect

    def test_messages_order_newest_first(self):
        self.client.login(username="testuser", password="testpass")  # Ensure user is logged in
        newer_message = Message.objects.create(author=self.user, message="Newest message!")
        response = self.client.get(reverse("message_board:message_board"))
        messages = list(response.context["messages"])
        self.assertEqual(messages[0], newer_message)
        self.assertEqual(messages[1], self.message)
