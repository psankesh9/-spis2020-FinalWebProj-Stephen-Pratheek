"""
WSGI config for BlogProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
#made no edits to this file comes inbuilt when creating django app folder
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BlogProject.settings')

application = get_wsgi_application()
