from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Record
from django import forms
from django.forms.widgets import PasswordInput, TextInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput(), label = "Użytkownik")
    password = forms.CharField(widget=PasswordInput(), label = "Hasło")


class AddRecordForm(forms.ModelForm):
    powod = forms.CharField(widget = forms.Textarea, label = "Powód", max_length = 1000)
    dotyczy = forms.CharField(widget = forms.Textarea, label = "Dotyczy", max_length = 1000)
    data_pozew = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'} ), label = "Data pozwu")
    wyrok1 = forms.CharField(widget = forms.Textarea, label = "Wyrok pierwszej instancji", max_length = 1000, required = False)
    wyrok2 = forms.CharField(widget = forms.Textarea, label = "Wyrok drugiej instancji", max_length = 1000, required = False)
    zakonczenie = forms.CharField(widget = forms.Textarea, label = "Zakończenie", max_length = 1000, required = False)
    class Meta:
        model = Record
        fields = ["powod", "dotyczy", "data_pozew", "wyrok1", "wyrok2", "egzekucja", "uwagi", "zakonczenie", "status", "kto"]



class UpdateRecordForm(forms.ModelForm):
    powod = forms.CharField(widget = forms.Textarea, label = "Powód", max_length = 1000)
    dotyczy = forms.CharField(widget = forms.Textarea, label = "Dotyczy", max_length = 1000)
    data_pozew = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'} ), label = "Data pozwu")
    wyrok1 = forms.CharField(widget = forms.Textarea, label = "Wyrok pierwszej instancji", max_length = 1000, required = False)
    wyrok2 = forms.CharField(widget = forms.Textarea, label = "Wyrok drugiej instancji", max_length = 1000, required = False)
    zakonczenie = forms.CharField(widget = forms.Textarea, label = "Zakończenie", max_length = 1000, required = False)
    class Meta:
        model = Record
        fields = ["powod", "dotyczy", "data_pozew", "wyrok1", "wyrok2", "egzekucja", "uwagi", "zakonczenie", "status", "kto"]



class SmsRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ["powod", "dotyczy", "phone", "content"]