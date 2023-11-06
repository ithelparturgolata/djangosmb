from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name = ""),
    path("register", views.register, name = "register"),
    path("login", views.login_view, name = "login"),
    path("logout", views.logout_view, name = "logout"),
    #CRUD views
    path("dashboard", views.dashboard, name = "dashboard"),
    path("dashboard_przeciw", views.dashboard_przeciw, name = "dashboard-przeciw"),
    path("dashboard_przez", views.dashboard_przez, name = "dashboard-przez"),
    path("create", views.create_record, name = "create"),
    path("update/<int:pk>", views.update_record, name = "update"),
    path("view/<int:pk>", views.view_record, name = "view"),
    path("delete/<int:pk>", views.delete, name = "delete"),
    path("sms/<int:pk>", views.sms_record, name = "sms"),
    path("pdf", views.pdf, name = "pdf"),
    path("search", views.search, name = "search"),
]