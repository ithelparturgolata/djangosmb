from django.shortcuts import render, redirect
from telefony.forms import AddRecordFormTelefony, \
    UpdateRecordFormTelefony, SmsRecordFormTelefony
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Mieszkaniec
from smsapi.client import SmsApiPlClient
from django.core.paginator import Paginator
from django.http import FileResponse
import io
from django.db import connection
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage


@login_required(login_url="login")
def dashboard_telefony(request):
    my_records = Mieszkaniec.objects.all()
    p = Paginator(Mieszkaniec.objects.all(), 10)
    page = request.GET.get("page")
    my_record = p.get_page(page)

    return render(request, "dashboard-telefony.html",
                  {"records": my_records, "my_record": my_record})


@login_required(login_url="login")
def dashboard_ce(request):
    my_records = Mieszkaniec.objects.all().filter(administracja="ce")
    p = Paginator(Mieszkaniec.objects.all().filter(administracja="ce"), 10)
    page = request.GET.get("page")
    my_record = p.get_page(page)

    return render(request, "dashboard-ce.html",
                  {"records": my_records, "my_record": my_record})


@login_required(login_url="login")
def dashboard_ns(request):
    my_records = Mieszkaniec.objects.all().filter(administracja="ns")
    p = Paginator(Mieszkaniec.objects.all().filter(administracja="ns"), 10)
    page = request.GET.get("page")
    my_record = p.get_page(page)

    return render(request, "dashboard-ns.html",
                  {"records": my_records, "my_record": my_record})


@login_required(login_url="login")
def dashboard_nw(request):
    my_records = Mieszkaniec.objects.all().filter(administracja="nw")
    p = Paginator(Mieszkaniec.objects.all().filter(administracja="nw"), 10)
    page = request.GET.get("page")
    my_record = p.get_page(page)

    return render(request, "dashboard-nw.html",
                  {"records": my_records, "my_record": my_record})


# add pozew
@login_required(login_url="login")
def create_record(request):
    form = AddRecordFormTelefony()
    if request.method == "POST":

        form = AddRecordFormTelefony(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Dodano Kontrahenta")
            return redirect("dashboard_telefony")
    context = {"form": form}
    return render(request, "telefony-create.html", context=context)


# update pozew
@login_required(login_url="login")
def update_record(request, pk):
    record = Mieszkaniec.objects.get(id=pk)
    form = UpdateRecordFormTelefony(instance=record)
    all_records = Mieszkaniec.objects.get(id=pk)

    if request.method == 'POST':
        form = UpdateRecordFormTelefony(request.POST, instance=record)

        if form.is_valid():
            form.save()
            messages.success(request, "Zaktualizowano Kontrahenta")
            return redirect("dashboard_telefony")

    # context = {"form": form}
    return render(request, "telefony-update.html",
                  {"form": form, "record": record, "all_records": all_records})


# view pozew
@login_required(login_url="login")
def view_record(request, pk):
    all_records = Mieszkaniec.objects.get(id=pk)
    context = {"record": all_records}

    return render(request, "telefony-view.html", context=context)


# delete pozew
@login_required(login_url="login")
def delete(request, pk):
    record = Mieszkaniec.objects.get(id=pk)
    record.delete()
    messages.success(request, "Skasowano Kontrahenta")
    return redirect("dashboard_telefony")


# sms pozew
@login_required(login_url="login")
def sms_record(request, pk):
    record = Mieszkaniec.objects.get(id=pk)
    form = SmsRecordFormTelefony(instance=record)
    my_record = Mieszkaniec.objects.get(id=pk)

    if request.method == "POST":
        phone = request.POST.get("phone")
        content = request.POST.get("content")
        form = SmsRecordFormTelefony(request.POST, instance=record)
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
            my_records = Mieszkaniec.objects.all()
            p = Paginator(Mieszkaniec.objects.all(), 10)
            page = request.GET.get("page")
            my_record = p.get_page(page)

            return render(request, "telefony-sms.html",
                          {"form": form, "record": record,
                           "my_record": my_record})

    context = {"form": form, "record": record, "my_record": my_record}
    return render(request, "telefony-sms.html", context=context)


# pdf pozew
@login_required(login_url="login")
def pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    records = Mieszkaniec.objects.all()
    lines = []

    for record in records:
        lines.append(record.powod)
        lines.append(record.dotyczy)
        lines.append(record.wyrok1)
        lines.append(record.wyrok2)
        lines.append(record.egzekucja)
        lines.append(record.uwagi)
        lines.append(record.zakonczenie)
        lines.append(record.status)
        lines.append("#######################################")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="raport.pdf")


# search pozew
@login_required(login_url="login")
def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        my_records = Mieszkaniec.objects.filter(nazwa__contains=searched) | Mieszkaniec.objects.filter(indeks__contains=searched) | Mieszkaniec.objects.filter(adres__contains=searched)

        return render(request, "telefony-search.html",
                      {"searched": searched, "my_records": my_records})
    else:
        return render(request, "telefony-search.html", {})
