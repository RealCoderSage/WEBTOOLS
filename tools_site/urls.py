from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core_apps.webapp.urls"), name="webapp"),
    path('utmlinksapp/', include("core_apps.utmlinksapp.urls"), name="utmlinksapp"),
    path('invoiceapp/', include("core_apps.invoicesapp.urls"), name="invoiceapp"),
]
