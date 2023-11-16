from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def home(request):
    return HttpResponse("Witaj w bazie telefonow")