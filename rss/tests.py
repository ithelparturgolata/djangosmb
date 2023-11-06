from django.test import TestCase, Client
from django.urls import reverse
from rss.models import Record
import json


# test viewsy
class TestViews(TestCase):
    def test_dashboard_POST(self):
        client = Client()
        response = client.post(reverse("dashboard"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "rss/dashboard.html")
