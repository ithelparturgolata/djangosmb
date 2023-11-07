from django.test import SimpleTestCase
from django.urls import resolve, reverse
from rss.views import dashboard, dashboard_przeciw, dashboard_przez

class TestUrls(SimpleTestCase):
    def test_dasboard_url_is_resolved(self):
        url = reverse("dashboard")
        print(resolve(url))
        self.assertEqual(resolve(url).func, dashboard)

    def test_dasboard_przeciw_url_is_resolved(self):
        url = reverse("dashboard-przeciw")
        print(resolve(url))
        self.assertEqual(resolve(url).func, dashboard_przeciw)

    def test_dasboard_przez_url_is_resolved(self):
        url = reverse("dashboard-przez")
        print(resolve(url))
        self.assertEqual(resolve(url).func, dashboard_przez)