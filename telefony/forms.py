from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Mieszkaniec
from django import forms
from django.forms.widgets import PasswordInput, TextInput, FileInput


class AddRecordFormTelefony(forms.ModelForm):
    indeks = forms.CharField(label="Indeks", max_length=7)
    nazwa = forms.CharField(label="Nazwisko i Imię", max_length=255)
    adres = forms.CharField(label="Adres", max_length=255)
    klatka = forms.CharField(label="Klatka",
                             max_length=2)
    telefon = forms.CharField(label="Telefon",
                              max_length=9)
    zgoda = forms.CharField(label="Zgoda",
                            max_length=3)
    administracja = forms.CharField(label="Administracja",
                                    max_length=2)

    class Meta:
        model = Mieszkaniec
        fields = ["indeks", "nazwa", "adres", "klatka",
                  "telefon", "zgoda", "administracja"]


class UpdateRecordFormTelefony(forms.ModelForm):
    nazwa = forms.CharField(label="Nazwisko i Imię", max_length=255)
    klatka = forms.CharField(label="Klatka",
                             max_length=2)
    telefon = forms.CharField(label="Telefon",
                              max_length=9)
    zgoda = forms.CharField(label="Zgoda tak/nie",
                            max_length=3)

    class Meta:
        model = Mieszkaniec
        fields = ["nazwa", "klatka", "telefon", "zgoda"]


class SmsRecordFormTelefony(forms.ModelForm):
    class Meta:
        model = Mieszkaniec
        fields = ["indeks", "nazwa", "phone", "content", "telefon"]
