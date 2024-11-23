"""
ASGI config for UASSocialNetwork project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

import django
from channels.routing import get_default_application, ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from friends import routing as friends_routing
from notifications import routing as notifications_routing
from communications import routing as communications_routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UASSocialNetwork.settings')
django.setup()
application = get_asgi_application() # type: ignore

asgi_appProtocol = ProtocolTypeRouter({
    "http": application,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            friends_routing.websocket_urlpatterns +
            notifications_routing.websocket_urlpatterns +
            communications_routing.websocket_urlpatterns
        )
    ),
})
