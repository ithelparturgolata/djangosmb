from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("dashboard_sms", views.dashboard_sms,
         name="dashboard_sms"),
    path("dashboard_ce_sms", views.dashboard_ce_sms,
         name="dashboard-ce-sms"),
    path("dashboard_ce_sms_blok", views.dashboard_ce_sms_blok,
         name="dashboard-ce-sms-blok"),
    path("dashboard_nw_sms", views.dashboard_nw_sms,
         name="dashboard-nw-sms"),
    path("dashboard_nw_sms_blok", views.dashboard_nw_sms_blok,
         name="dashboard-nw-sms-blok"),
    path("dashboard_ns_sms", views.dashboard_ns_sms,
         name="dashboard-ns-sms"),
    path("dashboard_ns_sms_blok", views.dashboard_ns_sms_blok,
         name="dashboard-ns-sms-blok"),

    path("view/<int:pk>", views.view_record_sms, name="sms-view"),
    path("sms/<int:pk>", views.sms_record_sms, name="sms-sms"),
    path("search", views.search, name="search-sms"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
