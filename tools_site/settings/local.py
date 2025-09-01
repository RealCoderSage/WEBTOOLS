from .base import *  # noqa
from .base import env

DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="Rq352SWElH_4nlMkeUL--FwL6s6Ri_J0UkpuEmDEuYGBn2C3B_Pi3ntY8rbLrbXb-LA"
)

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = ["http://localhost:8000", "http://127.0.0.1:8000"]
