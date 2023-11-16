from django.db import models



class Mieszkaniec(models.Model):
    data_utworzenia = models.DateTimeField(auto_now_add=True)

