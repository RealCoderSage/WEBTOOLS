from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UtmLinksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.utmlinksapp'
    verbose_name = _("Utmlinksapp")
