from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from telefony.models import Mieszkaniec
from django import forms
from django.forms.widgets import PasswordInput, TextInput, FileInput



class SmsRecordFormSms(forms.ModelForm):
    class Meta:
        model = Mieszkaniec
        content = forms.CharField(widget=forms.Textarea,
                            label="Telefon", max_length=1000)
        phone = forms.CharField(widget=forms.Textarea,
                            label="Tekst", max_length=9)
        fields = ["phone", "content"]