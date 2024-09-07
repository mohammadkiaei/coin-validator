"""
WSGI config for coinValidator project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import os
import os
from django.core.wsgi import get_wsgi_application

from django.core.wsgi import get_wsgi_applicos

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coinValidator.settings')

application = get_wsgi_application()
