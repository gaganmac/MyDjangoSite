from django.conf.urls import include, url
from blog.views import homepage, getContactPage

urlpatterns = [
    url(r'^$', homepage),
    url(r'^hello/$', homepage),
    url(r'^index/$', homepage),
    url(r'^Company/$', homepage),
    url(r'^contact.html/$', getContactPage),
]
