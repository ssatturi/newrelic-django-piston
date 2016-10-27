"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""
hostname='localhost'
if hostname == "localhost":
    import newrelic.agent
    newrelic.agent.initialize('/etc/newrelic.ini', 'testing')

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")


from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
