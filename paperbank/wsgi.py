"""
WSGI config for paperbanka project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from rednoise import DjangoRedNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "paperbank.settings")

application = get_wsgi_application()
application = DjangoRedNoise(application)