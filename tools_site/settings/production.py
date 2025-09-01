from .base import *  # noqa
from .base import env

ADMINS = [("Alpha", "api.imperfect@gmail.com")]

DEBUG = env.bool("DJANGO_DEBUG", False)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["*"])

CSRF_TRUSTED_ORIGINS = env.list(
    "CSRF_TRUSTED_ORIGINS",
    default=["https://yourdomain.com", "https://www.yourdomain.com"],
)

# Security flags configurable via .env
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", True)
SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE", True)
CSRF_COOKIE_SECURE = env.bool("DJANGO_CSRF_COOKIE_SECURE", True)
