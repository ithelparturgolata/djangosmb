from django.urls import path, include

import dashboard.views
from dashboard import views
# from rss import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name=""),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("dashboard_main", views.dashboard_main, name="dashboard_main"),
]