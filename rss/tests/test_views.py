from django.test import TestCase, Client
from django.urls import reverse
from rss.models import Record
import json


# testy views
class TestViews(TestCase):
    def view_records_GET(self):
        client = Client
        response = client.get(reverse(viewname="view_test"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "rss/dashboard.html")