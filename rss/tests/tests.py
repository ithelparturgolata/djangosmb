from django.test import TestCase, Client
from rss.models import Record
import json


class BasicTest(TestCase):
    def test_entry(self):
        name=Record()
        name.powod="Test z unittestu"
        name.dotyczy = "Firma z unitestu"
        name.data_pozew = "2023-11-06"
        name.save()


        record=Record.objects.get(pk=name.id)
        self.assertEqual(record,name)
