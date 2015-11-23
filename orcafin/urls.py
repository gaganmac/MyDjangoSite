from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from twiliocom.views import AppointmentCreateView, AppointmentDeleteView, AppointmentListView
from twiliocom.views import AppointmentDetailView, AppointmentUpdateView


urlpatterns = [
    url(r'appointments/', include('twiliocom.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('blog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()

# url(r'^', include('twiliocom', namespace="twiliocom")),