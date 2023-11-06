from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, AddRecordForm, UpdateRecordForm, SmsRecordForm
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
from django.db.models import Q

# homepage view
def home(request):
    return render(request, ("rss/index.html"))


#register view
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect()

    context = {"form": form}
    return render(request, "rss/register.html", context = context)

#login view
def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username = username, password = password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")

    context = {"form": form}
    return render(request, "rss/login.html", context = context)


# logout view
def logout_view(request):
    auth.logout(request)
    return redirect("login")


# dashboard view
@login_required(login_url = "login")
def dashboard(request):
    my_records = Record.objects.all()
    p = Paginator(Record.objects.all(), 10)
    page = request.GET.get("page")
    my_record = p.get_page(page)

    return render(request, "rss/dashboard.html", {"records": my_records, "my_record": my_record})



@login_required(login_url = "login")
def dashboard_przeciw(request):
    my_records = Record.objects.all()
    p = Paginator(Record.objects.all(), 10)
    page = request.GET.get("page")
    my_record = p.get_page(page)

    return render(request, "rss/dashboard-przeciw.html", {"records": my_records, "my_record": my_record})



@login_required(login_url = "login")
def dashboard_przez(request):
    my_records = Record.objects.all()
    p = Paginator(Record.objects.all(), 10)
    page = request.GET.get("page")
    my_record = p.get_page(page)

    return render(request, "rss/dashboard-przez.html", {"records": my_records, "my_record": my_record})




# add pozew
@login_required(login_url = "login")
def create_record(request):
    form = AddRecordForm()
    if request.method == "POST":

        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("dashboard")
    context = {'form': form}
    return render(request, 'rss/create-record.html', context=context)


# update pozew
@login_required(login_url = "login")
def update_record(request,  pk):
    record = Record.objects.get(id = pk)
    form = UpdateRecordForm(instance = record)

    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance = record)

        if form.is_valid():
            form.save()

        return redirect("dashboard")

    context = {"form": form}
    return render(request, "rss/update-record.html", context = context)


# view pozew
@login_required(login_url = "login")
def view_record(request,  pk):
    all_records = Record.objects.get(id = pk)
    context = {"record": all_records}

    return render(request, "rss/view-record.html", context = context)


# delete pozew
@login_required(login_url='my-login')
def delete(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()

    return redirect("dashboard")


# sms pozew
@login_required(login_url = "login")
def sms_record(request,  pk):
    pass



# pdf pozew
def pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    # lines = [
    #     "To jest linia 1",
    #     "To jest linia 2",
    #     "To jest linia 3",
    # ]
    records = Record.objects.all()
    lines = []

    for record in records:
        lines.append(record.powod)
        lines.append(record.dotyczy)
        # lines.append(record.data_pozew)
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


#search pozew
def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        my_records = Record.objects.filter(powod__contains=searched)

        return render(request, "rss/dashboard-search.html", {"searched": searched, "my_records": my_records})
    else:
        return render(request, "rss/dashboard-search.html", {})
