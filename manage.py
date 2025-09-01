#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

import environ


def main():
    """Run administrative tasks with environment support."""
    ROOT_DIR = Path(__file__).resolve().parent
    env = environ.Env()

    # Load environment variables from .env file if present
    env_file = ROOT_DIR / ".env"
    if env_file.exists():
        environ.Env.read_env(str(env_file))

    # Default to local settings if not set
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        env("DJANGO_SETTINGS_MODULE", default="tools_site.settings.local")
    )

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and "
            "available on your PYTHONPATH environment variable. Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
