from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("dashboard_sms", views.dashboard_sms,
         name="dashboard_sms"),
    path("dashboard_sms_kontrahent", views.dashboard_sms_kontrahent,
         name="dashboard-sms-kontrahent"),
    path("dashboard_sms_blok", views.dashboard_sms_blok,
         name="dashboard-sms-blok"),
    path("view/<int:pk>", views.view_record_sms, name="sms-view"),
    path("view/<int:pk>", views.view_record_sms_blok, name="sms-view-blok"),
    path("sms/<int:pk>", views.sms_record, name="sms-sms"),
    path("search", views.search, name="search-sms"),
    path("search_kontrahent", views.search_kontrahent, name="search-sms-kontrahent"),
    path("search_blok", views.search_blok, name="search-sms-blok"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
