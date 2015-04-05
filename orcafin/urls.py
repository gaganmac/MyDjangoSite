from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog.views import homepage, getContactPage

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', homepage),
    url(r'^hello/$', homepage),
    url(r'^index/$', homepage),
    url(r'^Company/$', homepage),
    url(r'^contact.html/$', getContactPage),
    url(r'^comments/$', include('django_comments.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()