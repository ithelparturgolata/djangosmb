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
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())



class AddRecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ["powod", "dotyczy", "data_pozew", "wyrok1", "wyrok2", "egzekucja", "uwagi", "zakonczenie", "status"]



class UpdateRecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ["powod", "dotyczy", "data_pozew", "wyrok1", "wyrok2", "egzekucja", "uwagi", "zakonczenie", "status"]



class SmsRecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ["powod", "dotyczy", "data_pozew", "wyrok1", "wyrok2", "egzekucja", "uwagi", "zakonczenie", "status"]