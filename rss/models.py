from django.db import models


class Record(models.Model):
    data_utworzenia = models.DateTimeField(auto_now_add = True)
    powod = models.CharField(max_length = 500, blank = False)
    dotyczy = models.CharField(max_length = 1000, blank= False)
    data_pozew = models.DateField(blank = True)
    wyrok1 = models.TextField(max_length = 1000, blank = True)
    wyrok2 = models.TextField(max_length = 1000, blank = True)
    egzekucja = models.TextField(max_length = 1000, blank = True)
    uwagi = models.TextField(max_length = 2000, blank = True)
    zakonczenie = models.TextField(max_length = 1000, blank = True)
    zakonczono = "Zakonczono"
    w_trakcie = "W trakcie realizacji"
    status_wybor = [
        (zakonczono, "Zakonczono"),
        (w_trakcie, "W trakcie realizacji")
    ]
    status = models.CharField(
        max_length = 22,
        choices = status_wybor,
        default = zakonczono,
    )

    przeciwko = "Pozew przeciwko Spółdzielni"
    przez = "Pozew przez Spółdzielnię"
    kto_wybor = [
        (przeciwko, "Pozew przeciwko Spółdzielni"),
        (przez, "Pozew przez Spółdzielnię")
    ]
    kto = models.CharField(
        max_length = 50,
        choices = kto_wybor,
    )

    asystentka = "500524230"
    zarzad = "601521658, 601202139"
    radca = "694704533"
    it = "601521657"
    wszyscy = "601521658, 601202139, 500524230, 694704533"

    phone_wybor = [
        (asystentka, "Asystentka"),
        (zarzad, "Zarzad"),
        (radca, "Radca"),
        (it, "IT"),
        (wszyscy, "Wszyscy")
    ]
    phone = models.CharField(
        max_length = 100,
        choices = phone_wybor,
        default = zarzad,
    )
    content = models.TextField(max_length=160, blank=True)


    def __str__(self):
        return self.powod + "   " + self.dotyczy