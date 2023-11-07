from django.test import SimpleTestCase
from django.urls import resolve, reverse
from rss.views import dashboard, dashboard_przeciw, dashboard_przez, create_record, pdf, search


# testy urls
class TestUrls(SimpleTestCase):
    def test_create_url_is_resolved(self):
        url = reverse("create")
        print(resolve(url))
        self.assertEqual(resolve(url).func, create_record)

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

    def test_pdf_przez_url_is_resolved(self):
        url = reverse("pdf")
        print(resolve(url))
        self.assertEqual(resolve(url).func, pdf)

    def test_search_przez_url_is_resolved(self):
        url = reverse("search")
        print(resolve(url))
        self.assertEqual(resolve(url).func, search)