"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

#import newrelic.agent
#newrelic.agent.initialize('/etc/newrelic.ini', 'testing')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
#application = newrelic.agent.WSGIApplicationWrapper(application)


#application = get_wsgi_application()
