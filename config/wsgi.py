"""
WSGI config for social-media-backend project.

It exposes the WSGI callable as a module-level variable named `application`.
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Get WSGI application
application = get_wsgi_application()
