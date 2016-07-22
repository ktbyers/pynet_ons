from django.conf.urls import url

from net_system.views import index 
from net_system.views import test

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^/$', index, name='index'),
    url(r'^test.html$', test, name='test'),
]
