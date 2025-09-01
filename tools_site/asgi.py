"""
ASGI config for tools_site project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import environ
from pathlib import Path
from django.core.asgi import get_asgi_application

ROOT_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()

# Try to read .env if it exists
env_file = ROOT_DIR / ".env"
if env_file.exists():
    environ.Env.read_env(str(env_file))

# Fallback to local settings if not defined
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    env("DJANGO_SETTINGS_MODULE", default="tools_site.settings.local")
)

application = get_asgi_application()