from django.db import models



class Mieszkaniec(models.Model):
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    indeks = models.CharField(max_length=7, blank=True)
    nazwa = models.CharField(max_length=255, blank=True)
    adres = models.CharField(max_length=255, blank=True)
    klatka = models.CharField(max_length=2, blank=True)
    telefon = models.CharField(max_length=9, blank=True)
    tak = "tak"
    nie = "nie"
    zgoda_wybor = [
        (tak, "tak"),
        (nie, "nie")
    ]
    zgoda = models.CharField(
        max_length=3,
        choices=zgoda_wybor,
        default=tak,
    )
    ce = "CE"
    nw = "NW"
    ns = "NS"
    administracja_wybor = [
        (ns, "NS"),
        (nw, "NW"),
        (ce, "CE")
    ]
    administracja = models.CharField(
        max_length=2,
        choices=administracja_wybor,
        default=ce,
    )
    content = models.TextField(max_length=160, blank=True)
    phone = models.TextField(max_length=9, blank=True)

    def __str__(self):
        return self.nazwa + "   " + self.telefon + "  " + self.zgoda