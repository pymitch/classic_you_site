"""
WSGI config for classic_you_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import sys, os

path = '/home/pymitch/classic_you_site'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "classic_you_site.settings")

application = get_wsgi_application()
