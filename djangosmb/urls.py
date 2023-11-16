from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("rss.urls")),
    path("telefony", include("telefony.urls")),
]
