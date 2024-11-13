"""
ASGI config for UASSocialNetwork project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

import django
from channels.routing import get_default_application # type: ignore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UASSocialNetwork.settings')
django.setup()
application = get_asgi_application() # type: ignore
