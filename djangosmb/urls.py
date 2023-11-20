from django.contrib import admin
from django.urls import path, include
from dashboard import views
from rss import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("dashboard.urls")),
    path("rss/", include("rss.urls")),
    path("telefony/", include("telefony.urls")),
]