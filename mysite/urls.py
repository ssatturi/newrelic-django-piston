"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.decorators.cache import cache_control
from piston.resource import Resource
from mysite.handlers import TestHandler1, TestHandler2

cached_resource = cache_control(public=False, maxage=0, s_maxage=0, no_cache=True, must_revalidate=True)

def create_resource(Handler):
    resource = cached_resource(Resource(Handler))
    return resource

testhandler1=create_resource(TestHandler1)
testhandler2=create_resource(TestHandler2)

urlpatterns = [
#    url(r'^admin/', admin.site.urls),
     url(r'^hello', testhandler1, name='testhandler1'),
     url(r'^hi', testhandler2, name='testhandler2')

]
