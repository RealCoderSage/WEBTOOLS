from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InvoicesappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.invoicesapp'
    verbose_name = _("Invoicesapp")
