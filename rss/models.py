from django.db import models


#
class Record(models.Model):
    data_utworzenia = models.DateTimeField(auto_now_add = True)
    powod = models.TextField(max_length = 500, blank = False)
    dotyczy = models.TextField(max_length=1000, blank= False)
    data_pozew = models.DateField(blank=True)
    wyrok1 = models.TextField(max_length=1000, blank=True)
    wyrok2 = models.TextField(max_length=1000, blank=True)
    egzekucja = models.TextField(max_length=1000, blank=True)
    uwagi = models.TextField(max_length=2000, blank=True)
    zakonczenie = models.TextField(max_length=1000, blank = True)
    zakonczono = "Zakonczono"
    w_trakcie = "W trakcie realizacji"
    status_wybor = [
        (zakonczono, "Zakonczono"),
        (w_trakcie, "W trakcie realizacji")
    ]
    status = models.CharField(
        max_length=22,
        choices=status_wybor,
        default=zakonczono,
    )
    przeciwko = "Przeciwko"
    przez = "Przez"
    kto_wybor = [
        (przeciwko, "Przeciwko"),
        (przez, "Przez")
    ]
    kto = models.CharField(
        max_length=22,
        choices=kto_wybor,
    )

    def __str__(self):
        return self.powod + "   " + self.dotyczy