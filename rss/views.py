from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, \
    AddRecordForm, UpdateRecordForm, SmsRecordForm, UploadFileForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Record
from smsapi.client import SmsApiPlClient
from django.core.paginator import Paginator
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# homepage view
def home(request):
    return render(request, ("rss/index.html"))


# register view
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "rss/register.html", context=context)


# login view
def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "Zalogowano")

                return redirect("dashboard")

    context = {"form": form}
    return render(request, "rss/login.html", context=context)


# logout view
def logout_view(request):
    auth.logout(request)
    messages.success(request, "Wylogowano")
    return redirect("login")


# dashboard view
@login_required(login_url="login")
def dashboard(request):
    my_records = Record.objects.all()
    p = Paginator(Record.objects.all(), 10)
    page = request.GET.get("page")
    my_record = p.get_page(page)

    return render(request, "rss/dashboard.html",
                  {"records": my_records, "my_record": my_record})


@login_required(login_url="login")
def dashboard_przeciw(request):
    my_records = Record.objects.all()
    p = Paginator(Record.objects.all(), 10)
    page = request.GET.get("page")
    my_record = p.get_page(page)

    return render(request, "rss/dashboard-przeciw.html",
                  {"records": my_records, "my_record": my_record})


@login_required(login_url="login")
def dashboard_przez(request):
    my_records = Record.objects.all()
    p = Paginator(Record.objects.all(), 10)
    page = request.GET.get("page")
    my_record = p.get_page(page)

    return render(request, "rss/dashboard-przez.html",
                  {"records": my_records, "my_record": my_record})


# add pozew
@login_required(login_url="login")
def create_record(request):
    form = AddRecordForm()
    if request.method == "POST":

        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Dodano pozew")
            return redirect("dashboard")
    context = {"form": form}
    return render(request, "rss/create-record.html", context=context)


# update pozew
@login_required(login_url="login")
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    all_records = Record.objects.get(id=pk)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()
            messages.success(request, "Zaktualizowano pozew")
            return redirect("dashboard")

    # context = {"form": form}
    return render(request, "rss/update-record.html", {"form": form, "record": record, "all_records": all_records})


# view pozew
@login_required(login_url="login")
def view_record(request,  pk):
    all_records = Record.objects.get(id=pk)
    context = {"record": all_records}

    return render(request, "rss/view-record.html", context=context)


# delete pozew
@login_required(login_url="login")
def delete(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, "Skasowano pozew")
    return redirect("dashboard")


# sms pozew
@login_required(login_url="login")
def sms_record(request,  pk):
    record = Record.objects.get(id=pk)
    form = SmsRecordForm(instance=record)
    my_record = Record.objects.get(id=pk)



    if request.method == "POST":
        phone = request.POST.get("phone")
        content = request.POST.get("content")
        form = SmsRecordForm(request.POST, instance=record)
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
            my_records = Record.objects.all()
            p = Paginator(Record.objects.all(), 10)
            page = request.GET.get("page")
            my_record = p.get_page(page)

            return render(request, "rss/dashboard.html",
                          {"form": form, "record": record, "my_record": my_record})

    context = {"form": form, "record": record, "my_record": my_record}
    return render(request, "rss/sms-record.html", context=context)


# pdf pozew
@login_required(login_url="login")
def pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    records = Record.objects.all()
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
        my_records = Record.objects.filter(powod__contains=searched)

        return render(request, "rss/dashboard-search.html",
                      {"searched": searched, "my_records": my_records})
    else:
        return render(request, "rss/dashboard-search.html", {})


# view pozew pliki
@login_required(login_url="login")
def view_file(request, pk):
    my_record = Record.objects.get(id=pk)
    context = {"record": my_record}

    return render(request, "rss/view-file.html", context=context)


# upload pozew pliki
@login_required(login_url="login")
def upload_file(request, pk):
    record = Record.objects.get(id=pk)
    form = UploadFileForm(instance=record)
    my_record = Record.objects.get(id=pk)

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Dodano plik")
            return redirect('view_file', pk)
    else:
        form = UploadFileForm()
    context = {"form": form, "record": record, "my_record": my_record}
    return render(request, 'rss/upload-file.html', context=context)
