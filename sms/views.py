from django.shortcuts import render, redirect
from sms.forms import SmsRecordFormSms
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Mieszkaniec, Blok
from smsapi.client import SmsApiPlClient
from django.core.paginator import Paginator
from django.http import FileResponse
from itertools import chain
import io
from django.db import connection
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage


@login_required(login_url="login")
def dashboard_sms(request):
    my_records = Mieszkaniec.objects.all()
    p = Paginator(Mieszkaniec.objects.all(), 10)
    page = request.GET.get("page")
    my_record = p.get_page(page)

    return render(request, "dashboard-sms.html",
                  {"records": my_records, "my_record": my_record})


def dashboard_sms_blok(request):
    my_records = Blok.objects.all()
    p = Paginator(Blok.objects.all(), 10)
    page = request.GET.get("page")
    my_record = p.get_page(page)

    return render(request, "dashboard-sms-blok.html",
                  {"records": my_records, "my_record": my_record})


def dashboard_sms_kontrahent(request):
    my_records = Mieszkaniec.objects.all()
    p = Paginator(Mieszkaniec.objects.all(), 10)
    page = request.GET.get("page")
    my_record = p.get_page(page)

    return render(request, "dashboard-sms-kontrahent.html",
                  {"records": my_records, "my_record": my_record})

# @login_required(login_url="login")
# def dashboard_ce_sms(request):
#     my_records = Mieszkaniec.objects.all().filter(administracja="ce")
#     p = Paginator(Mieszkaniec.objects.all().filter(administracja="ce"), 10)
#     page = request.GET.get("page")
#     my_record = p.get_page(page)
#
#     return render(request, "dashboard-ce-sms.html",
#                   {"records": my_records, "my_record": my_record})


# @login_required(login_url="login")
# def dashboard_ce_sms_blok(request):
#     my_records = Blok.objects.all().filter(administracja="ce")
#     p = Paginator(Blok.objects.all().filter(administracja="ce"), 10)
#     page = request.GET.get("page")
#     my_record = p.get_page(page)
#
#     return render(request, "dashboard-ce-sms-blok.html",
#                   {"records": my_records, "my_record": my_record})


# @login_required(login_url="login")
# def dashboard_ns_sms(request):
#     my_records = Mieszkaniec.objects.all().filter(administracja="ns")
#     p = Paginator(Mieszkaniec.objects.all().filter(administracja="ns"), 10)
#     page = request.GET.get("page")
#     my_record = p.get_page(page)
#
#     return render(request, "dashboard-ns-sms.html",
#                   {"records": my_records, "my_record": my_record})


# @login_required(login_url="login")
# def dashboard_ns_sms_blok(request):
#     my_records = Blok.objects.all().filter(administracja="ns")
#     p = Paginator(Blok.objects.all().filter(administracja="ns"), 10)
#     page = request.GET.get("page")
#     my_record = p.get_page(page)
#
#     return render(request, "dashboard-ns-sms-blok.html",
#                   {"records": my_records, "my_record": my_record})


# @login_required(login_url="login")
# def dashboard_nw_sms(request):
#     my_records = Mieszkaniec.objects.all().filter(administracja="nw")
#     p = Paginator(Mieszkaniec.objects.all().filter(administracja="nw"), 10)
#     page = request.GET.get("page")
#     my_record = p.get_page(page)
#
#     return render(request, "dashboard-nw-sms.html",
#                   {"records": my_records, "my_record": my_record})


# @login_required(login_url="login")
# def dashboard_nw_sms_blok(request):
#     my_records = Blok.objects.all().filter(administracja="nw")
#     p = Paginator(Blok.objects.all().filter(administracja="nw"), 10)
#     page = request.GET.get("page")
#     my_record = p.get_page(page)
#
#     return render(request, "dashboard-nw-sms-blok.html",
#                   {"records": my_records, "my_record": my_record})



# view pozew
@login_required(login_url="login")
def view_record_sms(request, pk):
    all_records = Mieszkaniec.objects.get(id=pk)
    context = {"record": all_records}

    return render(request, "sms-view.html", context=context)



# sms pozew
@login_required(login_url="login")
def sms_record(request,  pk):
    record = Mieszkaniec.objects.get(id=pk)
    form = SmsRecordFormSms(instance=record)
    my_record = Mieszkaniec.objects.get(id=pk)



    if request.method == "POST":
        phone = request.POST.get("phone")
        content = request.POST.get("content")
        form = SmsRecordFormSms(request.POST, instance=record)
        to_remov = {"ą": "a", "Ą": "A", "ś": "s", "Ś": "S",
                    "ę": "e", "Ę": "E", "Ł": "L", "ł": "l",
                    "Ó": "O", "ó": "o",
                    "Ń": "N", "ń": "n", "ć": "c", "Ć": "C",
                    "Ż": "Z", "Ź": "Z", "ż": "z", "ź": "z",
                    '„': "", '”': ""}
        for char in to_remov.keys():
            content = content.replace(char, to_remov[char])
        if request.method == "POST":
            token = "rM5DsJlOvDkbGnYnHAn9f9GmpphT0ovOywqPaiLL"
            client = SmsApiPlClient(access_token=token)
            send_results = client.sms.send(to=phone,
                                           message=content,
                                           from_="SMBUDOWLANI")


            return render(request, "dashboard-sms.html",
                          {"form": form, "record": record, "my_record": my_record})

    context = {"form": form, "record": record, "my_record": my_record}
    return render(request, "sms-sms.html", context=context)



# search pozew
@login_required(login_url="login")
def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        my_records = Mieszkaniec.objects.filter(nazwa__contains=searched) | Mieszkaniec.objects.filter(
            indeks__contains=searched) | Mieszkaniec.objects.filter(adres__contains=searched)
        return render(request, "sms-search.html",
                      {"searched": searched, "my_records": my_records})
    else:
        return render(request, "sms-search.html", {})


@login_required(login_url="login")
def search_kontrahent(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        my_records = Mieszkaniec.objects.filter(nazwa__contains=searched) | Mieszkaniec.objects.filter(
            indeks__contains=searched) | Mieszkaniec.objects.filter(adres__contains=searched)
        return render(request, "sms-search-kontrahent.html",
                      {"searched": searched, "my_records": my_records})
    else:
        return render(request, "sms-search-kontrahent.html", {})


@login_required(login_url="login")
def search_blok(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        my_record = Blok.objects.filter(adres_budynku__contains=searched) | Blok.objects.filter(symbol_budynku__contains=searched)
        return render(request, "sms-search-blok.html",
                      {"searched": searched, "my_records": my_record})
    else:
        return render(request, "sms-search-blok.html", {})