"""
WSGI config for store project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

if path not in sys.path:
    sys.path.append(path)

os.ENVIRON[ "DJANGO_SETTINGS_MODULE" ]  =  'store.settings'

from django.core.wsgi import get_wsgi_application


application = get_wsgi_application()
