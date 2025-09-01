from pathlib import Path
import os
import environ

env = environ.Env()

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
APP_DIR = ROOT_DIR / "core_apps"

# Read .env file if present
environ.Env.read_env(os.path.join(ROOT_DIR, ".env"))

# =====================
# Core Django Settings
# =====================
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="unsafe-default-key-change-in-env"
)

DEBUG = env.bool("DJANGO_DEBUG", False)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[])

# =====================
# Installed Apps
# =====================
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

THIRD_PARTY_APPS = [
    "corsheaders"
]

LOCAL_APPS = [
    "core_apps.adminapp",
    "core_apps.invoicesapp",
    "core_apps.usersapp",
    "core_apps.utmlinksapp",
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS 

# =====================
# Middleware
# =====================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'tools_site.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            ROOT_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = 'tools_site.wsgi.application'

# =====================
# Database (from .env)
# =====================
DATABASES = {
    "default": {
        "ENGINE": env("DJANGO_DB_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": env("DJANGO_DB_NAME", default=str(ROOT_DIR / ".instance/web.db")),
    }
}

# =====================
# Auth & Security
# =====================
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

SITE_ID = 1
ADMIN_URL = "adminsite/"

# =====================
# Static & Media
# =====================
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(ROOT_DIR, 'static')]
# STATIC_ROOT = str(ROOT_DIR / "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(ROOT_DIR, 'media')

# AUTH_USER_MODEL = "usersapp.User"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =====================
# Security Headers
# =====================
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "SAMEORIGIN"

# =====================
# Logging
# =====================
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(name)-12s %(asctime)s %(module)s "
                      "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"]
    },
}