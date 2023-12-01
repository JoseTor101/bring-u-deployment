import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bring_u.settings')
django.setup()

from django.core.asgi import get_asgi_application
import chat.routing
from channels.routing import get_default_application


application = get_default_application()
