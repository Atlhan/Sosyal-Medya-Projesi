import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator 
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Türkat.settings')

django_asgi_app = get_asgi_application()

import chat.routing

application = ProtocolTypeRouter(
  {
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
      AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns))
    ),
  }
)