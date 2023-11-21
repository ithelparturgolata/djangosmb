from django.db import models
from telefony.models import Mieszkaniec


class Blok(models.Model):
    symbol_budynku = models.CharField(max_length=255, blank=False)
    adres_budynku = models.CharField(max_length=255, blank=False)
    administracja = models.CharField(max_length=2, blank=False, null=True)


    def __str__(self):
        return self.powod + "   " + self.dotyczy

