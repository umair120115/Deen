"""
ASGI config for deen project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter,URLRouter
from hadith.middleware import JWTAuthMiddleware
from django.core.asgi import get_asgi_application
from hadith import routing
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deen.settings")

# application = get_asgi_application()
application= ProtocolTypeRouter({
    "http":get_asgi_application(),
    'websocket':JWTAuthMiddleware(
        URLRouter(
            routing.websocket_urlpatterns
            
        )

    )
})


