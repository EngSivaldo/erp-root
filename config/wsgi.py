import os
from django.core.wsgi import get_wsgi_application

# Define o arquivo de configurações base
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')

application = get_wsgi_application()