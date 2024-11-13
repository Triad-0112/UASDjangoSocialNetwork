import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise # type: ignore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UASSocialNetwork.settings')

application = get_wsgi_application()
application = WhiteNoise(application)
